# -*- mode: python; coding: utf-8; -*-

# Based on
# - https://github.com/hmgaudecker/econ-project-templates/blob/python/.mywaflib/waflib/extras/sphinx_build.py
# - http://docs.waf.googlecode.com/git/book_17/single.html#_a_compiler_producing_source_files_with_names_unknown_in_advance
#
# Hans-Martin von Gaudecker, 2012
# Sean Fisk, 2014

"""Waf tool for building documentation with Sphinx."""

import os
import sys
import uuid
import re

import waflib
from waflib.Configure import conf

MAKEINFO_VERSION_RE = re.compile(r'makeinfo \(GNU texinfo\) (\d+)\.(\d+)')
# http://svn.savannah.gnu.org/viewvc/*checkout*/trunk/NEWS?root=texinfo
MAKEINFO_MIN_VERSION = (4, 13)

def _version_tuple_to_string(version_tuple):
    return '.'.join(str(x) for x in version_tuple)


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

class SphinxBuild(waflib.Task.Task):
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
        """Use Sphinx's internal environment to find the dependencies."""
        sphinx_app = self.sphinx_app

        # From Sphinx BuildEnvironment.update() docstring:
        # "(Re-)read all files new or changed since last update."
        summary, num_docs_reread, doc_name_iterator = sphinx_app.env.update(
            sphinx_app.config,
            sphinx_app.srcdir,
            sphinx_app.doctreedir,
            sphinx_app,
        )
        # TODO: Decide whether this output is necessary.
        # sphinx_app.info(summary)
        # Avoid duplicates by using a set.
        dependee_nodes = set()
        # for doc_path_basename in sphinx_app.builder.status_iterator(
        #         doc_name_iterator, 'reading sources... '):
        for doc_name in doc_name_iterator:
            doc_path = doc_name + sphinx_app.config.source_suffix
            doc_node = self.src_dir_node.find_node([doc_path])
            if doc_node is None:
                raise waflib.Errors.WafError(
                    'Could not find Sphinx document node: {0}'.format(
                        doc_path))
            dependee_nodes.add(doc_node)

        for dependee_paths in sphinx_app.env.dependencies.values():
            for dependee_path in dependee_paths:
                node = (
                    self.src_dir_node.find_node([dependee_path]) or
                    # Try as absolute path if no success relative to
                    # src_dir.
                    self.src_dir_node.ctx.root.find_resource(dependee_path))
                if node is None:
                    raise waflib.Errors.WafError(
                        'Could not find Sphinx document dependency node: {0}'
                        .format(doc_path))
                dependee_nodes.add(node)

        # TODO: Do we need to call sphinx_app.env.check_dependents(...) in case
        # section numbers have changed?

        # "The return value is a tuple containing a list of nodes to depend on
        # and serializable data for custom uses." Make sure to convert the
        # nodes back to a list before returning.
        return (list(dependee_nodes), [])

    def _maybe_add_info_task(self):
        if self.requested_builder != 'info':
            return

        texi_node = None
        for in_node in self.outputs:
            if in_node.suffix() == '.texi':
                texi_node = in_node
                break
        if texi_node is None:
            raise waflib.Errors.WafError(
                'Could not find the texi file for Sphinx info builder!')
        # Put the .texi node first to allow us to determine the input to
        # makeinfo.
        self.outputs.remove(texi_node)
        self.outputs = [texi_node] + self.outputs

        # Create the task.
        task = self.generator.create_task(
            'SphinxMakeinfo',
            src=self.outputs,
            tgt=texi_node.change_ext('.info'))
        self.more_tasks = [task]

    def run(self):
        """Run sphinx-build."""
        # Running Sphinx *should* be this easy:
        #
        #     self.sphinx_app.build()
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
        excludes = ['Makefile']
        if self.sphinx_builder == 'texinfo':
            excludes.append('*.info')

        # quiet=True disables a warning printed in verbose mode.
        self.outputs = self.out_dir_node.ant_glob(
            '**', quiet=True, excl=excludes)

        self._maybe_add_info_task()

        # Set up the raw_deps list for later use in runnable_status(). This
        # will allow us to determine whether to rebuild.
        self.generator.bld.raw_deps[self.uid()] = (
            [self.signature()] + self.outputs)

        return ret

    def runnable_status(self):
        ret = super(SphinxBuild, self).runnable_status()
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

            # When this task can be skipped, force creation of the info task.
            # That does not necessarily mean the info task will run.
            self.outputs = out_nodes
            self._maybe_add_info_task()

        return ret

class SphinxMakeinfo(waflib.Task.Task):
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
        requested_builder = task_gen.builder
    except AttributeError:
        raise waflib.Errors.WafError(
            'Sphinx task generator missing necessary keyword: builder')

    # Make sure that 'makeinfo' is available if the 'info' builder was
    # requested.
    if not task_gen.env.MAKEINFO:
        raise waflib.Errors.WafError(
            "Sphinx 'info' builder requested but 'makeinfo' program not found!"
        )

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

    # No targets; they will be assigned after Sphinx runs.
    task = task_gen.create_task('SphinxBuild', src=conf_node)
    # Assign attributes necessary for task methods.
    task.requested_builder = requested_builder
    task.sphinx_builder = sphinx_builder
    task.src_dir_node = src_dir_node
    task.out_dir_node = out_dir_node
    task.doctrees_node = doctrees_node
    task.quiet = quiet
    task.warning_is_error = warning_is_error
    task.nitpicky = nitpicky

    # Set up the Sphinx application instance.
    from sphinx.application import Sphinx
    task.sphinx_app = Sphinx(
        srcdir=src_dir_node.abspath(),
        confdir=src_dir_node.abspath(),
        outdir=out_dir_node.abspath(),
        doctreedir=doctrees_node.abspath(),
        buildername=sphinx_builder,
        warningiserror=warning_is_error,
        confoverrides=(
            {'nitpicky': True} if nitpicky
            else None),
        # Indicates the file where status messages should be printed. Typically
        # sys.stdout or sys.stderr, but can be None to disable. Since builds
        # can happen in parallel, don't output anything.
        status=None,
    )

    # Prevent execution of process_source. We don't need it because we are
    # letting Sphinx decide on the sources.
    # Following the lead of code in waflib.
    task_gen.source = []
    # Also possible.
    # task_gen.meths.remove('process_source')
