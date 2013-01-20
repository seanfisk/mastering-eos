This is my template project for LaTeX using SCons as a builder. Since
it is a personal template, it is quite opionated on certain tools,
such as:

* Use of [SCons][scons] for building the LaTeX document.
* Use of [LuaTeX][luatex] instead of [pdfTeX][pdftex].
* Use of [Biber][biber] instead of [BiBTeX][bibtex].
* Use of [Emacs][emacs] and [AUCTeX][auctex] for editing the document.

[scons]: http://scons.org/
[luatex]: http://www.luatex.org/
[pdftex]: http://www.tug.org/applications/pdftex/
[biber]: http://biblatex-biber.sourceforge.net/
[bibtex]: http://www.ctan.org/pkg/bibtex
[emacs]: http://www.gnu.org/software/emacs/
[auctex]: http://www.gnu.org/software/auctex/

To see how I use this template to build my PDFs from [Emacs][emacs], please take a look at the [TeX section of my Emacs configuration][sean-tex-emacs].

[sean-tex-emacs]: https://github.com/seanfisk/emacs/blob/sean/personal/personal-tex.el
