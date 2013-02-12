# -*- mode: python -*-
# SCons build file

import os

env = Environment()

# Use LuaTeX instead of pdfTeX.
env.Replace(PDFLATEX='lualatex')

# Use Biber instead of BiBTeX.
env.Replace(BIBTEX='biber')

# Enable SyncTeX. This is personal, but I use it, and I would
# recommend it to everybody.
env.AppendUnique(PDFLATEXFLAGS='-synctex=1')

# Shell escape. Needed by minted and dot2tex to name a few.
# env.AppendUnique(PDFLATEXFLAGS='-shell-escape')

# Look in standard directory ~/texmf for .sty files.
env.SetDefault(TEXMFHOME=os.path.join(os.environ['HOME'], 'texmf'))

pdf = env.PDF('document.tex')
Default(pdf)
