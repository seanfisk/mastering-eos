# -*- mode: python; coding: utf-8; -*-

# Waf build file
#
# Keep this file and all Waf files Python 2/3 single-source compatible (using
# six when necessary).

# Waf constants
APPNAME = 'mastering-eos'
VERSION = '0.1'
top = '.'
out = 'build'

SUBDIRS = ['poster'] # , 'manual'

def options(ctx):
    ctx.recurse(SUBDIRS)

def configure(ctx):
    ctx.recurse(SUBDIRS)

def build(ctx):
    ctx.recurse(SUBDIRS)
