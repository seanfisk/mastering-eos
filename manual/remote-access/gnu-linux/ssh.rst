=====
 SSH
=====

The most popular implementation of the SSH protocol on GNU/Linux is OpenSSH_. The SSH client can be run from the command-line and is simply called :program:`ssh`.

Many GNU/Linux distributions come with OpenSSH_ pre-installed. If your GNU/Linux distribution does not have it installed by default, please install it with your package manager. You should not install this software from scratch or on your own.

On Debian-based systems (Ubuntu, Linux Mint, and friends), run the following command::

    sudo apt-get install openssh-client

On Red Hat-based systems (Fedora, CentOS, RHEL, and friends), run the following command::

    sudo yum install openssh-clients

For other distributions (Arch, etc.), the package name and command should be similar. Consult your package management tool for details.

.. _OpenSSH: http://www.openssh.com/

.. include:: ../common/openssh/connect.rst

.. _linux-fingerprints:

.. include:: ../common/openssh/fingerprints.rst

.. _linux-ssh-keys:

.. include:: ../common/keys/intro.rst

::

    ssh-copy-id smithj@eos01.cis.gvsu.edu

.. include:: ../common/keys/outro.rst

.. This label is used for BetterPlanner; do not remove.
.. _linux-ssh-tunnel:

.. include:: ../common/openssh/forwarding.rst
