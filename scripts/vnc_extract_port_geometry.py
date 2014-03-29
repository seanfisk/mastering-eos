#!/usr/bin/python

# This is a quick-and-dirty script to extract ports and matching geometries
# from our VNC server configurations.

# Using a hard-coded Python is purposeful -- this should work no matter what
# environment variables or anything are configured. The current system Python
# version at this time of writing is 2.6.6.

# This script is based on a bunch of different assumptions and doesn't do a lot
# of error checking, but it seems to work well in practice.

from __future__ import print_function
import sys
import os


class ConfigurationFormatError(Exception):
    def __init__(self, conf_file_path, message):
        self._conf_file_path = conf_file_path
        self._message = message

    def __str__(self):
        return '{0}: {1}'.format(self._conf_file_path, self._message)


def main(argv):
    etc_dir = '/etc/xinetd.d'
    port_geom_list = []
    for basename in os.listdir(etc_dir):
        if not basename.startswith('vnc'):
            continue
        conf_file_path = os.path.join(etc_dir, basename)
        with open(conf_file_path) as conf_file:
            port = None
            geometry = None
            for line in conf_file:
                if 'port' in line:
                    try:
                        port = line.split('=')[1].strip()
                    except IndexError:
                        raise ConfigurationFormatError(
                            conf_file_path,
                            "Unexpected format of 'port' line")
                if 'server_args' in line:
                    split = line.split()
                    for i, token in enumerate(split):
                        if token == '-geometry':
                            break
                    try:
                        geometry = split[i + 1]
                    except IndexError:
                        raise ConfigurationFormatError(
                            conf_file_path,
                            "Unexpected format of 'server_args' line")
            if port is None:
                raise ConfigurationFormatError(
                    conf_file_path, "Missing 'port' line")
            if geometry is None:
                raise ConfigurationFormatError(
                    conf_file_path, "Missing 'server_args' line")
            port_geom_list.append((port, geometry))
    for port, geometry in sorted(port_geom_list):
        print(port, geometry)
    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
