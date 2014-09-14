# -*- mode: python; coding: utf-8; -*-

# Waf build file
#
# Keep this file and all Waf files Python 2/3 single-source compatible (using
# six when necessary).

import os
from os.path import join

import waflib

# Waf constants
APPNAME = 'mastering-eos'
VERSION = '0.1'
top = '.'
out = 'build'

SUBDIRS = ['manual', 'poster']

def options(ctx):
    ctx.recurse(SUBDIRS)

def configure(ctx):
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
    # correctly, switch to sphinx_external which always rebuilds.
    ctx.load('sphinx_internal', tooldir='waf_tools')

    ctx.recurse(SUBDIRS)

def build(ctx):
    ctx.recurse(SUBDIRS)
