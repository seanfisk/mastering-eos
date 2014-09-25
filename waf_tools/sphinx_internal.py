"""Waf tool for building documentation with Sphinx.

This version works really well with with Waf at the cost of staggering
complexity.

Based on
- https://github.com/hmgaudecker/econ-project-templates/blob/python/.mywaflib/waflib/extras/sphinx_build.py
- http://docs.waf.googlecode.com/git/book_17/single.html#_a_compiler_producing_source_files_with_names_unknown_in_advance

Hans-Martin von Gaudecker, 2012
Sean Fisk, 2014
"""

import os
import sys
import uuid
import re
import shutil

import waflib
from waflib.Configure import conf
from sphinx.application import Sphinx


MAKEINFO_VERSION_RE = re.compile(r'makeinfo \(GNU texinfo\) (\d+)\.(\d+)')
# http://svn.savannah.gnu.org/viewvc/*checkout*/trunk/NEWS?root=texinfo
MAKEINFO_MIN_VERSION = (4, 13)

class InfoBuilder(object):
    tool_name = 'MAKEINFO'
    in_suffix = '.texi'
    out_suffix = '.info'
    sphinx_builder = 'texinfo'

    def create_task(self, task_gen, src, tgt):
        return [task_gen.create_task('sphinx_makeinfo', src=src, tgt=tgt)]

class PdflatexBuilder(object):
    tool_name = 'PDFLATEX'
    in_suffix = '.tex'
    out_suffix = '.pdf'
    sphinx_builder = 'latex'

    def create_task(self, task_gen, src, tgt):
        tasks = []
        orig_tex_node = src[0]
        dep_nodes = src[1:]
        # We don't want to pollute the LaTeX sources directory (which is in the
        # build directory) with all the extra files LaTeX generates because
        # that will interfere with our Sphinx output detection. The Waf tex
        # tool sets the cwd to the parent of the first input, but that only
        # makes sense if the sources are not in the build directory. Hack
        # around it by copying the .tex file to the desired output directory
        # and setting TEXINPUTS. THIS IS UGLY.
        copied_tex_node = tgt.change_ext('.tex')
        copy_task = task_gen.create_task(
            'copy_file', src=orig_tex_node, tgt=copied_tex_node)
        tasks.append(copy_task)
        # The following code is based on apply_tex() from Waf tex tool.
        latex_task = task_gen.create_task(
            'pdflatex',
            src=copied_tex_node,
            tgt=tgt)
        latex_task.env.TEXINPUTS = orig_tex_node.parent.abspath()
        # Set the build order to prevent node signature issues.
        latex_task.set_run_after(copy_task)
        # Add manual dependencies.
        task_gen.bld.node_deps[latex_task.uid()] = dep_nodes
        tasks.append(latex_task)
        return tasks

FOLLOWUP_BUILDERS = {
    'info': InfoBuilder(),
    'latexpdf': PdflatexBuilder(),
}
"""Mapping of Sphinx composite builders."""

def _version_tuple_to_string(version_tuple):
    return '.'.join(str(x) for x in version_tuple)

def _node_or_bust(node_or_path, node_func):
    return (node_or_path
            if isinstance(node_or_path, waflib.Node.Node)
            else node_func(node_or_path))

def _sorted_nodes(nodes):
    """Sort nodes on their names."""
    return sorted(nodes, key=lambda node: node.name)

@conf
def warn_about_old_makeinfo(ctx):
    version_out = ctx.cmd_and_log([ctx.env.MAKEINFO, '--version'])
    version_str = version_out.splitlines()[0].rstrip()
    match = MAKEINFO_VERSION_RE.match(version_str)
    if match is None:
        ctx.fatal("Couldn't verify makeinfo version!")
    version_tuple = tuple(int(x) for x in match.groups())
    if version_tuple < MAKEINFO_MIN_VERSION:
        waflib.Logs.warn(
'''Your makeinfo version ({0}) is too old to support UTF-8.
You will see warnings; upgrade to {1} to get UTF-8 support.'''.format(
    _version_tuple_to_string(version_tuple),
    _version_tuple_to_string(MAKEINFO_MIN_VERSION)))

def configure(ctx):
    ctx.find_program('sphinx-build', var='SPHINX_BUILD')
    if ctx.find_program('makeinfo', mandatory=False):
        ctx.warn_about_old_makeinfo()
    ctx.load('tex')

# PEP8 dictates CamelCase class names, but the prevailing style with Waf seems
# to be lowercase. Also, waflib.Task.Task.__str__ strips off a trailing '_task'
# from the name.

class copy_file_task(waflib.Task.Task):
    """Copy a file. Used for building the LaTeX PDF in a different
    directory.
    """

    def run(self):
        shutil.copyfile(self.inputs[0].abspath(), self.outputs[0].abspath())

