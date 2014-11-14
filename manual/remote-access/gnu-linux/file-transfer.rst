===============
 File Transfer
===============

Graphical
=========

GNOME
-----

The GNOME desktop features the `GNOME Virtual Filesystem`_ (GVFS), which has native support for SFTP. First, start up the file manager (:wikipedia:`GNOME Files <GNOME_Files>`, formerly known as Nautilus). On the left pane, click :menuselection:`Network ---> Connect to Server`. In the :guilabel:`Server Address` field, enter :samp:`sftp://{smithj}@eos01.cis.gvsu.edu`. Your files on EOS should be displayed.

.. _GNOME Virtual Filesystem: https://wiki.gnome.org/action/show/Projects/gvfs

If you need to access these files from the command line, you can find your EOS account mounted as a subdirectory of this directory::

    ls $XDG_RUNTIME_DIR/gvfs

KDE
---

KDE's file manager, Dolphin_, also support SFTP URLs. First, click :menuselection:`Places ---> Network` in the pane on the left. Then, click :guilabel:`Add Network Folder`. Select :guilabel:`Secure shell (ssh)` as the type and click :guilabel:`Next`. Fill out the form as follows, then click :guilabel:`Save & Connect`:

.. image:: /images/kde-file-transfer.png
    :alt: SSH file transfer with KDE Dolphin

Both the SFTP and FISH protocols *should* work, although we have had the most luck with the FISH protocol.

.. _Dolphin: https://www.kde.org/applications/system/dolphin/

Other Desktop Managers
----------------------

This guide only covers GNOME and KDE. However, many GNU/Linux file managers are very similar, and most offer support for SSH file transfer. Consult your desktop's documentation for more information, or just try to figure it out on your own.

.. |ssh-keys| replace:: :ref:`linux-ssh-keys`
.. include:: ../common/openssh/scp.rst

.. include:: ../common/rsync.rst

.. include:: ../common/sshfs/intro.rst

Installation
------------

SSHFS is popular package and is usually available through your operating system's package manager.

On Debian-based systems (Ubuntu, Linux Mint, and friends), run the following command::

    sudo apt-get install sshfs

On Red Hat-based systems (Fedora, CentOS, RHEL, and friends), run the following command::

    sudo yum install fuse-sshfs

For other distributions (Arch, etc.), the package name and command should be similar. Consult your package management tool for details.

To mount your EOS home directory, first create a mount point for it::

    mkdir ~/eos

Next, mount your EOS home directory using SSHFS::

    sshfs -o volname=EOS smithj@eos01.cis.gvsu.edu: ~/eos

.. tip::

    If you set up :ref:`linux-ssh-aliases`, you can use these with SSHFS::

        sshfs -o volname=EOS eos01: ~/eos

Test the mount point by listing your EOS files::

    ls ~/eos

You should now be able to use files on your EOS account as if they were on your own machine. For example, you can open and browse your files using your file browser::

    xdg-open ~/eos

Be aware that there may be some lag in the filesystem, especially when using programs which access the filesystem frequently.

When finished with the mount point, make sure to unmount it::

    fusermount -u ~/eos

SSHFS accepts many options which can be viewed with ``man ssh`` or ``sshfs --help``. For example, to enable caching and automatic reconnection (recommended)::

    sshfs -o auto_cache,reconnect smithj@eos01.cis.gvsu.edu: ~/eos

If you use this command often, you may want to create script or alias for it.

.. TODO Link to aliases when shell section is done.

.. include:: ../common/sshfs/outro.rst
