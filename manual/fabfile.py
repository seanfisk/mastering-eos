from __future__ import print_function

from fabric.api import env, task, execute, run, runs_once
from texttable import Texttable

# Allow being overridden from the command-line.
if env.hosts == []:
    env.hosts += [
        'eos{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 25)]
    env.hosts += [
        'arch{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 9)]


@task
def per_machine():
    return run('ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key.pub', shell=False)


@task
@runs_once
def fingerprints():
    results_dict = execute(per_machine)
    table = Texttable()
    # The default decoration produces the correct table.
    table.header(['Host', 'Fingerprint'])

    for host, output in sorted(results_dict.items()):
        # The second element is the fingerprint.
        fingerprint = output.split()[1]
        table.add_row([host, fingerprint])

    with open('ssh/common/fingerprints.rst', 'w') as fingerprint_file:
        print(table.draw(), file=fingerprint_file)
