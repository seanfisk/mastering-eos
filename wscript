# -*- mode: python; coding: utf-8; -*-

# Waf build file
#
# Keep this file and all Waf files Python 2/3 single-source compatible (using
# six when necessary).

import os
from os.path import join
import textwrap
import shutil

import waflib
from waflib.Task import always_run

# Waf constants
APPNAME = 'mastering-eos'
VERSION = '0.1'
top = '.'
out = 'build'

# Process the poster first, as it takes more time to generate but has less
# dependencies.
SUBDIRS = ['poster', 'manual']

def options(ctx):
    # We need to use XeLaTeX or LuaLaTeX to support custom fonts on our poster.
    # We'd like to use LuaLaTeX, as it's been named as the successor to pdfTeX.
    # However, our LuaLaTeX installation on EOS is broken at this time of
    # writing (2014-09-25). XeLaTex works fine, so we've made it the default.
    latex_engines = ['xelatex', 'lualatex']
    default_latex_engine = latex_engines[0]
    ctx.add_option(
        '-l', '--latex-engine',
        choices=latex_engines, default=default_latex_engine,
        help=("set LaTeX engine; valid values {0}; "
              "default is '{1}'").format(
                  ', '.join("'{0}'".format(e) for e in latex_engines),
                  default_latex_engine))

    ctx.load('tex')
    ctx.load('sphinx_internal', tooldir='waf_tools')
    ctx.load('fabric', tooldir='waf_tools')

    ctx.recurse(SUBDIRS)

def configure(ctx):
    ctx.load('tex')
    latex_engine_path = ctx.find_program(ctx.options.latex_engine)

    # Override TeX program. Keep in mind that this overrides PDFLATEX for
    # everything using it, that is, the poster and the manual. That's OK,
    # though.
    ctx.env.PDFLATEX = latex_engine_path

    # makeinfo on Mac OS X is notoriously old. Try to find a newer one
    # installed with Homebrew if possible.
    try:
        texinfo_brew_prefix = ctx.cmd_and_log([
            'brew', '--prefix', 'texinfo']).rstrip()
    except waflib.Errors.WafError:
        pass
    else:
        possible_makeinfo_path = join(texinfo_brew_prefix, 'bin', 'makeinfo')
        if os.path.isfile(possible_makeinfo_path):
            os.environ['MAKEINFO'] = possible_makeinfo_path

    # If there are problems with sphinx_internal not triggering builds
    # correctly, switch to sphinx_external which always rebuilds. IMPORTANT:
    # This will change the output file paths, so that will have to be changed
    # too...
    ctx.load('sphinx_internal', tooldir='waf_tools')

    # Deployment programs
    ctx.find_program('ghp-import', var='GHP_IMPORT')
    ctx.load('fabric', tooldir='waf_tools')

    ctx.recurse(SUBDIRS)

def build(ctx):
    ctx.recurse(SUBDIRS)

# Archive context and command

def _copy_file(tsk):
    shutil.copyfile(tsk.inputs[0].abspath(), tsk.outputs[0].abspath())

class ArchiveContext(waflib.Build.BuildContext):
    cmd = 'archive'
    fun = 'archive'

def archive(ctx):
    # Prepare website directory
    html_build_dir = ctx.path.find_or_declare(['manual', 'html'])
    html_build_nodes = html_build_dir.ant_glob(
        '**',
        excl=['Makefile', '.doctrees', '.buildinfo'],
        quiet=True, # don't warn in verbose mode
    )

    website_dir = ctx.path.find_or_declare('website')
    website_dir.mkdir()

    # Copy HTML assets.
    for node in html_build_nodes:
        ctx(rule=_copy_file,
            source=node,
            target=website_dir.find_or_declare(node.path_from(html_build_dir)))

    # Copy PDF and EPUB.
    ctx(rule=_copy_file,
        source=ctx.bldnode.find_node([
            'manual', 'latexpdf', 'mastering-eos.pdf']),
        target=website_dir.find_or_declare('mastering-eos.pdf'))
    ctx(rule=_copy_file,
        source=ctx.bldnode.find_node([
            'manual', 'epub', 'mastering-eos.epub']),
        target=website_dir.find_or_declare('mastering-eos.epub'))

    # Copy poster.
    ctx(rule=_copy_file,
        source=ctx.bldnode.find_node(['poster', 'mastering-eos.pdf']),
        target=website_dir.find_or_declare('mastering-eos-poster.pdf'))

    # Prepare archives
    ctx.load('archive', tooldir='waf_tools')

    archive_basename = 'mastering-eos-html'
    html_sources = [
        (node, join(archive_basename, node.path_from(html_build_dir)))
        for node in html_build_nodes
    ]
    ctx(features='archive',
        formats='gztar zip',
        source=html_sources,
        target=join('website', archive_basename))

# Deploy context and command

@always_run
class ghp_import_task(waflib.Task.Task):
    vars = ['GHP_IMPORT']

    def __init__(self, dir_node, *args, **kwargs):
        super(ghp_import_task, self).__init__(*args, **kwargs)
        self._dir_node = dir_node

    def run(self):
        return self.exec_command([
            self.env.GHP_IMPORT,
            '-n', # Include a .nojekyll file in the branch
            '-p', # Push the branch after import
            self._dir_node.abspath(),
        ])

class DeployContext(waflib.Build.BuildContext):
    cmd = 'deploy'
    fun = 'deploy'

def deploy(ctx):
    # Deploy man and info docs
    ctx(features='fabric',
        fabfile=ctx.path.find_resource('fabfile.py'),
        command='deploy_man_info',
        args=dict(
            manpage=ctx.bldnode.find_node([
                'manual', 'man', 'eos.7']).abspath(),
            infodoc=ctx.bldnode.find_node([
                'manual', 'info', 'eos.info']).abspath(),
        ),
        always=True,
    )

    # Deploy GitHub pages
    website_node = ctx.bldnode.find_dir('website')
    ghp_task = ghp_import_task(website_node, env=ctx.env)
    ctx.add_to_group(ghp_task)
