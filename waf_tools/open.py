# -*- coding: utf-8 -*-

"""Open various filetypes."""

import sys
import platform
import webbrowser

from waflib.Configure import conf

SYSTEM = platform.system()

OPEN_PROG = {
    'Linux': 'xdg-open',
    'Darwin': 'open',
}

def configure(ctx):
    try:
        ctx.find_program(OPEN_PROG[SYSTEM], var='OPEN', mandatory=False)
    except KeyError:
        pass
    ctx.find_program('man', mandatory=False)
    ctx.find_program('info', mandatory=False)

@conf
def open_file(self, node):
    """Open a node in operating system's associated program."""
    path = node.abspath()
    if self.env.OPEN:
        self.exec_command(self.env.OPEN + [path])
    elif SYSTEM == 'Windows':
        os.startfile(path)
    else:
        try:
            msg = "'{}' not found".format(OPEN_PROG[SYSTEM])
        except KeyError:
            msg = 'platform unsupported'
        self.fatal('Opening file failed, ' + msg)

@conf
def open_html_file(self, node):
    """Open an HTML in a web browser. Although :func:`open_file` will generally
    work for this as well, this function uses the :mod:`webbrowser` module.
    """
    webbrowser.open('file://' + node.abspath())

def _open_man_info(ctx, prog, format, node):
    exe = ctx.env[prog.upper()]
    if exe:
        ctx.exec_command(
            exe + [node.abspath()],
            # Don't capture the standard streams so that the program can run
            # successfully.
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
    else:
        ctx.fatal("Opening {} failed, '{}' not found".format(format, prog))

@conf
def open_manpage(self, node):
    _open_man_info(self, 'man', 'manpage', node)

@conf
def open_info(self, node):
    _open_man_info(self, 'info', 'info document', node)
