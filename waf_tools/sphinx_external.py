"""Waf tool for building documentation with Sphinx.

This version leaves the dependency tracking to Sphinx (and the generated
Makefile s). It always runs the builds, which is somewhat less efficient.
However, it has the virtue of being far simpler than the "internal"
implementation.

sphinx-build touches the output files and causes their modification time to
change regardless of the need to write them. But Make uses modification times
(not file hashes) to check for modifications. Therefore, using Make for the
purpose of follow-up builds is pointless anyway because it will force a build.
I'm not sure if this is a bug, an oversight, or both. I could be wrong too, who
knows.
"""

import waflib
from waflib.Configure import conf

FOLLOWUP_BUILDERS = {
    'info': 'texinfo',
    'latexpdf': 'latex',
}
"""Mapping of builder to real Sphinx builder."""

def _node_or_bust(node_or_path, node_func):
    return (node_or_path
            if isinstance(node_or_path, waflib.Node.Node)
            else node_func(node_or_path))

def configure(ctx):
    # Although Sphinx can be used as a Python module, it might not be safe to
    # launch multiple simulatenous mains in different threads. Just to be safe,
    # use the executable to spawn new processes.
    ctx.find_program('sphinx-build', var='SPHINX_BUILD')
    # For follow-up builders.
    ctx.find_program('make', mandatory=False)
    # Don't try to find makeinfo or pdflatex here because the Makefile won't
    # respect those selected here anyway. It will use the executables on the
    # PATH.

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

class SphinxRunMake(waflib.Task.Task):
    # Leave dependency processing to Sphinx's generated Makefile. Always build.
    always = True

    def run(self):
        return self.exec_command(
            [self.env.MAKE], cwd=self.outputs[0].abspath())

@waflib.TaskGen.feature('sphinx')
@waflib.TaskGen.before_method('process_source')
def apply_sphinx(task_gen):
    """Set up the task generator for building with Sphinx.

    This method overrides the processing by
    :py:meth:`waflib.TaskGen.process_source`.
    """
    # Initialize the keywords.
    try:
        requested_builders = waflib.Utils.to_list(task_gen.builders)
    except AttributeError:
        raise waflib.Errors.WafError(
            'Sphinx task generator missing necessary keyword: builders')

    # Check for dupes.
    requested_builders_set = set(requested_builders)
    if len(requested_builders) != len(requested_builders_set):
        raise waflib.Errors.WafError(
            "Sphinx 'builder' keyword cannot contain duplicates.")

    # Make sure that 'make' is available if one of the follow-up builders was
    # requested.
    intersect = requested_builders_set.intersection(FOLLOWUP_BUILDERS.keys())
    if intersect and not task_gen.env.MAKE:
        raise waflib.Errors.WafError((
            "Sphinx builder{0} {1} requested "
            "but 'make' program not found!").format(
                's' if len(intersect) > 1 else '',
                ' and '.join("'{0}'".format(b) for b in intersect)))

    source = getattr(task_gen, 'source', [])
    target = getattr(task_gen, 'target', [])
    # Turning off quiet will print out all of the Sphinx output. The default is
    # to be quiet because builds can happen in parallel which will cause output
    # to be interleaved. However, it is feasible that turning on the output
    # might be useful for debugging. Note that not being quiet is not the same
    # as Sphinx being verbose.
    quiet = getattr(task_gen, 'quiet', True)
    warning_is_error = getattr(task_gen, 'warningiserror', False)
    nitpicky = getattr(task_gen, 'nitpicky', False)

    # There is a helper method for inputs, so we may as well use it.
    in_nodes = task_gen.to_nodes(source)
    in_nodes_len = len(in_nodes)
    if in_nodes_len != 1:
        raise waflib.Errors.WafError(
            'Sphinx task generator takes one input, {0} given.'.format(
                in_nodes_len))

    conf_node = in_nodes[0]
    src_dir_node = conf_node.parent

    # Outputs have no helper...
    if not target:
        out_dir_parent_node = src_dir_node.get_bld()
    else:
        outs = waflib.Utils.to_list(target)
        if len(outs) != 1:
            raise waflib.Errors.WafError(
                'If specified, Sphinx task generator '
                'can only take one output.'
            )
        out_dir_parent_node = _node_or_bust(
            outs[0], task_gen.path.find_or_declare)

    for requested_builder in requested_builders:
        # Get the real Sphinx builders for different follow-up builders given.
        try:
            sphinx_builder = FOLLOWUP_BUILDERS[requested_builder]
        except KeyError:
            sphinx_builder = requested_builder

        out_dir_node = out_dir_parent_node.find_or_declare(sphinx_builder)

        # Although it usually doesn't happen, we had trouble with race
        # conditions using a shared doctrees directory. Set up a private
        # doctrees directory to avoid race conditions.
        doctrees_node = out_dir_node.find_or_declare('.doctrees')

        task = task_gen.create_task(
            'SphinxBuild', src=conf_node, tgt=out_dir_node)
        # Assign attributes necessary for task methods.
        task.requested_builder = requested_builder
        task.sphinx_builder = sphinx_builder
        task.src_dir_node = src_dir_node
        task.doctrees_node = doctrees_node
        task.quiet = quiet
        task.warning_is_error = warning_is_error
        task.nitpicky = nitpicky

        # The follow-up builders have an extra step -- we have to run a
        # Makefile in their output directories. Ugh :(
        if requested_builder in FOLLOWUP_BUILDERS:
            # Setting the target to the output directory unfortunately produces
            # a warning when the runner zone output is turned. We have to
            # declare an output else the task won't build, but we don't know
            # what the outputs are going to be!
            make_task = task_gen.create_task(
                'SphinxRunMake', tgt=out_dir_node)
            # Set the build order.
            make_task.set_run_after(task)

    # Prevent execution of process_source. We don't need it because we are
    # letting Sphinx decide on the sources.
    # Following the lead of code in waflib.
    task_gen.source = []
    # Also possible.
    # task_gen.meths.remove('process_source')
