from __future__ import print_function
from glob import glob
import subprocess
import os
import stat

from fabric.api import env, task, execute, run, runs_once, put
from texttable import Texttable

FINGERPRINTS_TABLE_FILENAME = 'remote_access/common/fingerprints/table.rst'
VNC_TABLE_FILENAME = 'remote_access/common/vnc_port_geometry_table.rst'

# Allow being overridden from the command-line.
if env.hosts == []:
    env.hosts += [
        'eos{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 25)]
    env.hosts += [
        'arch{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 11)]


@task
def get_fingerprint_for_machine():
    """Retrieve the SSH fingerprint for a specific machine."""
    output = run(
        'ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key.pub', shell=False)
    # The second element is the fingerprint.
    return output.split()[1]


@task
@runs_once
def generate_fingerprints_table():
    """Generate the fingerprints table for the manual."""
    results_dict = execute(get_fingerprint_for_machine)
    table = Texttable()
    # The default decoration produces the correct table.
    table.header(['Host', 'Fingerprint'])

    table.add_rows(
        sorted(
            # Use the short host name, and use a fixed-width for the
            # fingerprint itself.
            (host.split('.')[0], '``{0}``'.format(fingerprint))
            for (host, fingerprint)
            in results_dict.iteritems()),
        header=False)

    with open(FINGERPRINTS_TABLE_FILENAME, 'w') as fingerprint_file:
        print(table.draw(), file=fingerprint_file)


@task
@runs_once
def generate_vnc_table():
    """Generate the VNC port/geometry table for the manual."""
    script_name = 'vnc_extract_port_geometry.py'
    dest_path = '~/bin/' + script_name
    put('../scripts/' + script_name, dest_path, mode=stat.S_IRWXU)
    output = run(dest_path, shell=False)

    table = Texttable()
    # The default decoration produces the correct table.
    table.header(['Port', 'Geometry'])

    for line in output.splitlines():
        try:
            port, geometry = line.split()
        except IndexError:
            raise SystemExit('Invalid format returned by remote command')
        table.add_row([port, geometry])
    with open(VNC_TABLE_FILENAME, 'w') as vnc_table_file:
        print(table.draw(), file=vnc_table_file)


@task
@runs_once
def build():
    """Build the manual."""
    # Build the fingerprints and VNC tables if they do not exist. If it does
    # exist, we assume that it's accurate. Not the best assumption, so it's up
    # to the user to delete the generated table files or manually re-run the
    # generation task when it should be updated.
    if not os.path.exists(FINGERPRINTS_TABLE_FILENAME):
        execute(generate_fingerprints_table)

    if not os.path.exists(VNC_TABLE_FILENAME):
        execute(generate_vnc_table)

    # We choose not to use fabric's local() because it uses the shell. It's
    # better to avoid invoking the shell.

    # Must have epub first or we receive 'index can't be built errors'.

    # Sometimes Sphinx doesn't detect modifications to files even though they
    # are modified (e.g., includes). As a workaround, clean before building.
    # It's ugly, but it works.
    subprocess.check_call([
        'make', 'clean', 'epub', 'html', 'latexpdf', 'man', 'info'])


def rsync_to(extra_args):
    """Rsync the documentation with the specificed extra args.
    These should include the destination."""
    execute(build)
    subprocess.check_call([
        'rsync',
        '--verbose',
        '--archive',
        '--compress',
    ] + glob('_build/html/*') + [
        '_build/latex/MasteringEOS.pdf',
        '_build/epub/MasteringEOS.epub',
    ] + extra_args)


@task
@runs_once
def deploy_eos_web():
    ("Deploy the manual to the user's personal web directory in their EOS "
     'account.')
    rsync_to([
        '--chmod=go=rX',
        # Allow the user to override the username using fabric.
        env.user + '@eos10.cis.gvsu.edu:public_html/mastering-eos',
    ])


@task
@runs_once
def deploy_github_pages():
    """Deploy the manual to GitHub pages."""
    # Allow the user to override the username using fabric.
    rsync_to([
        # Be less careful about what we delete on GitHub pages.
        '--delete',
        'github_pages',
    ])


@task
@runs_once
def deploy_man_info_for_user():
    """Upload the man page and info docs to user's `~.local' directory."""
    execute(build)
    LOCAL_PREFIX = '.local/share'
    run('mkdir -p {0}/man/man7 {0}/info'.format(LOCAL_PREFIX), shell=False)
    put('_build/man/eos.7', LOCAL_PREFIX + '/man/man7/eos.7')
    put('_build/texinfo/eos.info', LOCAL_PREFIX + '/info/eos.info')


@task
def deploy_man_info_for_lab():
    ('Upload the man page and info docs to each EOS machine. Requires root '
     'access to said machines.')
    execute(build)
    # Untested, but this should work.
    env.user = 'root'
    GLOBAL_PREFIX = '/usr/local/share'
    run('mkdir -p {0}/man/man7 {0}/info'.format(GLOBAL_PREFIX), shell=False)
    put('_build/man/eos.7', GLOBAL_PREFIX + '/man/man7/eos.7')
    put('_build/texinfo/eos.info', GLOBAL_PREFIX + '/info/eos.info')
