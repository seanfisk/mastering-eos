# -*- coding: utf-8 -*- pylint: disable=invalid-name

"""Sphinx configuration file"""

from __future__ import unicode_literals
import subprocess
from urlparse import urljoin
import locale
from datetime import date

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.extlinks']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Mastering EOS'
_slug = 'mastering-eos'
_authors = ['Sean Fisk', 'Ira Woodring']
_authors_str = ' and '.join(_authors)
copyright = '{0} {1}'.format( # pylint: disable=redefined-builtin
    date.today().year, _authors_str)
# Name of the man page and info docs.
_short_name = 'eos'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    '**/common',
]

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d %H:%M:%S %Z'

# Output file base name for HTML help builder.
htmlhelp_basename = _slug

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', _slug + '.tex', project, _authors_str, 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', _short_name, project, _authors, 7),
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', _short_name, project, _authors_str, project,
     'EOS Lab Documentation', 'Miscellaneous'),
]

# -- Custom Options -------------------------------------------------------

# Disable module indices for all our output types.
html_domain_indices = latex_domain_indices = texinfo_domain_indices = False

_github_url = 'https://github.com/seanfisk/mastering-eos'

# Global substitutions and links, using rst_epilog.
# Apparently we can't use the `text <link>`_ notation in here, so see
# <http://docutils.sourceforge.net/FAQ.html#is-nested-inline-markup-possible>.
# See here for the nbsp trick: http://stackoverflow.com/a/12145490
rst_epilog = '''
.. |title| replace:: {title}
.. |bold-title| replace:: **{title}**
.. |the-sysadmin| replace:: Ira Woodring
.. _the-sysadmin: mailto:woodriir@gvsu.edu
.. |nbsp| unicode:: 0xA0

.. Keep these in order

.. _report an issue:
.. _issue tracker: {url}/issues
.. _rpath:
.. _Wikipedia entry on rpath:
.. _run-time search path (rpath): http://en.wikipedia.org/wiki/Rpath
.. _pull requests:
.. _making a pull request: https://help.github.com/articles/using-pull-requests/
.. _Emacs:
.. _GNU Emacs: https://gnu.org/software/emacs/

.. Sort these

.. _Autoconf manual on Preset Output Variables: http://www.gnu.org/software/autoconf/manual/autoconf.html#Preset-Output-Variables
.. _Autotools: http://en.wikipedia.org/wiki/GNU_build_system
.. _CMake: http://www.cmake.org/
.. _EditorConfig: http://editorconfig.org/
.. _ExpanDrive: http://www.expandrive.com/expandrive
.. _GNOME: http://www.gnome.org/
.. _Git: http://git-scm.com/
.. _GitHub: https://github.com/
.. _Homebrew: http://brew.sh/
.. _KDE: https://www.kde.org/
.. _LXDE: http://lxde.org/
.. _Mastering EOS GitHub repository: {url}
.. _Python: http://python.org/
.. _Qt: http://qt-project.org/
.. _QtQuick/QML: http://qt-project.org/doc/qt-5/qmlapplications.html
.. _Ruby: https://www.ruby-lang.org/
.. _Russ Allbery's notes on Shared Library Search Paths: http://www.eyrie.org/~eagle/notes/rpath.html
.. _Sphinx: http://sphinx-doc.org/
.. _The Linux Documentation Project article on Shared Libraries: http://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html
.. _Waf: https://code.google.com/p/waf/
.. _X.Org: http://www.x.org/
.. _Xfce: http://xfce.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
'''.format(title=project, url=_github_url)

# The default highlight language is Python; switch it to Bash.
highlight_language = 'bash'

# Shortcut for various links, see http://sphinx-doc.org/ext/extlinks.html
_sphinx_base_url = 'http://sphinx-doc.org'
extlinks = {
    'wikipedia': ('http://en.wikipedia.org/wiki/%s', ''),
    'rest-primer': (urljoin(_sphinx_base_url, 'rest.html#%s'), ''),
    'sphinx-role': (
        urljoin(_sphinx_base_url, 'markup/inline.html#role-%s'), ''),
    'sphinx-directive': (
        urljoin(_sphinx_base_url, 'domains.html#directive-%s'), ''),
    'bash': ('http://www.gnu.org/software/bash/manual/bash.html#%s', ''),
    # This is the 2013-revised edition of POSIX.1-2008.
    'posix': ('http://pubs.opengroup.org/onlinepubs/9699919799/%s.html', ''),
}

# Git revision: custom option, for use in '_templates/footer.html'.
_git_short_revision = subprocess.check_output([
    'git', 'rev-parse', '--short', 'HEAD']).decode(
        locale.getpreferredencoding()).rstrip()
# Inject the 'git_revision' keyword into the Jinja template.
html_context = dict(
    git_revision=(
        '<a href="{github_url}/commit/{rev}">'
        '{rev}</a>'.format(github_url=_github_url, rev=_git_short_revision)
    )
)

# The :command: role defaults to displaying in bold. However, we think that
# literal text looks more appropriate, so we've created our own role, :cmd:,
# which displays them as such.
#
# Code adapated from the Sphinx source tree: 'sphinx/roles.py'
def _override_command_role():
    from docutils.parsers.rst import roles
    from docutils import nodes
    rolename = 'cmd'
    generic = roles.GenericRole(rolename, nodes.literal)
    role = roles.CustomRole(rolename, generic, {'classes': [rolename]})
    roles.register_local_role(rolename, role)
_override_command_role()

# Override table CSS, see:
# https://github.com/snide/sphinx_rtd_theme/issues/117#issuecomment-41571653
def setup(app):
    """Hook into Sphinx's application setup."""
    app.add_stylesheet('table-override.css')
