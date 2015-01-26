# -*- coding: utf-8; -*-

"""Extra context methods"""

from waflib.Configure import conf

# Placed in here so that they don't interfere with the Waf help screen.

@conf
def should_build(self, fmt):
    """Indicate whether the specified format should build."""
    # If we don't have a specific target, always build. If we have a specific
    # target, build if that target matches the provided target.
    spec_format = self.env.SPECIFIC_TARGET.format
    return not spec_format or spec_format == fmt

@conf
def find_or_make(self, parent, lst): # pylint: disable=unused-argument
    """Find or make a node. This looks for the node specified, and creates it
    if it doesn't exist. The notable difference from
    :meth:`waflib.Node.find_resource` and :meth:`waflib.Node.find_or_declare`
    is that this doesn't look in the other of the source/build directory.
    """
    return parent.find_node(lst) or parent.make_node(lst)

@conf
def find_or_make_in_src(self, lst):
    """Find or make a node in the source directory. It's like
    :meth:`waflib.Node.find_or_declare()`, but for the source directory only.
    """
    # Since we are creating a file in the source directory, we can't use a
    # built-in Waf method. Please see here for a "solution":
    # <https://code.google.com/p/waf/issues/detail?id=1168>
    # That issue deals with exactly our problem here.
    return self.find_or_make(self.srcnode, lst)
