"""Waf tool for building documentation with Sphinx.

Using Sphinx from Waf is a little tricky. That's because Sphinx is not really a
compiler -- it just produces a bunch of output files from a bunch of input
files. This implementation leaves the dependency tracking to Sphinx (and the
generated Makefile, for texinfo) and always runs their builds. It's not the
most clever approach, but it *is* the most reliable.

There are some ambitious approaches [#econ-project-templates]_ which use Sphinx
internals to attempt to track Sphinx dependencies and bring them into Waf.

.. [#econ-project-templates]: https://github.com/hmgaudecker/econ-project-templates/blob/python/.mywaflib/waflib/extras/sphinx_build.py

"""

import waflib
from waflib.Configure import conf

def _node_or_bust(node_or_path, node_func):
    return (node_or_path
            if isinstance(node_or_path, waflib.Node.Node)
            else node_func(node_or_path))

def configure(ctx):
    # Although Sphinx can be used as a Python module, it might not be safe to
    # launch multiple simulatenous mains in different threads. Just to be safe,
    # use the executable to spawn new processes.
    ctx.find_program('sphinx-build', var='SPHINX_BUILD')
    # For info docs.
    ctx.find_program('make', mandatory=False)
    ctx.find_program('makeinfo', mandatory=False)

class SphinxBuild(waflib.Task.Task):
    """Handle run of sphinx-build."""
    # Leave dependency processing to Sphinx itself. Always build.
    always = True

    def run(self):
        conf_node = self.inputs[0]
        args = [
            self.env.SPHINX_BUILD,
            '-b', self.sphinx_builder,
            '-d', self.doctrees_node.abspath(),
        ]
        if self.quiet:
            args.append('-q')
        if self.nitpicky:
            args.append('-n')
        if self.warning_is_error:
            args.append('-W')
        args += [
            self.src_dir_node.abspath(),
            self.outputs[0].abspath(),
        ]
        return self.exec_command(args)

class SphinxMakeInfo(waflib.Task.Task):
    # Leave dependency processing to Sphinx's generated Makefile. Always build.
    always = True
    # Run this after SphinxBuild only.
    after = 'SphinxBuild'

    def run(self):
        return self.exec_command(
            [self.env.MAKE, 'info'],
            cwd=self.outputs[0].abspath())

@waflib.TaskGen.feature('sphinx')
@waflib.TaskGen.before_method('process_source')
def apply_sphinx(task_gen):
    """Set up the task generator for building with Sphinx.

    This method overrides the processing by
    :py:meth:`waflib.TaskGen.process_source`.
    """
    # Initialize the keywords.
    try:
        requested_builder = task_gen.builder
    except AttributeError:
        raise waflib.Errors.WafError(
            'Sphinx task generator missing necessary keyword: builder')

    # Make sure that 'make' and 'makeinfo' are available if the 'info' builder
    # was requested.
    for prog in ['make', 'makeinfo']:
        if not task_gen.env[prog.upper()]:
            raise waflib.Errors.WafError(
                "Sphinx 'info' builder requested"
                " but '{0}' program not found!".format(prog))

    # Turning off quiet will print out all of the Sphinx output. The default is
    # to be quiet because builds can happen in parallel which will cause output
    # to be interleaved. However, it is feasible that turning on the output
    # might be useful for debugging. Note that not being quiet is not the same
    # as Sphinx being verbose.
    source = getattr(task_gen, 'source', [])
    target = getattr(task_gen, 'target', [])
    quiet = getattr(task_gen, 'quiet', True)
    warning_is_error = getattr(task_gen, 'warningiserror', False)
    nitpicky = getattr(task_gen, 'nitpicky', False)

    # There is no builder called 'info', but if requested, we'll build the info
    # manual just like the Sphinx Makefile.
    sphinx_builder = (
        requested_builder if requested_builder != 'info' else 'texinfo')

    # There is a helper method for inputs, so we may as well use it.
    in_nodes = task_gen.to_nodes(source)
    in_nodes_len = len(in_nodes)
    if in_nodes_len != 1:
        raise waflib.Errors.WafError(
            'Sphinx task generator takes one input, {0} given.'.format(
                in_nodes_len))

    conf_node = in_nodes[0]
    src_dir_node = conf_node.parent

    # Outputs have no such helper...
    if not target:
        out_dir_node = src_dir_node.get_bld().find_or_declare(sphinx_builder)
    else:
        outs = waflib.Utils.to_list(target)
        if len(outs) != 1:
            raise waflib.Errors.WafError(
                'If specified, Sphinx task generator can only take one output.'
            )
        out_dir_node = _node_or_bust(outs[0], task_gen.path.find_or_declare)

    # TODO: We're really not sure what the best approach is yet.
    # Set up a shared doctrees directory, just like the Sphinx Makefile does.
    doctrees_node = out_dir_node.parent.find_or_declare('doctrees')
    # Set up a private doctrees directory to avoid race conditions.
    # doctrees_node = out_dir_node.find_or_declare('.doctrees')

    task = task_gen.create_task('SphinxBuild', src=conf_node, tgt=out_dir_node)
    # Assign attributes necessary for task methods.
    task.requested_builder = requested_builder
    task.sphinx_builder = sphinx_builder
    task.src_dir_node = src_dir_node
    task.doctrees_node = doctrees_node
    task.quiet = quiet
    task.warning_is_error = warning_is_error
    task.nitpicky = nitpicky

    # The info builder requires some special considerations because it has an
    # extra step -- we have to run a Makefile in the texinfo directory. Ugh :(
    if requested_builder == 'info':
        # Setting the target to the output directory unfortunately produces a
        # warning when the runner zone output is turned. We have to declare an
        # output else the task won't build, but we don't know what the outputs
        # are going to be!
        task = task_gen.create_task('SphinxMakeInfo', tgt=out_dir_node)

    # Prevent execution of process_source. We don't need it because we are
    # letting Sphinx decide on the sources.
    # Following the lead of code in waflib.
    task_gen.source = []
    # Also possible.
    # task_gen.meths.remove('process_source')
