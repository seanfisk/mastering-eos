from __future__ import print_function
from glob import glob
import subprocess

from fabric.api import env, task, execute, run, runs_once
from texttable import Texttable

# Allow being overridden from the command-line.
if env.hosts == []:
    env.hosts += [
        'eos{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 25)]
    env.hosts += [
        'arch{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 9)]


@task
def fingerprint_for_machine():
    """Find the SSH fingerprint for a specific machine."""
    return run('ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key.pub', shell=False)


@task
@runs_once
def gen_fingerprints():
    """Generate a fingerprints table for the documentation."""
    results_dict = execute(fingerprint_for_machine)
    table = Texttable()
    # The default decoration produces the correct table.
    table.header(['Host', 'Fingerprint'])

    for host, output in sorted(results_dict.items()):
        # The second element is the fingerprint.
        fingerprint = output.split()[1]
        table.add_row([host, fingerprint])

    with open('ssh/common/fingerprints.rst', 'w') as fingerprint_file:
        print(table.draw(), file=fingerprint_file)


@task
@runs_once
def build():
    """Build the manual."""
    # Must have epub first or we receive 'index can't be built errors'.

    # We choose not to use fabric's local() because it uses the shell. It's
    # better to avoid invoking the shell.
    subprocess.check_call(['make', 'epub', 'html', 'latexpdf', 'man', 'info'])


@task
@runs_once
def deploy():
    """Deploy the manual to the user's personal EOS account."""
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
