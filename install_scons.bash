#!/usr/bin/env bash

set -o errexit
set -o nounset

# Install SCons into the current environment.
readonly SCONS_WITH_VERSION='scons-2.3.0'
wget "http://prdownloads.sourceforge.net/scons/$SCONS_WITH_VERSION.tar.gz" --output-document - | tar -xz
pushd $SCONS_WITH_VERSION
python setup.py install
popd # $SCONS_WITH_VERSION
rm -r "$SCONS_WITH_VERSION"
