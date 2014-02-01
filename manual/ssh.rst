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
