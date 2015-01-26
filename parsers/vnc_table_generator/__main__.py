#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from vnc_table_generator import generate_vnc_table

def main(argv):
    # Parse args.
    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        description='Generate a table of VNC ports and geometries from a '
        "provided 'vncts' file.")
    arg_parser.add_argument(
        'input_file', type=argparse.FileType('r'),
        help='input vncts file')
    arg_parser.add_argument(
        'output_file', type=argparse.FileType('w'),
        help='output file')
    args = arg_parser.parse_args(argv[1:])

    generate_vnc_table(args.input_file, args.output_file)

    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
