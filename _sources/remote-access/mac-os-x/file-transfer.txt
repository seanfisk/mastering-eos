===============
 File Transfer
===============

Graphical
=========

The recommend graphical client for file transfer on Mac OS X is Cyberduck_. It is quite easy to use. Download the application, install as normal, and start Cyberduck.

.. _Cyberduck: http://cyberduck.io/

Click :guilabel:`Open Connection`. From the drop-down box, select :guilabel:`SFTP (SSH File Transfer Protocol)`. Type in the EOS machine to which you'd like to connect in the :guilabel:`Server` field and fill in your username.

If you have set up :ref:`mac-ssh-keys`, click the :guilabel:`Use Public Key Authentication` checkbox and select the file :file:`id_rsa`. This is the identity file that you use to log in to EOS. If you have not set up your keys, you can still use password authentication, although this is not recommended.

If you have created a config file with hostname aliases, you may also notice Cyberduck auto-detect your configuration and fill in some information.

Your connection information should look something like this:

.. image:: /images/mac-cyberduck-conf.png
   :alt: Cyberduck Configuration

After connecting, we recommend creating a bookmark so that you can easily return. Click :menuselection:`Bookmark --> New Bookmark` to create one. You can change the nickname if you like. When you start Cyberduck again, simply click your bookmark to connect.

Most of Cyberduck's action are available through the :guilabel:`File` menu or the right-click context menu. In addition, Cyberduck has great support for dragging between it and Finder.

.. |ssh-keys| replace:: :ref:`mac-ssh-keys`
.. include:: ../common/openssh/scp.rst

.. include:: ../common/rsync.rst

.. include:: ../common/sshfs/intro.rst

Installation
------------

The OSXFUSE_ project maintains high-quality packages of FUSE and SSHFS. Visit the homepage and download and install the stable versions of *both* OSXFUSE and SSHFS to get started.

.. _OSXFUSE: http://osxfuse.github.io/

Use
---

To mount your EOS home directory, first create a mount point for it::

   mkdir ~/eos

Next, mount your EOS home directory using SSHFS::

   sshfs -o volname=EOS smithj@eos01.cis.gvsu.edu: ~/eos

.. tip::

   If you set up :ref:`mac-ssh-aliases`, you can use these with SSHFS::

      sshfs -o volname=EOS eos01: ~/eos

Test the mount point by listing your EOS files::

   ls ~/eos

You should now be able to use files on your EOS account as if they were on your own machine. For example, you can open and browse your files using Finder::

   open ~/eos

Be aware that there may be some lag in the filesystem, especially when using Finder or other programs which access the filesystem frequently.

When finished with the mount point, make sure to unmount it::

   diskutil unmount ~/eos

The mount point can also be unmounted using Finder:

.. image:: /images/mac-sshfs-eject.png
   :alt: Ejecting an SSHFS filesystem using Finder

SSHFS accepts many options which can be viewed with ``man ssh`` or ``sshfs --help``. For example, to enable caching and automatic reconnection (recommended)::

   sshfs -o auto_cache,reconnect,volname=EOS smithj@eos01.cis.gvsu.edu: ~/eos

If you use this command often, you may want to create script or alias for it.

.. TODO Link to aliases when shell section is done.

.. include:: ../common/sshfs/outro.rst

Another option for SSH file transfer on Mac OS X is ExpanDrive_, a commercial product.
