import os
from pipes import quote as shquote
import re

import six
from fabric.api import env, task, runs_once, execute, run, get, put
from texttable import Texttable

# Allow being overridden from the command-line.
env.hosts = [
    'eos{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 33)
] + [
    'arch{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 11)
]

# Instruct Fabric to read the SSH config file, but only if it exists. Fabric
# won't crash if we say to use it and it doesn't exist, but it will dump tons
# of warnings to the terminal. We'd like to avoid those.
env.use_ssh_config = os.path.exists(os.path.expanduser(env.ssh_config_path))

SSH_KEYGEN_RE = re.compile(
    r'\d+\s+(?P<fingerprint>(?:(?:[0-9a-f]{2}):){15}[0-9a-f]{2})',
    # Don't care about case for hex digits.
    flags=re.IGNORECASE)

def _get_fingerprint():
    """Retrieve the SSH fingerprint for a specific machine."""
    output = run(
        'ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key.pub', shell=False)
    # The second element is the fingerprint.
    match = SSH_KEYGEN_RE.match(output)
    if not match:
        # Return (not raise) so that execution can continue when skip_bad_hosts
        # is set. Our choice is between doing that and raising a NetworkError,
        # which is recognized internally by Fabric.
        return ValueError('Unexpected format for remote output of ssh-keygen.')
    return match.group('fingerprint')

@task
@runs_once
def make_ssh_fingerprints_table(output):
    ('Generate a table of SSH fingerprints in reStructuredText for the EOS Lab'
     'machines.')
    # Enable skip_bad_hosts -- we will list down hosts as such in the table.
    #
    # skip_bad_hosts and parallel are, unfortunately, mutually exclusive. Don't
    # see why they have to be, but that's the way it is.
    env.skip_bad_hosts = True

    # Generate table.
    results_dict = execute(_get_fingerprint)

    table = Texttable()
    # The default decoration produces the correct table.
    table.header(['Host', 'Fingerprint'])

    for host, command_output in sorted(six.iteritems(results_dict)):
        # Use the short host name.
        short_hostname = host.split('.')[0]

        fingerprint_text = (
            # Indicate that the host is down in the table.
            'down for maintenance' if
            # Fabric returns the exception if the task failed.
            isinstance(command_output, Exception)
            # Use a fixed-width font for the fingerprint itself.
            else '``{0}``'.format(command_output))
        table.add_row((short_hostname, fingerprint_text))

    with open(output, 'w') as output_file:
        six.print_(table.draw(), file=output_file)

@task
@runs_once
def download_vncts_file(output):
    get(remote_path='/etc/xinetd.d/vncts',
        # local_path can be a file-like object.
        local_path=output)

@task
def deploy_to_eos(manpage, infodoc, webscript):
    ('Upload the man page, info docs, and web docs script to each EOS machine.'
     ' Requires root access to said machines.')
    # Collect args and assign more sensible names. We will be doing a lot of
    # path-munging, and having proper names helps.
    man_source_path = manpage
    info_source_path = infodoc
    web_docs_source_path = webscript

    env.user = 'root'
    # skip_bad_hosts and parallel are, unfortunately, mutually exclusive. Don't
    # see why they have to be, but that's the way it is.
    env.skip_bad_hosts = True

    # Don't use os.path.join here, as we are always dealing with GNU/Linux on
    # the EOS machines.

    prefix = '/usr/local'
    share_dir = prefix + '/share'

    man_base = os.path.basename(man_source_path)
    man_section = os.path.splitext(man_base)[1].lstrip('.')
    man_dir = share_dir + '/man/man' + man_section

    info_base = os.path.basename(info_source_path)
    info_dir = share_dir + '/info'

    web_docs_base = os.path.basename(web_docs_source_path)
    bin_dir = prefix + '/bin'

    # Ensure the containing directories are creating, else upload will fail.
    run('mkdir -p ' + ' '.join(map(shquote, [man_dir, info_dir, bin_dir])),
        shell=False)
    put(man_source_path, man_dir + '/' + man_base)
    put(info_source_path, info_dir + '/' + info_base)
    put(web_docs_source_path, bin_dir + '/' + web_docs_base, mode=0755)
