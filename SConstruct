# -*- mode: python -*-
# SCons build file

import os


# If using dot2tex, uncomment the following.
#
# LaTeX will not error out if dot2tex is not found, but without it, we can't
# generate our Graphviz graphs. Don't let execution continue if it isn't found.
# from distutils.spawn import find_executable
# if find_executable('dot2tex') is None:
#     raise SystemExit("SConstruct: program not found: dot2tex")


# Use this to inherit the PATH environmental variable if necessary.
#
# This will be necessary, e.g., for finding pygmentize for minted installed in
# the Python user directory (e.g., ~/.local).
env = Environment(ENV={'PATH': os.environ['PATH']})

# Use LuaTeX instead of pdfTeX.
env.Replace(PDFLATEX='lualatex')

# Use Biber instead of BiBTeX.
env.Replace(BIBTEX='biber')

# Enable SyncTeX. This is personal, but I use it, and I would
# recommend it to everybody.
env.AppendUnique(PDFLATEXFLAGS='-synctex=1')

# Shell escape. Needed by minted and dot2tex to name a few.
env.AppendUnique(PDFLATEXFLAGS='-shell-escape')

# Look in standard directory ~/texmf for .sty files.
env.SetDefault(TEXMFHOME=os.path.join(os.environ['HOME'], 'texmf'))

pdf = env.PDF('mastering-eos.tex')
env.Depends(pdf, 'beamerthemeEOS.sty')
env.Depends(pdf, env.Glob('scripts/*'))
env.Depends(pdf, env.Glob('images/*'))
env.Depends(pdf, Glob('blocks/*.tex'))
Default(pdf)