class sphinx_build_task(waflib.Task.Task):
    """Handle run of sphinx-build."""

    vars = ['SPHINX_BUILD']

    def uid(self):
        # Tasks are not allowed to have the same uid. The default uid is
        # computed by hashing the class name, inputs, and outputs. For multiple
        # invocations of this class, this will be the same. However, if we
        # throw in the requested builder name, it should not.
        try:
            return self.uid_
        except AttributeError:
            # Based on Task.uid()
            m = waflib.Utils.md5()
            up = m.update
            up(self.__class__.__name__.encode())
            for x in self.inputs:
                up(x.abspath().encode())
            up(self.requested_builder.encode())
            self.uid_ = m.digest()
            return self.uid_

    def scan(self):
        """Use Sphinx's internal environment to find the outdated dependencies."""
        # Set up the Sphinx application instance.
        app = Sphinx(
            srcdir=self.src_dir_node.abspath(),
            confdir=self.src_dir_node.abspath(),
            outdir=self.out_dir_node.abspath(),
            doctreedir=self.doctrees_node.abspath(),
            buildername=self.sphinx_builder,
            warningiserror=self.warning_is_error,
            confoverrides=(
                {'nitpicky': True} if self.nitpicky
                else None),
            # Indicates the file where status messages should be printed.
            # Typically sys.stdout or sys.stderr, but can be None to disable.
            # Since builds can happen in parallel, don't output anything.
            status=None,
        )

        # Update dependencies dictionary by updating. From Sphinx
        # BuildEnvironment.update() docstring: "(Re-)read all files new or
        # changed since last update." Note that this only returns *doc names
        # that have been updated*.
        summary, num_docs_reread, updated_doc_names_iterator = app.env.update(
            app.config,
            app.srcdir,
            app.doctreedir,
            app,
        )
        # Avoid duplicates by using a set.
        dependency_nodes = set()

        # Add documents which have been updated and their dependencies. It's
        # very important to add both of these, because their content needs to
        # be tracked by Waf from the first build. Because we are using Sphinx's
        # BuildEnvironment.update() method, each file will only be listed as a
        # dependency *if it changed*.

        # Add documents which have been updated.
        for doc_name in updated_doc_names_iterator:
            doc_path = doc_name + app.config.source_suffix
            doc_node = self.src_dir_node.find_node([doc_path])
            if doc_node is None:
                raise waflib.Errors.WafError(
                    'Could not find Sphinx document node: {0}'.format(
                        doc_path))
            dependency_nodes.add(doc_node)

        # Add dependencies of documents which have been updated.
        for dependency_paths in app.env.dependencies.values():
            for dependency_path in dependency_paths:
                node = (
                    self.src_dir_node.find_node([dependency_path]) or
                    # Try as absolute path if no success relative to
                    # src_dir.
                    self.src_dir_node.ctx.root.find_resource(dependency_path))
                if node is None:
                    raise waflib.Errors.WafError(
                        'Could not find Sphinx document dependency node: {0}'
                        .format(doc_path))
                dependency_nodes.add(node)

        # Sphinx's Builder.build() methods calls
        # BuildEnvironment.check_dependents(...) to see if section numbers have
        # changed. I don't think we need to call this, though, because this can
        # only happen if an actual file changes. Waf is only reponsible for
        # triggering the re-build, not for telling Sphinx what needs to be
        # re-built.

        # Return these sorted for a consistent ordering. Make sure to convert
        # the nodes back to a list before returning (which sorted() does).
        #
        # The second list is for raw_deps, which we don't need at this point.
        return (_sorted_nodes(dependency_nodes), [])

    def run(self):
        # After creating a Sphinx application, running Sphinx *should* be this
        # easy:
        #
        #     sphinx_app.build()
        #
        # However, its build using the Application API is not thread-safe
        # (apparently, because we've had problems). That sort of goes against
        # one of the major points of Waf.
        #
        # Calling the 'sphinx-build' executable, on the other hand, seems fine
        # to do in parallel. It's not the best situation, but it's the best
        # we've got.
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
            self.out_dir_node.abspath(),
        ]
        ret = self.exec_command(args)

        # Add almost everything found in the output directory tree as an
        # output. Not elegant, but pragmatic.
        #
        # Don't include generated Makefiles -- we're not using those.
        # No .doctrees directory either.
        #
        # quiet=True disables a warning printed in verbose mode.
        #
        # Return sorted to get a consistent ordering.
        self.outputs = _sorted_nodes(
            self.out_dir_node.ant_glob(
                '**', quiet=True, excl=['Makefile', '.doctrees', '.buildinfo'])
        )

        self._maybe_add_followup_task()

        # Set up the raw_deps list for later use in runnable_status(). This
        # will allow us to determine whether to rebuild.
        self.generator.bld.raw_deps[self.uid()] = (
            [self.signature()] + self.outputs)

        return ret

    def runnable_status(self):
        ret = super(sphinx_build_task, self).runnable_status()
        # Don't bother checking anything more if Waf already says this task
        # needs to be run.
        if ret == waflib.Task.SKIP_ME:
            raw_deps = self.generator.bld.raw_deps[self.uid()]

            # If the task signature changed, re-run.
            if raw_deps[0] != self.signature():
                return waflib.Task.RUN_ME

            # If any of the old build files were deleted, re-run.
            out_nodes = raw_deps[1:]
            for node in out_nodes:
                if not os.path.exists(node.abspath()):
                    return waflib.Task.RUN_ME

            # When this task can be skipped, force creation of follow-up tasks.
            # That does not necessarily mean the follow-up tasks will run.
            self.outputs = out_nodes
            self._maybe_add_followup_task()

        return ret

    def _maybe_add_followup_task(self):
        try:
            followup_builder = FOLLOWUP_BUILDERS[self.requested_builder]
        except KeyError:
            return

        main_in_node = None
        for in_node in self.outputs:
            if in_node.suffix() == followup_builder.in_suffix:
                main_in_node = in_node
                break
        if main_in_node is None:
            raise waflib.Errors.WafError(
                'Could not find the {0} file for Sphinx {1} builder!'.format(
                    followup_builder.in_suffix, self.requested_builder))
        # Put the main node first to allow us to easily determine the input.
        self.outputs.remove(main_in_node)
        self.outputs = [main_in_node] + self.outputs

        out_dir_node = self.out_dir_node.parent.find_or_declare(
            self.requested_builder)
        out_dir_node.mkdir()

        out_node = out_dir_node.find_or_declare(
            os.path.splitext(main_in_node.name)[0] +
            followup_builder.out_suffix)

        # Create the tasks and add to more_tasks.
        self.more_tasks = followup_builder.create_task(
            self.generator, src=self.outputs, tgt=out_node)

    def __str__(self):
        """Make the output look a little nicer. Reimplemented from
        :meth:`waflib.Task.Task.__str__`.
        """
        # These tasks will never have any declared targets, so don't bother.
        return 'sphinx_build_{0}: {1}\n'.format(
            self.sphinx_builder,
            ' '.join(n.nice_path() for n in self.inputs))

