# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from __future__ import unicode_literals
import subprocess

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    # 'rst2pdf.pdfbuilder',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Mastering EOS'
unix_name = 'mastering-eos'
authors = ['Sean Fisk', 'Ira Woodring']
authors_str = ' and '.join(authors)
from datetime import date
copyright = '{year} {authors_str}'.format(
    year=date.today().year, authors_str=authors_str)
# Name of the man page and info docs.
man_info_name = 'eos'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    'TODO.rst',
    '_build',
    '**/common',
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d %H:%M:%S %Z'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = unix_name


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', unix_name + '.tex', project, authors_str, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = False


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', man_info_name, project, authors, 7),
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', man_info_name, project, authors_str, project,
     'EOS Lab Documentation', 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
texinfo_domain_indices = False

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = authors_str
epub_publisher = authors_str
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
epub_basename = unix_name

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
# epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
# epub_fix_images = False

# Scale large images.
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# epub_show_urls = 'inline'

# If false, no index is generated.
# epub_use_index = True

# -- Options for PDF output --------------------------------------------------

# To use ReportLab PDF output with rst2pdf, see this link:
# <http://rst2pdf.ralsina.com.ar/handbook.html#sphinx>

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.

pdf_documents = [
    ('index', unix_name, project, authors_str),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx', 'kerning', 'a4']

# A list of folders to search for stylesheets. Example:
pdf_style_path = ['.', '_styles']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
# pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
# pdf_language = "en_US"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
# pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
# pdf_break_level = 0

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
# pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
# pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
# pdf_verbosity = 0

# If false, no index is generated.
# pdf_use_index = True

# If false, no modindex is generated.
pdf_use_modindex = False

# If false, no coverpage is generated.
# pdf_use_coverpage = True

# Name of the cover page template to use
# pdf_cover_template = 'sphinxcover.tmpl'

# Documents to append as an appendix to all manuals.
# pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = False

# Set the default DPI for images
# pdf_default_dpi = 72

# Enable rst2pdf extension modules (default is only vectorpdf)
# you need vectorpdf if you want to use sphinx's graphviz support
# pdf_extensions = ['vectorpdf']

# Page template name for "regular" pages
# pdf_page_template = 'cutePage'

# Show Table Of Contents at the beginning?
# pdf_use_toc = True

# How many levels deep should the table of contents be?
pdf_toc_depth = 9999

# Add section number to section references
pdf_use_numbered_links = False

# Background images fitting mode
pdf_fit_background_mode = 'scale'

# -- Custom Options -------------------------------------------------------

_github_url = 'https://github.com/seanfisk/mastering-eos'

# Global substitutions and links, using rst_epilog.
# Apparently we can't use the `text <link>`_ notation in here, so see
# <http://docutils.sourceforge.net/FAQ.html#is-nested-inline-markup-possible>.
rst_epilog = '''
.. |title| replace:: {title}
.. |bold-title| replace:: **{title}**
.. |the-sysadmin| replace:: Ira Woodring
.. _the-sysadmin: mailto:woodriir@gvsu.edu

.. _Mastering EOS GitHub repository: {url}
.. _The Linux Documentation Project article on Shared Libraries: http://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html
.. _Russ Allbery's notes on Shared Library Search Paths: http://www.eyrie.org/~eagle/notes/rpath.html
.. _Autoconf manual on Preset Output Variables: http://www.gnu.org/software/autoconf/manual/autoconf.html#Preset-Output-Variables
.. _Wikipedia entry on rpath:
.. _rpath:
.. _run-time search path (rpath): http://en.wikipedia.org/wiki/Rpath
.. _Waf: https://code.google.com/p/waf/
.. _CMake: http://www.cmake.org/
.. _Autotools: http://en.wikipedia.org/wiki/GNU_build_system
.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _report an issue:
.. _issue tracker: {url}/issues
.. _ExpanDrive: http://www.expandrive.com/expandrive
'''.format(title=project, url=_github_url)

# The default highlight language is Python; switch it to Bash.
highlight_language = 'bash'

# Shortcut for Wikipedia articles, see http://sphinx-doc.org/ext/extlinks.html
extlinks = dict(
    wikipedia=('http://en.wikipedia.org/wiki/%s', ''),
)

# Git revision: custom option, for use in '_templates/footer.html'.
_git_short_revision = subprocess.check_output([
    'git', 'rev-parse', '--short', 'HEAD']).decode('ascii').rstrip()
# Inject the 'git_revision' keyword into the Jinja template.
html_context = dict(
    git_revision=(
        '<a href="{github_url}/commit/{rev}">'
        '{rev}</a>'.format(github_url=_github_url, rev=_git_short_revision)
    )
)
