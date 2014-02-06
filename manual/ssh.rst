==============================
 Accessing EOS Remotely (SSH)
==============================

If you are not sitting in the EOS or Arch lab, EOS can be accessed from home using a protocol called Secure Shell (SSH). SSH allows you to remotely run commands on any EOS machine. Your SSH client of choice depends on your machine's operating system.

Mac OS X and GNU/Linux
======================

Mac OS X and most GNU/Linux distributions come with OpenSSH_, the most popular implementation of the SSH protocol. The client can be run from the command-line and is simply called ``ssh``. If your GNU/Linux distribution does not have it installed by default, please check your package manager. You should not install this software from scratch or on your own.

.. _OpenSSH: http://www.openssh.com/

Microsoft Windows
=================

The most popular and capable SSH client for Windows is called PuTTY_. It can be installed by visiting the `PuTTY download page`_. We recommend installing via the Windows installer, labeled "A Windows installer for everything except PuTTYtel."

.. _PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/
.. _PuTTY download page: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html

Password-less Logins
====================

It is often handy to be able to ``ssh`` into a host without having to type a password (for instance if the ``ssh`` command was part of a script).  In most \*nix systems this is quite easy to accomplish.  First, you need to generate your public/private key pairs with the command

``ssh-keygen``

Accept the default values unless you know what you are doing.  Once the keys have been generated you can copy the public key over to the remote system by entering

``ssh-copy-id <username>@<REMOTE HOST>``

Note that <REMOTE HOST> can be either an IP address or DNS resolvable hostname.  Also note that on OSX machines the ``ssh-copy-id`` command does not exist.  In that case you will manually need to copy over your keys.  This can be done in the following manner:

.. code-block:: bash

    ssh <username>@<REMOTE HOST> 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub

Once this process has been completed users can ``ssh`` into the remote machine without the need of inserting a password.
