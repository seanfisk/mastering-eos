# -*- coding: utf-8 -*-

"""Pylint checker for Waf coding conventions"""

from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages

REQUIRED_FIRST_ARG = 'self'
"""Required name of the first argument of a Waf configure method."""

class WafChecker(BaseChecker):
    """Checks for Waf coding conventions."""
    __implements__ = IAstroidChecker

    name = 'waf'
    msgs = {
        'C9010': (
            "Waf configure method does not use '{}' as first argument"
            .format(REQUIRED_FIRST_ARG),
            'waf-conf-arg',
            "Used when first configure method argument is not '{}'".format(
                REQUIRED_FIRST_ARG),
        ),
    }

    @check_messages('waf-conf-arg')
    def visit_function(self, node):
        """Ensure the function has correct argument names."""
        # Without any decorators, the node's 'decorators' attribute will be
        # 'None'. Skip if there are no decorators or the function's first
        # argument is correct.
        if not node.decorators or node.args.args[0].name == REQUIRED_FIRST_ARG:
            return

        for decorator in node.decorators.nodes:
            for inferred in decorator.infer():
                # qname is "qualified name", and yields the full name of the
                # object. By using the qname, we avoid false positives like
                # other decorators called 'conf'.
                if inferred.qname() == 'waflib.Configure.conf':
                    self.add_message('waf-conf-arg', node=node)

def register(linter):
    """Method to auto-register our checkers."""
    linter.register_checker(WafChecker(linter))
