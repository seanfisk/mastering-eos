# -*- coding: utf-8 -*-

"""Open various filetypes."""

import os
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
    ctx.find_program('emacsclient', mandatory=False)

@conf
def open_file(self, node):
    """Open a node in operating system's associated program."""
    path = node.abspath()
    if self.env.OPEN:
        self.exec_command(
            self.env.OPEN + [path],
            # Don't buffer the program's output. On GNU/Linux, buffering
            # xdg-open's output causes it to block the Waf process.
            stdout=None, stderr=None)
    elif SYSTEM == 'Windows':
        os.startfile(path) # pylint: disable=no-member
    else:
        try:
            msg = "'{}' not found".format(OPEN_PROG[SYSTEM])
        except KeyError:
            msg = 'platform unsupported'
        self.fatal('Opening file failed, ' + msg)

@conf
def open_html_file(self, node): # pylint: disable=unused-argument
    """Open an HTML node in a web browser. Although :func:`open_file` will
    generally work for this as well, this function uses the :mod:`webbrowser`
    module.
    """
    webbrowser.open('file://' + node.abspath())

@conf
def open_manpage(self, node):
    """Open a manual page."""
    _open_man_info(self, 'man', 'manpage', node)

@conf
def open_info(self, node):
    """Open a set of info documentation."""
    _open_man_info(self, 'info', 'info document', node)

@conf
def open_info_emacs(self, node):
    """Open an info node in Emacs."""
    emacsclient = self.env.EMACSCLIENT
    if emacsclient:
        # We attempt to make this to work as best as it can with differing
        # setups.
        self.exec_command(
            emacsclient + [
                # Start Emacs in daemon mode if we can't connect.
                '--alternate-editor=',
                # If we choose not to create a new frame and the Emacs server
                # isn't started, the command will start Emacs in daemon mode
                # and not create a frame. We don't want this. If the Emacs
                # server is started, this command will still create a new frame
                # in this terminal, which may or may not be the desired
                # behavior. It's a bit of a compromise, but we've put the
                # highest priority on *something* working most of the time.
                '--create-frame',
                # Open an info bufffer. The escaping is somewhat sketchy.
                '--eval', '(info "{}")'.format(
                    node.abspath().replace('"', r'\"')),
            ],
            # Avoid capturing the standard streams so that the program can run
            # successfully.
            stdout=None,
            stderr=None,
        )
    else:
        _tool_not_found(self, 'info document', 'emacsclient')

def _tool_not_found(ctx, prog, fmt):
    ctx.fatal("Opening {} failed, '{}' not found".format(fmt, prog))

def _open_man_info(ctx, prog, fmt, node):
    exe = ctx.env[prog.upper()]
    if exe:
        ctx.exec_command(
            exe + [node.abspath()],
            # Avoid capturing the standard streams so that the program can run
            # successfully.
            stdout=None,
            stderr=None,
        )
    else:
        _tool_not_found(ctx, prog, fmt)
