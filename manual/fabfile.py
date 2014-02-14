from __future__ import print_function
from glob import glob
import subprocess
import os

from fabric.api import env, task, execute, run, runs_once, put
from texttable import Texttable

FINGERPRINTS_TABLE_FILENAME = 'ssh/common/fingerprints.rst'

# Allow being overridden from the command-line.
if env.hosts == []:
    env.hosts += [
        'eos{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 25)]
    env.hosts += [
        'arch{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 9)]


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

    table.add_rows(sorted(results_dict.iteritems()), header=False)

    with open(FINGERPRINTS_TABLE_FILENAME, 'w') as fingerprint_file:
        print(table.draw(), file=fingerprint_file)


@task
@runs_once
def build():
    """Build the manual."""
    # Build the fingerprints file if it does not exist. If it does exist, we
    # assume that it's accurate. Not the best assumption, so it's up to the
    # user to delete the fingerprints table file or manually re-run the
    # generation task when it should be updated.
    if not os.path.exists(FINGERPRINTS_TABLE_FILENAME):
        execute(generate_fingerprints_table)

    # We choose not to use fabric's local() because it uses the shell. It's
    # better to avoid invoking the shell.

    # Must have epub first or we receive 'index can't be built errors'.

    # Sometimes Sphinx doesn't detect modifications to files even though they
    # are modified (e.g., includes). As a workaround, clean before building.
    # It's ugly, but it works.
    subprocess.check_call([
        'make', 'clean', 'epub', 'html', 'latexpdf', 'man', 'info'])


@task
@runs_once
def deploy_html_pdf_epub():
    """Deploy the manual to the user's personal web directory in their EOS
    account.
    """
    execute(build)
    subprocess.check_call([
        'rsync',
        '--verbose',
        '--archive',
        '--chmod=go=rX',
        '--compress'
    ] + glob('_build/html/*') + [
        '_build/latex/MasteringEOS.pdf',
        '_build/epub/MasteringEOS.epub',
        # Allow the user to override the username using fabric.
        env.user + '@eos10.cis.gvsu.edu:public_html/mastering-eos'
    ])


@task
@runs_once
def deploy_man_info_for_user():
    """Upload the man page and info docs to user's `~.local' directory."""
    execute(build)
    LOCAL_PREFIX = '.local'
    put('_build/man/eos.7', LOCAL_PREFIX + '/man/man7/eos.7')
    put('_build/texinfo/eos.info', LOCAL_PREFIX + '/share/info/eos.info')


@task
def deploy_man_info_for_lab():
    """Upload the man page and info docs to each EOS machine. Requires root
    access to said machines.
    """
    execute(build)
    # Untested, but this should work.
    GLOBAL_PREFIX = '/usr/local'
    put('_build/man/eos.7', GLOBAL_PREFIX + '/man/eos.7', use_sudo=True)
    put('_build/texinfo/eos.info', GLOBAL_PREFIX + '/share/info/eos.info',
        use_sudo=True)
