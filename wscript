# -*- mode: python; coding: utf-8; -*-

# Waf build file
#
# Keep this file and all Waf files Python 2/3 single-source compatible (using
# six when necessary).

import os
from os.path import join
import re
import textwrap
import shutil
from collections import OrderedDict
from tempfile import TemporaryFile

import six
import waflib
from waflib.Task import always_run

# Waf constants
APPNAME = 'mastering-eos'
VERSION = '0.1'
top = '.'
out = 'build'

# Process the poster first, as it takes more time to generate but has less
# dependencies.
SUBDIRS = ['parsers', 'poster', 'manual']
WAF_TOOLS_DIR = 'waf_tools'

def options(ctx):
    # This option tells our build system not to always run operations which use
    # SSH to access EOS. Currently, this includes building the VNC and SSH
    # fingerprints tables. Users building on their machines should probably
    # disable auto-update, while automated builds leave auto-updated enabled.
    # The default is to auto-update because it is safer.
    ctx.add_option(
        # -m for Manual update
        '-m', '--no-ssh-auto-update',
        default=False, action='store_true',
    help='disable auto-update of ops requiring SSH')

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
    ctx.load('sphinx_internal', tooldir=WAF_TOOLS_DIR)
    ctx.load('fabric_tool', tooldir=WAF_TOOLS_DIR)
    ctx.load('grako_tool', tooldir=WAF_TOOLS_DIR)

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

    # Grako
    ctx.load('grako_tool', tooldir=WAF_TOOLS_DIR)

    # If there are problems with sphinx_internal not triggering builds
    # correctly, switch to sphinx_external which always rebuilds. IMPORTANT:
    # This will change the output file paths, so that will have to be changed
    # too...
    ctx.load('sphinx_internal', tooldir=WAF_TOOLS_DIR)

    # Deployment programs
    ctx.find_program('ghp-import', var='GHP_IMPORT')
    ctx.load('fabric_tool', tooldir=WAF_TOOLS_DIR)

    # Add the vendor directory to the TeX search path so that our vendored
    # packages can be found.
    ctx.env.TEXINPUTS = ctx.path.find_dir('vendor').abspath()

    ctx.recurse(SUBDIRS)

    # Yay for double negatives!
    ctx.env.SSH_AUTO_UPDATE = not ctx.options.no_ssh_auto_update
    ctx.msg('Auto-update of SSH operations',
            'enabled' if ctx.env.SSH_AUTO_UPDATE else 'disabled',
            'GREEN' if ctx.env.SSH_AUTO_UPDATE else 'YELLOW')

