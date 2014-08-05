from __future__ import print_function
import subprocess
import os
import stat
import errno
from tempfile import mkdtemp
import shutil
import tarfile
import zipfile

from fabric.api import env, task, execute, run, runs_once, put
from texttable import Texttable

POSTER_DIR = 'poster'
MANUAL_DIR = 'manual'
FINGERPRINTS_TABLE_FILENAME = os.path.join(
    MANUAL_DIR, 'remote_access', 'common', 'fingerprints', 'table.rst')
VNC_TABLE_FILENAME = os.path.join(
    MANUAL_DIR, 'remote_access', 'common', 'vnc_port_geometry_table.rst')
BUILD_DIR = os.path.join(MANUAL_DIR, '_build')

# Allow being overridden from the command-line.
if env.hosts == []:
    env.hosts += [
        'eos{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 25)]
    env.hosts += [
        'arch{0:02}.cis.gvsu.edu'.format(num) for num in xrange(1, 11)]


class cwd(object):
    """Class used for temporarily changing directories. Can be though of
    as a `pushd /my/dir' then a `popd' at the end.
    """
    def __init__(self, newcwd):
        """:param newcwd: directory to make the cwd
        :type newcwd: :class:`str`
        """
        self.newcwd = newcwd

    def __enter__(self):
        self.oldcwd = os.getcwd()
        os.chdir(self.newcwd)
        return os.getcwd()

    def __exit__(self, type, value, traceback):
        # This acts like a `finally' clause: it will always be executed.
        os.chdir(self.oldcwd)


def copy_dir_contents(src_dir, dest_dir):
    """Copy the contents of an existing directory to an existing destination
    directory."""
    # Annoying way to copy a tree to an existing directory.
    with cwd(src_dir):
        for rel_path in os.listdir('.'):
            dest_path = os.path.join(dest_dir, rel_path)
            try:
                shutil.copytree(rel_path, dest_path)
            except OSError as exc:
                # Use exception handling to avoid the race condition between
                # checking whether the file is a directory and copying it.
                if exc.errno == errno.ENOTDIR:
                    shutil.copyfile(rel_path, dest_path)
                else:
                    raise


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

    for host, command_output in sorted(results_dict.iteritems()):
        # Use the short host name.
        short_hostname = host.split('.')[0]

        if isinstance(command_output, Exception):
            # Note that the host is down in the table when '--skip-bad-hosts'
            # is given on the command line.
            fingerprint_text = 'down for maintenance'
        else:
            # Use a fixed-width for the fingerprint itself.
            fingerprint_text = '``{0}``'.format(command_output)
        table.add_row((short_hostname, fingerprint_text))

    with open(FINGERPRINTS_TABLE_FILENAME, 'w') as fingerprint_file:
        print(table.draw(), file=fingerprint_file)


@task
@runs_once
def generate_vnc_table():
    """Generate the VNC port/geometry table for the manual."""
    script_name = 'vnc_extract_port_geometry.py'
    dest_path = '~/bin/' + script_name
    put(os.path.join('scripts', script_name), dest_path, mode=stat.S_IRWXU)
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
def build_manual():
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
    with cwd(MANUAL_DIR):
        subprocess.check_call([
            'make', 'clean', 'epub', 'html', 'latexpdf', 'man', 'info'])


@task
@runs_once
def build_poster():
    """Build the poster."""
    with cwd(POSTER_DIR):
        subprocess.check_call(['scons'])


@task
@runs_once
def build():
    build_manual()
    build_poster()


def create_html_dist_directory():
    """Prepare an HTML website directory suitable for distribution. It is
    placed in a temporary directory, and the path to the directory is returned.
    The calling code is responsible for deleting the directory."""
    execute(build)

    name = 'mastering-eos-html'
    dist_dir = mkdtemp(prefix='mastering-eos-dist-')
    html_src_dir = os.path.join(BUILD_DIR, 'html')

    # Copy HTML (and other asset) files.
    copy_dir_contents(html_src_dir, dist_dir)

    # Copy PDF and EPUB.
    shutil.copy(
        os.path.join(BUILD_DIR, 'epub', 'mastering-eos.epub'), dist_dir)
    shutil.copy(
        os.path.join(BUILD_DIR, 'latex', 'mastering-eos.pdf'), dist_dir)

    # Copy poster.
    shutil.copyfile(
        os.path.join(POSTER_DIR, 'mastering-eos.pdf'),
        os.path.join(dist_dir, 'mastering-eos-poster.pdf'))

    # Create extra HTML archives.
    temp_dir = mkdtemp(prefix='mastering-eos-tmp-')
    temp_html_dir_path = os.path.join(temp_dir, name)
    shutil.copytree(html_src_dir, temp_html_dir_path)

    tarfile_path = os.path.join(dist_dir, name + '.tar.gz')
    zipfile_path = os.path.join(dist_dir, name + '.zip')

    with cwd(temp_dir):
        tar = tarfile.open(tarfile_path, 'w:gz')
        tar.add(name)
        tar.close()

        zip_ = zipfile.ZipFile(zipfile_path, 'w')
        for dirpath, dirnames, filenames in os.walk(name):
            for filename in filenames:
                zip_.write(os.path.join(dirpath, filename))
        zip_.close()

    shutil.rmtree(temp_dir)

    return dist_dir


@task
@runs_once
def deploy_eos_web():
    ("Deploy the manual to the user's personal web directory in their EOS "
     'account.')
    temp_dir = create_html_dist_directory()
    with cwd(temp_dir):
        subprocess.check_call([
            'rsync',
            '--verbose',
            '--archive',
            '--compress',
            '--chmod=go=rX',
            '.',
            # Allow the user to override the username using fabric.
            env.user + '@eos10.cis.gvsu.edu:public_html/mastering-eos',
        ])
    shutil.rmtree(temp_dir)


@task
@runs_once
def deploy_github_pages():
    """Deploy the manual to GitHub pages."""
    temp_dir = create_html_dist_directory()
    subprocess.check_call([
        'ghp-import',
        '-n',  # Include a .nojekyll file in the branch
        '-p',  # Push the branch after import
        temp_dir,
    ])
    shutil.rmtree(temp_dir)


@task
@runs_once
def deploy_man_info_for_user():
    """Upload the man page and info docs to user's `~/.local` directory."""
    execute(build)
    LOCAL_PREFIX = '.local/share'
    run('mkdir -p {0}/man/man7 {0}/info'.format(LOCAL_PREFIX), shell=False)
    put(os.path.join(BUILD_DIR, 'man', 'eos.7'),
        LOCAL_PREFIX + '/man/man7/eos.7')
    put(os.path.join(BUILD_DIR, 'texinfo', 'eos.info'),
        LOCAL_PREFIX + '/info/eos.info')


@task
def deploy_man_info_for_lab():
    ('Upload the man page and info docs to each EOS machine. Requires root '
     'access to said machines.')
    execute(build)
    env.user = 'root'
    GLOBAL_PREFIX = '/usr/local/share'
    run('mkdir -p {0}/man/man7 {0}/info'.format(GLOBAL_PREFIX), shell=False)
    put(os.path.join(BUILD_DIR, 'man', 'eos.7'),
        GLOBAL_PREFIX + '/man/man7/eos.7')
    put(os.path.join(BUILD_DIR, 'texinfo', 'eos.info'),
        GLOBAL_PREFIX + '/info/eos.info')
