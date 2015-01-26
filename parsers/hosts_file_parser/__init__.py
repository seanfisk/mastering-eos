#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""/etc/hosts file parser"""

import re
from collections import namedtuple

from hosts_file_parser.parser import HostsParser # pylint: disable=import-error,no-name-in-module

Record = namedtuple('Record', ['ip', 'hostname', 'aliases'])

EOS_HOSTNAME_RE = re.compile(
    r'(?:eos|arch|dc)\d+\.cis\.gvsu\.edu$')

class Semantics(object):
    """Transformations for AST nodes."""
    def record(self, ast): # pylint: disable=no-self-use
        """Handle a record node."""
        try:
            aliases = ast['aliases']
        except KeyError:
            aliases = []
        return Record(ast['ip'], ast['hostname'], aliases)

def get_eos_hostnames(hosts_file):
    """Extract EOS hostnames (EOS, Arch, and Datacomm) from an EOS
    ``/etc/hosts`` file.

    :param hosts_file: a file object representing the hosts file
    :type hosts_file: :class:`file`
    :return: list of EOS hostnames
    :rtype: :class:`list` of :class:`unicode`
    """
    hosts_parser = HostsParser(
        # Don't include newline in the whitespace because records end with a
        # newline.
        whitespace=' \t',
        # Because we didn't include newline in the whitespace characters, it
        # needs to be in here.
        eol_comments_re='#.*\n',
        semantics=Semantics(),
    )
    with hosts_file:
        try:
            kwargs = dict(filename=hosts_file.name)
        except AttributeError:
            kwargs = {}
        records = hosts_parser.parse(
            hosts_file.read(), rule_name='file', **kwargs)

    return [record.hostname for record in records if
            EOS_HOSTNAME_RE.match(record.hostname)]
