#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

import six

from hosts_file_parser import get_eos_hostnames

def main(argv):
    # Parse args.
    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        description='Extract EOS hostnames from an EOS /etc/hosts file.')
    arg_parser.add_argument(
        'hosts_file', type=argparse.FileType('r'),
        help='/etc/hosts file')
    args = arg_parser.parse_args(argv[1:])

    six.print_(*get_eos_hostnames(args.hosts_file), sep='\n')

    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
