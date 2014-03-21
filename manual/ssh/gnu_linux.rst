===========
 GNU/Linux
===========

The most popular implementation of the SSH protocol on GNU/Linux is OpenSSH_. The SSH client can be run from the command-line and is simply called :program:`ssh`.

Many GNU/Linux distributions come with OpenSSH_ pre-installed. If your GNU/Linux distribution does not have it installed by default, please install it with your package manager. You should not install this software from scratch or on your own.

On Debian-based systems (Ubuntu, Linux Mint, etc.), run the following command::

    sudo apt-get install openssh-client

On Red Hat-based systems (Fedora, CentOS, RHEL, etc.), run the following command::

    sudo yum install openssh-clients

With other distributions (Arch, etc.), you are on your own.

.. _OpenSSH: http://www.openssh.com/

.. include:: common/basic_openssh.rst

.. include:: common/keys_intro.rst

::

    ssh-copy-id smithj@eos01.cis.gvsu.edu

.. include:: common/keys_outro.rst
