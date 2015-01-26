# -*- coding: utf-8 -*- pylint: disable=unused-argument
# The unused-argument is for 'self'.

"""Logging helpers"""

import waflib
from waflib.Configure import conf

@conf
def log_success(self, msg):
    """Log a message indicating success in green color.

    :param msg: the message to print
    :type msg: :class:`str`
    """
    waflib.Logs.pprint('GREEN', msg)

@conf
def log_failure(self, msg):
    """Log a message indicating failure in red color, then fail out.

    :param msg: the message to print
    :type msg: :class:`str`
    """
    self.fatal(msg)
