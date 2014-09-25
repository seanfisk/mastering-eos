# -*- coding: utf-8; -*-

"""Waf tool for creating various types of archives.

Q: How is this different from the 'waf dist' command?
A: This tool allows you to create arbitrary archives, not just archives of the
   project. Much of the code is based on the code from the 'waf dist' command,
   however.

Q: How is this different from shutil.make_archive()?
A: This tool allows setting of the archive name of files in the archive. In
   addition, it sets the owner and group to 'root' in the tar files.
"""

import os
from abc import ABCMeta, abstractmethod
import tarfile
import zipfile

import six
import waflib
from waflib.Configure import conf

TAR_FORMAT_COMPRESSION_MAPPING = {
    'tar': None,
    'gztar': 'gz',
    'bztar': 'bz2',
}

source_element_error = waflib.Errors.WafError(
    'Archive source element must be in the form (node, archive_name)')

class make_archive_task(waflib.Task.Task):
    def run(self):
        out_path = self.outputs[0].abspath()
        archive = (ZipArchive(out_path) if self.format == 'zip'
                   else TarArchive(out_path, self.compression))
        try:
            for in_node in self.inputs:
                archive.add_file(
                    in_node.abspath(),
                    self.in_node_archive_name_mapping[in_node])
        finally:
            archive.close()

@waflib.TaskGen.feature('archive')
@waflib.TaskGen.before_method('process_source')
def apply_archive(task_gen):
    """Create various types of archives.

    This method overrides the processing by
    :py:meth:`waflib.TaskGen.process_source`.
    """
    # Initialize the keywords.
    try:
        formats = waflib.Utils.to_list(task_gen.formats)
    except AttributeError:
        raise waflib.Errors.WafError(
            'Archive task generator missing necessary keyword: formats')

    # Check for dupes.
    if len(formats) != len(set(formats)):
        raise waflib.Errors.WafError(
            "Archive 'format' keyword cannot contain duplicates.")

    source = getattr(task_gen, 'source', [])

    in_nodes = []
    in_node_archive_name_mapping = {}
    for source_tuple in source:
        # If source is a tuple, it should be a tuple of (node, archive_name)
        # where archive name is the file's name in the archive.
        if not isinstance(source_tuple, tuple):
            raise source_element_error
        try:
            node, archive_name = source_tuple
        except ValueError:
            raise source_element_error

        in_nodes.append(node)
        in_node_archive_name_mapping[node] = archive_name

    try:
        outs = waflib.Utils.to_list(task_gen.target)
    except AttributeError:
        raise waflib.Errors.WafError(
            'Archive task generator missing necessary keyword: target')
    if len(outs) != 1:
        raise waflib.Errors.WafError(
            'If specified, archive task generator '
            'can only take one output.'
        )
    out_base = outs[0]

    for format in formats:
        if format == 'zip':
            extension = '.zip'
            compression = None # Not used for zip
        else:
            try:
                compression = TAR_FORMAT_COMPRESSION_MAPPING[format]
            except KeyError:
                raise waflib.Errors.WafError(
                    'Archive format not recognized: {0}'.format(self.format))
            extension = '.tar' + ('.' + compression if compression else '')

        out_node = task_gen.path.find_or_declare(out_base + extension)

        task = task_gen.create_task('make_archive', src=in_nodes, tgt=out_node)
        # Assign attributes necessary for task methods.
        task.format = format
        task.compression = compression
        task.in_node_archive_name_mapping = in_node_archive_name_mapping

        # Set the task order if that was requested.
        for attr in ['after', 'before']:
            setattr(task, attr, getattr(task_gen, attr, []))

    # Prevent execution of process_source. We don't want this to run because we
    # have our own format for the source list.
    # Following the lead of code in waflib:
    task_gen.source = []
    # Also possible.
    # task_gen.meths.remove('process_source')

class Archive(six.with_metaclass(ABCMeta, object)):
    @abstractmethod
    def add_file(self, node, archive_name):
        raise NotImplementedError()

    def close(self):
        pass

class TarArchive(Archive):
    def __init__(self, path, compression):
        mode = 'w' + (':' + compression if compression else '')
        self._archive = tarfile.open(path, mode=mode)

    def add_file(self, file_path, archive_name):
        # TODO: Make archive_name optional as in 'waf dist'.
        tarinfo = self._archive.gettarinfo(
            name=file_path, arcname=archive_name)
        tarinfo.uid = 0
        tarinfo.gid = 0
        tarinfo.uname = 'root'
        tarinfo.gname = 'root'

        fileobj = None
        try:
            fileobj = open(file_path, 'rb')
            self._archive.addfile(tarinfo, fileobj=fileobj)
        finally:
            if fileobj:
                fileobj.close()

    def close(self):
        self._archive.close()

class ZipArchive(Archive):
    def __init__(self, path):
        self._archive = zipfile.ZipFile(path, mode='w')

    def add_file(self, file_path, archive_name):
        # TODO: Make archive_name optional as in 'waf dist'.
        self._archive.write(file_path, arcname=archive_name)

    def close(self):
        self._archive.close()
