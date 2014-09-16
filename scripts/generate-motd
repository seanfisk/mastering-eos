#!/usr/bin/env python

from __future__ import print_function
import sys
import re

import colorama
from colorama import Fore, Back, Style
colorama.init()

ANSI_RE = colorama.ansitowin32.AnsiToWin32.ANSI_RE
WIDTH = 80

TEXT_ANSI = Fore.WHITE
HIGHLIGHT_ANSI = Fore.GREEN
LINES = [
    TEXT_ANSI + 'Access to this EOS Lab computer is permitted only to',
    "Grand Valley State University Computer and Information Systems",
    'faculty, students, and other authorized users.',
    '',
    TEXT_ANSI + 'EOS Lab documentation is available by visiting',
    HIGHLIGHT_ANSI + 'http://seanfisk.github.io/mastering-eos/',
    TEXT_ANSI + 'or by running',
    (TEXT_ANSI + '  -or-  ').join([
        TEXT_ANSI + '$ ' + HIGHLIGHT_ANSI + cmd for cmd in [
            'eos-web-docs', 'man eos', 'info eos']]),
    '',
    (TEXT_ANSI + 'Email ' + HIGHLIGHT_ANSI + 'woodriir@cis.gvsu.edu' +
     TEXT_ANSI + ' with questions.'),
    '',
]


def _center(line):
    """Center a line of text which possibly contains ANSI escape sequences."""
    line_no_ansi = ANSI_RE.sub('', line)

    if len(line_no_ansi) > WIDTH:
        raise ValueError('Given line must be less than or equal to max width, '
                         'not counting ANSI escape sequences.')

    # If the line doesn't have any visible characters, don't bother centering.
    # Just return the original line.
    if len(line_no_ansi) == 0:
        return line

    # Do the centering. There's really no reason to add spaces to the end of
    # the line, so just add spaces to the beginning with right justification.
    num_leading_spaces = (WIDTH - len(line_no_ansi)) // 2
    return line.rjust(len(line) + num_leading_spaces)


def main(argv):
    print('\n'.join(_center(line) for line in LINES) + Style.RESET_ALL)


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
