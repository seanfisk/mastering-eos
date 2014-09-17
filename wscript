# -*- mode: python; coding: utf-8; -*-

# Waf build file
#
# Keep this file and all Waf files Python 2/3 single-source compatible (using
# six when necessary).

import os
from os.path import join
import textwrap

import waflib

# Waf constants
APPNAME = 'mastering-eos'
VERSION = '0.1'
top = '.'
out = 'build'

# Process the poster first, as it takes more time to generate but has less
# dependencies.
SUBDIRS = ['poster', 'manual']

def options(ctx):
    latex_engines = ['lualatex', 'xelatex']
    default_latex_engine = latex_engines[0]
    ctx.add_option(
        '-l', '--latex-engine',
        choices=latex_engines, default=default_latex_engine,
        help=("set LaTeX engine; valid values {0}; "
              "default is '{1}'").format(
                  ', '.join("'{0}'".format(e) for e in latex_engines),
                  default_latex_engine))

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

    ctx.recurse(SUBDIRS)

def build(ctx):
    ctx.recurse(SUBDIRS)
