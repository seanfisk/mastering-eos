# -*- mode: python -*-
# SCons build file

import os

# Inherit the current environment. Just makes a lot of things much easier.
env = Environment(ENV=os.environ)

# Use LuaTeX instead of pdfTeX.
env.Replace(PDFLATEX='lualatex')

# Shell escape. Needed by minted and dot2tex to name a few.
# env.AppendUnique(PDFLATEXFLAGS='-shell-escape')

# Look in standard directory ~/texmf for .sty files.
env.SetDefault(TEXMFHOME=os.path.join(os.environ['HOME'], 'texmf'))

pdf = env.PDF('document.tex')
Default(pdf)