class sphinx_makeinfo_task(waflib.Task.Task):
    """Handle run of makeinfo for Sphinx's texinfo output."""

    vars = ['MAKEINFO']

    def run(self):
        # Mostly copied from the Sphinx Makefile that gets generated and put in
        # the texinfo output directory. It is so simple that the info output is
        # just reimplemented here.
        texi_node = self.inputs[0]
        return self.exec_command(
            [
                self.env.MAKEINFO,
                '--no-split',
                '-o', self.outputs[0].abspath(),
                texi_node.abspath()
            ],
            # Set the cwd so that relative paths in the .texi file will be
            # found.
            cwd=texi_node.parent.abspath())

@waflib.TaskGen.feature('sphinx')
@waflib.TaskGen.before_method('process_source')
def apply_sphinx(task_gen):
    """Set up the task generator with a Sphinx instance and create a task.

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
    if len(requested_builders) != len(set(requested_builders)):
        raise waflib.Errors.WafError(
            "Sphinx 'builder' keyword cannot contain duplicates.")

    # Make sure that the requisite tools are available if builders with
    # follow-ups were requested.
    for requested_builder in requested_builders:
        try:
            followup_builder = FOLLOWUP_BUILDERS[requested_builder]
        except KeyError:
            continue

        tool = followup_builder.tool_name
        if not task_gen.env[tool.upper()]:
            raise waflib.Errors.WafError((
                "Sphinx '{0}' builder requested "
                "but '{1}' program not found!").format(
                    requested_builder, tool))

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
            sphinx_builder = (
                FOLLOWUP_BUILDERS[requested_builder].sphinx_builder)
        except KeyError:
            sphinx_builder = requested_builder

        out_dir_node = out_dir_parent_node.find_or_declare(sphinx_builder)

        # Although it usually doesn't happen, we had trouble with race
        # conditions using a shared doctrees directory. Set up a private
        # doctrees directory to avoid race conditions.
        doctrees_node = (
            out_dir_node.find_or_declare('.doctrees')
            # The epub builder spits out unknown mimetype warnings if we throw
            # the doctree in its output directory.
            if requested_builder != 'epub'
            else out_dir_parent_node.find_or_declare('.epub-doctrees'))

        # No targets; they will be assigned after Sphinx runs.
        #
        # Our input is just the conf node. Note that we can't assign our
        # dependencies as inputs because they are not *all of the dependencies
        # of the documentation*, they are just *dependencies of the updated
        # files*. Unfortunately, Sphinx doesn't provide an easy way to get all
        # dependencies without re-reading all of the documents, which is
        # exactly what we're trying not do to.
        task = task_gen.create_task('sphinx_build', src=conf_node)
        # Assign attributes necessary for task methods.
        task.requested_builder = requested_builder
        task.sphinx_builder = sphinx_builder
        task.src_dir_node = src_dir_node
        task.out_dir_node = out_dir_node
        task.doctrees_node = doctrees_node
        task.quiet = quiet
        task.warning_is_error = warning_is_error
        task.nitpicky = nitpicky

        # Set the task order if that was requested.
        for attr in ['after', 'before']:
            setattr(task, attr, getattr(task_gen, attr, []))

    # Prevent execution of process_source. We don't need it because we are
    # letting Sphinx decide on the sources.
    # Following the lead of code in waflib:
    task_gen.source = []
    # Also possible.
    # task_gen.meths.remove('process_source')
