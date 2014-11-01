# -*- coding: utf-8 -*-

"""Generate a table of VNC ports and geometries by parsing the ``vncts``
file.
"""

import re
import argparse
from collections import OrderedDict

import six
from texttable import Texttable
from grako.exceptions import FailedSemantics

from vnc_table_generator.parser import VnctsParser

# The front part is just so that things like 'not-really-geometry' don't match.
# The end part is so that things like '1440x900abcd' don't match.
SERVER_ARGS_RE = re.compile(r'(?:^|\s)-geometry\s+(\d+x\d+)(?:$|\s)')
"""Regex used to parse server_args."""

def _dict_list_to_ordered_dict(d_list):
    """Convert a list of dictionaries::

        [{'key': 1, 'value': 'abcd'}, {'key': 'butter', 'value': 'knife'}]

    to an ordered dictionary::

        OrderedDict([(1, 'abcd'), ('butter', 'knife')])

    :param d_list: list of dictionaries
    :type d_list: :class:`list` of :class:`dict`
    :returns: the ordered dictionary
    :rtype: :class:`collections.OrderedDict`
    :raises: :exc:`grako.exceptions.FailedSemantics` when dictionary does not
        have ``key`` or ``value`` keys or when duplicate ``key`` values arise
    """
    out = OrderedDict()
    for d in d_list:
        try:
            key = d['key']
            value = d['value']
        except KeyError as e:
            missing_key = e.args[0]
            # TODO: Grako has a bug that causes FailedSemantics exceptions
            # raised within a repeater to not be reported correctly. It will
            # need to be fixed in Grako itself.
            raise FailedSemantics(
                "Dictionary has no {0!r} key: {1!r}".format(missing_key, d))

        if key in out:
            # TODO: Ditto from above
            raise FailedSemantics(
                'Duplicate key {0!r} from previous dictionary found: {1!r}'
                .format(key, d))

        out[key] = value

    return out

class Semantics(object):
    def file(self, ast):
        return _dict_list_to_ordered_dict(ast)

    def service(self, ast):
        return {
            'key': ast['key'],
            'value': _dict_list_to_ordered_dict(ast['value']),
        }

def generate_vnc_table(input_file, output_file):
    """Generate a table of VNC display, port, and resolution from an input
    ``vncts`` file.

    :param input_file: the ``vncts`` file object
    :type input_file: :class:`file`
    :param output_file: the output table file object
    :type output_file: :class:`file`
    """
    # Parse the config file.
    vncts_parser = VnctsParser(
        eol_comments_re='#.*$',
        semantics=Semantics(),
    )
    try:
        kwargs = dict(filename=input_file.name)
    except AttributeError:
        kwargs = {}
    with input_file:
        result = vncts_parser.parse(
            input_file.read(), rule_name='file', **kwargs)

    table = Texttable()
    # The default decoration produces the correct table.
    table.header(['Display', 'Port', 'Geometry'])

    for display, (name, properties) in enumerate(six.iteritems(result)):
        try:
            server_args = properties['server_args']
        except KeyError:
            raise ValueError(
                "Service '{0}' does not have a 'server_args' property!".format(
                    name))

        match = SERVER_ARGS_RE.search(server_args)
        if not match:
            raise ValueError(
                ("Service '{0}' does not contain a recognized "
                 "'-geometry WIDTHxHEIGHT' option!").format(name))

        geometry = match.group(1)
        port = 5900 + display
        table.add_row([display, port, geometry])

    with output_file:
        output_file.write(table.draw())
