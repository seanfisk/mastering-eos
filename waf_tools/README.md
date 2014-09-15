Sphinx Waf Tools
================

Using Sphinx from Waf is a little tricky. That's because Sphinx is not really a compiler -- it just produces a bunch of output files from a bunch of input files. In addition, some steps like the `info` and `latexpdf` builders have extra steps which require running `make` in the output directory.
