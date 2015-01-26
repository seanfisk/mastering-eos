===============
 File Transfer
===============

Graphical
=========

The recommend graphical client for file transfer on Windows is WinSCP_, which can be found on the `WinSCP downloads page`_. We recommend downloading the latest stable installer, labeled *Installation package*. It should be near the top.

.. _WinSCP: http://winscp.net/eng/index.php
.. _WinSCP downloads page: http://winscp.net/eng/download.php

After downloading, run the installer. The *Typical installation* is usually fine, but feel free to customize the installation options. You can choose either the *Commander* or *Explorer* interface, but keep in mind that most people use the *Commander* interface. Don't forget to disable the sneaky Google Chrome installer included with this installer.

After the installer copies its files, it may detect your sessions from PuTTY. If so, click :guilabel:`OK` to import them. Select the sessions you'd like to import and click :guilabel:`OK` again. This is the single easiest way to start quickly with WinSCP.

At the end of the installer, leave the box labeled :guilabel:`Launch WinSCP` checked. You can choose to open the *Getting started* page as well, although there is really no need to do so.

If you didn't choose to import your sites from PuTTY in the installer, you can also import them from the WinSCP Login screen by clicking :menuselection:`Tools --> Import Sites...`, selecting the sites, and clicking :guilabel:`OK`.

There is really no reason not to import your sites from PuTTY if you already have them configured (you should). However, if you'd like to create a custom site, click :guilabel:`New Site`. Choose SFTP as the protocol, and enter in the EOS machine for :guilabel:`Host name` as well as your username. For authentication, you can use a password or SSH keys. To select a key, click :guilabel:`Advanced...`, then :menuselection:`SSH --> Authentication --> Authentication parameters --> Private key file` to select the private key file. Click :guilabel:`Save` to save your site.

.. tip::

    You can create a desktop shortcut for your site by right-clicking your site in the WinSCP Login screen, then clicking :guilabel:`Desktop Icon`. This allows you to open your site directly without visiting the WinSCP Login screen. Creating a 'Send To' shortcut for Windows Explorer is similarly useful.

Automatic Synchronization
-------------------------

Automatic synchronization of local to remote directories is a very useful advanced feature of WinSCP. It is especially useful when developing a website on EOS. This partially makes up for the lack of a maintained free Windows SSHFS or rsync implementation.

To start using it, click :menuselection:`Commands --> Keep Remote Directory up to Date...`. You can get more information about this task and its use in the `WinSCP Keep Remote Directory up to Date documentation`_.

.. _WinSCP Keep Remote Directory up to Date documentation: http://winscp.net/eng/docs/task_keep_up_to_date

For more information on using WinSCP, consult the excellent `WinSCP Documentation`_.

.. _WinSCP Documentation: http://winscp.net/eng/docs/start

Command Line (SCP)
==================

Files can be transferred on the command line using a utility called SCP, implemented in PuTTY through a command called ``pscp``. Because ``pscp`` uses PuTTY for authentication, if you have set up :ref:`win-ssh-keys`, you will not have to type any passwords. SCP stands for *Secure Copy* and works very similar to the GNU/Linux ``cp`` command, except that it can also transfer files across the network. Make sure you are familiar with the operation of ``cp`` before using SCP.

PuTTY's commands are not added to the Windows :envvar:`Path` by default. To add them to the :envvar:`Path`, open Windows PowerShell from the Start Menu and run the following command. If you installed PuTTY to a non-default location, you will need to change it in the command below.

.. code-block:: powershell

    $puttyInstallPath = 'C:\Program Files (x86)\PuTTY'; [Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path', 'User') + ';' + $puttyInstallPath, 'User')

Restart PowerShell or your terminal emulator after running this command to allow your updates to the :envvar:`Path` to take effect. The ``pscp`` utility may now be used from PowerShell by simply typing ``pscp``.

The following examples showcase the typical use of ``pscp``. Each file can be prefixed with a PuTTY session name or user/host, which tells ``pscp`` where it is or should be located. The session name "EOS" is used in these examples; change it to match your PuTTY session name if it is different. Files with no prefix are assumed to be on the local machine. Paths on the remote machine start at your home directory, so there is typically no need to include :file:`/home/smithj` in the path. Here are some examples of use of ``pscp``:

.. code-block:: powershell

    # Typical upload
    pscp classes\cis162\hw1.txt EOS:classes/cis162
    # Typical download
    pscp EOS:classes/cis162/hw2.txt classes\cis162
    # Upload a directory
    pscp -r projects EOS:classes/cis163
    # User/host instead of EOS session name (will likely require password)
    pscp smithj@eos01.cis.gvsu.edu:classes/cis162/hw3.txt classes/cis162

.. note::

    Windows uses ``\`` as a path separator by default, while GNU/Linux uses ``/``. While Windows is generally forgiving and will accept ``/`` as well, GNU/Linux is not. *Always use* ``/`` *as a path separator when specifying GNU/Linux paths.*

.. include:: ../common/sshfs/intro.rst

Unfortunately, there are no stand-out options for SSHFS on Windows. The following programs are possible solutions of which we are aware:

* ExpanDrive_ is a commercial product with a free trial available. While the product works well, the prices are in the expensive range.
* win-sshfs_ is an open-source SSHFS implementation for Windows. Unfortunately, it is not being maintained and therefore we cannot recommend it.
* `dimov-cz's win-sshfs fork`_ is a maintained fork of win-sshfs. However, no binaries are provided, so it must be compiled from source. If you are familiar with compiling and installing .NET programs, this may be a viable alternative for you.

Although none of these programs are supported, you are welcome to try them if they seem useful to you.

.. _win-sshfs: https://code.google.com/p/win-sshfs/
.. _dimov-cz's win-sshfs fork: https://github.com/dimov-cz/win-sshfs

.. include:: ../common/sshfs/outro.rst
