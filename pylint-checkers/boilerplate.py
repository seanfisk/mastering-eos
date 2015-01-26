# -*- coding: utf-8 -*-

"""Pylint module boilerplate checker."""

from pylint.interfaces import IRawChecker
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages

REQUIRED_CODING = 'coding: utf-8'
"""Required source encoding"""

class BoilerplateChecker(BaseChecker):
    """Checks for project-specific boilerplate."""
    __implements__ = IRawChecker

    name = 'boilerplate'
    msgs = {
        'C9001': (
            'Module is missing or has incorrect source code encoding',
            'source-encoding',
            'Used when source code encoding is missing or incorrect',
        ),
    }

    @check_messages('source-encoding')
    def process_module(self, module):
        """Ensure the module has the correct boilerplate."""
        add_msg = lambda l: self.add_message('source-encoding', line=l)
        stream = module.file_stream
        # TODO: When astroid gets updated, change to stop seeking.
        stream.seek(0) # Make sure we are at the beginning of the file
        # 'module.file_stream' is a 'io.BufferedReader', so any reads will be
        # in binary mode. We would like to wrap it with 'io.TextIOWrapper' read
        # it in text mode [this is basically what open(...) does]; however,
        # this apparently closes the file afterward which is a problem.
        #
        # Following the lead of EncodingChecker in 'checkers/misc.py' in the
        # pylint source tree, we default to ASCII. This is also specified under
        # 'Defining the Encoding' in PEP 263. Funny enough, this is the exact
        # problem this checker is designed to solve.
        encoding = module.file_encoding or 'ascii'
        readline = lambda: next(stream).decode(encoding)
        try:
            first_line = readline()
        except StopIteration:
            return # Empty file, always valid
        else:
            if REQUIRED_CODING not in first_line:
                try:
                    second_line = readline()
                except StopIteration:
                    # One-line file; did not contain required declaration
                    add_msg(1)
                else:
                    if first_line.lstrip().startswith('#!'):
                        # Multi-line file; has hash-bang; second line did not
                        # contain required declaration
                        if REQUIRED_CODING not in second_line:
                            add_msg(2)
                    else:
                        # Multi-line file; no hash-bang; first line did not
                        # contain required declaration
                        add_msg(1)

def register(linter):
    """Method to auto-register our checkers."""
    linter.register_checker(BoilerplateChecker(linter))
