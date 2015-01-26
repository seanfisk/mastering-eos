# -*- coding: utf-8 -*-

"""Git helpers"""

import waflib
from waflib.Configure import conf

def _run_git_ls_files(ctx, args):
    """Run ``git ls-files`` with the specified arguments.

    :return: set of file names
    :rtype: :class:`set`
    """
    return set(ctx.cmd_and_log(
        ['git', 'ls-files'] + args, quiet=waflib.Context.STDOUT).splitlines())

@conf
def get_git_files(self, dir_='.'):
    """Retrieve a list of all Git non-ignored files, including untracked
    files, excluding deleted files, within a specific directory.

    :param dir: directory to list, default is current directory
    :return: sorted list of git project files
    :rtype: :class:`list`
    """
    cached_and_untracked_files = _run_git_ls_files(self, [
        '--cached',  # All files cached in the index
        '--others',  # Untracked files
        # Exclude untracked files that would be excluded by .gitignore,
        # etc.
        '--exclude-standard',
        dir_,
    ])
    uncommitted_deleted_files = _run_git_ls_files(self, ['--deleted', dir_])

    # Since sorting of files in a set is arbitrary, return a sorted list to
    # provide a well-defined order to other tools.
    return sorted(cached_and_untracked_files - uncommitted_deleted_files)

@conf
def get_git_nodes(self, dir_='.'):
    """Return a list of Git files in a specific directory as Waf nodes.

    :param ctx: Waf context
    :type ctx: waflib.Context.Context
    :param dir: directory to list, default is current directory
    :rtype: :class:`list`
    """
    # find_resource basically does the same thing as find_node, but checks
    # in the build directory first. We know these files aren't in the build
    # directory, so just use find_node.
    return map(self.path.find_node, self.get_git_files(dir_))