def build(ctx):
    # Parsers (specifically the hosts parser) need to be build before anything
    # else.
    ctx.recurse('parsers')

    # Fetch the host file from EOS.
    fabfile_node = ctx.srcnode.find_resource('fabfile.py')
    hosts_node = ctx.path.find_or_declare('hosts')
    ctx(name='download_hosts_file',
        features='fabric',
        fabfile=fabfile_node,
        commands=dict(download_hosts_file=dict(output=hosts_node.abspath())),
        target=[hosts_node],
        **(dict(always=True) if ctx.env.SSH_AUTO_UPDATE else {})
    )

    parsers_dir = ctx.bldnode.find_dir('parsers')
    hostnames_node = ctx.path.find_or_declare('hostnames')
    # Build the list of hostnames.
    @ctx.rule(
        name='get_eos_hostnames',
        source=[hosts_node] + [
            # Depend on the generated parser files as well.
            parsers_dir.find_or_declare(['hosts_file_parser', base])
            for base in ctx.env.PARSER_FILES],
        target=hostnames_node,
        vars=['PYTHON'],
    )
    def get_eos_hostnames(tsk):
        with open(tsk.outputs[0].abspath(), 'w') as out_file:
            # Note: colorama (from grako) has issues if we try to directly call
            # into the Python module from here.
            tsk.exec_command(
                [
                ctx.env.PYTHON,
                    '-m', 'hosts_file_parser',
                    tsk.inputs[0].abspath(),
                ],
                stdout=out_file,
                # Add the module to the Python search path.
                env={'PYTHONPATH': parsers_dir.abspath()},
            )

    # Substitute max machine numbers into relevant files.
    in_nodes = map(ctx.path.find_resource, [
        ['common', 'inter-eos-ssh.bash.in'],
        ['manual', 'remote-access', 'index.rst.in'],
    ])
    # The generated files may or may not already exist. Since we are creating a
    # file in the source directory, it gets a little more complicated. Please
    # see here for the "solution":
    # <https://code.google.com/p/waf/issues/detail?id=1168>
    # That issue deals with exactly our problem here.
    def find_or_make(node):
        new_name = os.path.splitext(node.name)[0]
        return (node.parent.find_node(new_name) or
                node.parent.make_node(new_name))
    out_nodes = map(find_or_make, in_nodes)
    # Note: Can't use the 'fun' keyword for the 'subst' feature; it returns
    # after running.

    # TODO: We can't use the 'subst' feature because it requires us to provide
    # substitution values up-front, which is exactly what we can't do. That's
    # why we've used this replace(...) solution. There's got to be a better
    # way.
    @ctx.rule(
        name='subst_max_hostnames',
        source=[hostnames_node] + in_nodes,
        target=out_nodes,
        update_outputs=True)
    def subst_max_hostnames(tsk):
        hostnames_node = tsk.inputs[0]
        hostnames_content = hostnames_node.read()
        maxes = dict(('MAX_' + lab.upper(),
                      str(max(map(int, re.findall(
                          lab + r'(\d+)', hostnames_content)))))
                     for lab in ['eos', 'arch', 'dc'])
        for in_node, out_node in zip(tsk.inputs[1:], tsk.outputs):
            contents = in_node.read()
            for var, value in six.iteritems(maxes):
                contents = contents.replace('@{0}@'.format(var), value)
            out_node.write(contents)

    # Sphinx won't be able to detect that 'index.rst' hasn't been created yet,
    # so add a group to make sure it's been created.
    ctx.add_group()

    ctx.recurse(SUBDIRS[1:])

# Archive context and command

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
    ctx(features='subst',
        source=html_build_nodes,
        target=[website_dir.find_or_declare(node.path_from(html_build_dir))
                for node in html_build_nodes],
        is_copy=True)

    # Copy PDF.
    ctx(features='subst',
        source=ctx.bldnode.find_node([
            'manual', 'latexpdf', 'mastering-eos.pdf']),
        target=website_dir.find_or_declare('mastering-eos.pdf'),
        is_copy=True)

    # Copy poster.
    ctx(features='subst',
        source=ctx.bldnode.find_node(['poster', 'mastering-eos.pdf']),
        target=website_dir.find_or_declare('mastering-eos-poster.pdf'),
        is_copy=True)

    # Prepare archives
    ctx.load('archive', tooldir=WAF_TOOLS_DIR)

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
    hostnames_node = ctx.path.find_or_declare('hostnames')
    ctx(features='fabric',
        fabfile=ctx.path.find_resource('fabfile.py'),
        commands=OrderedDict([
            ('set_hosts', dict(hostfile=hostnames_node.abspath())),
            ('deploy_to_eos', {}),
        ]),
        args=dict(
            manpage=ctx.bldnode.find_node([
                'manual', 'man', 'eos.7']).abspath(),
            infodoc=ctx.bldnode.find_node([
                'manual', 'info', 'eos.info']).abspath(),
            webscript=ctx.path.find_resource([
                'scripts', 'eos-web-docs']).abspath(),
        ),
        source=[hostnames_node],
        always=True,
    )

    # Deploy GitHub pages
    website_node = ctx.bldnode.find_dir('website')
    ghp_task = ghp_import_task(website_node, env=ctx.env)
    ctx.add_to_group(ghp_task)
