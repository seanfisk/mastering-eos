===================
 Microsoft Windows
===================

SSH
===

The most popular SSH client for Windows is called PuTTY_. It can be installed by visiting the `PuTTY download page`_. We recommend installing via the Windows installer, labeled *A Windows installer for everything except PuTTYtel*.

.. _PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/
.. _PuTTY download page: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html

Logging In
----------

The first step we will take is to create a saved session for our EOS connection configuration. This will save time for future logins.

Open PuTTY and enter your username and the hostname of the EOS machine into the :guilabel:`Host Name` field. This has the form *user@host*, for example, :samp:`smithj@eos{XX}.cis.gvsu.edu`, where :samp:`XX` is the number of the chosen machine.

In the field under :guilabel:`Saved Sessions`, type :samp:`EOS` (this name is not strictly required, but is assumed in the next section). Click :guilabel:`Save`.

To log in to EOS, click :guilabel:`Open`. For future logins, simply select the session you created and click :guilabel:`Open` to connect.

Checking Host Fingerprints
--------------------------

When logging in to an EOS machine for the first time, you will see a dialog like this:

.. image:: /images/putty-security-alert.png
    :alt: PuTTY Security Alert

.. include:: common/fingerprints/checking.rst

Password-less Logins (SSH keys)
-------------------------------

It is often handy to be able to SSH into a host without having to type a password, for instance as part of a script. First, we need to generate your public/private key pair. Open PuTTYgen_ from the PuTTY distribution to begin the generation process. Click :guilabel:`Generate` and do the mouse nonsense to generate your keys.

.. _PuTTYgen: http://the.earth.li/~sgtatham/putty/0.63/htmldoc/Chapter8.html#pubkey-puttygen

Copy the text from the field labelled :guilabel:`Public key for pasting into OpenSSH authorized_keys file`. Open Notepad and paste this text. Save it to the desktop as :file:`id_rsa.pub`. Now open Windows PowerShell from the Start Menu and run the following command. If your EOS saved session is named something other than "EOS", you will need to change it in the command below.

.. code-block:: powershell

    $puttySessionName = 'EOS'; Get-Content "$env:USERPROFILE\Desktop\id_rsa.pub" | & "$env:SYSTEMDRIVE\Program Files (x86)\PuTTY\plink" -pw ([Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($(Read-Host -AsSecureString Password)))) $puttySessionName 'umask u=rwx,go= && mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'

Your public key has now been uploaded to EOS. The file :file:`id_rsa.pub` may be deleted now.

However, we still need to be able to tell PuTTY to use your private key to log in to EOS. Back in PuTTYgen, click :guilabel:`Save private key` and save the resulting PPK file to a location of your choosing. We recommend your home directory. Answer *Yes* when you are warned about saving the private key without a passphrase.

.. note::

    If you would like to use a passphrase for your key, see the `PuTTY Guide to Pageant`_ after completing this guide. Setting up an SSH agent is out of the scope of this guide.

Now start up PuTTY, select your saved session, then click :guilabel:`Load`. This loads our previously configured session for editing. In the configuration tree to the left, expand :menuselection:`Connection --> SSH` and click on :guilabel:`Auth`. Click :guilabel:`Browse...` to the right of the field labelled :guilabel:`Private key file for authentication`. Select the PPK file you saved earlier.

Go back to :guilabel:`Session` and click :guilabel:`Save`. PuTTY is now configured to use this private key to connect to EOS. Click :guilabel:`Open` to log in, which you should be able to do without a password.

.. important::

    When you make changes to your configuration, make sure to go back to :guilabel:`Session` and click :guilabel:`Save`. If you click :guilabel:`Open` after making changes, those changes will be applied to the current session but will not be saved for the next time you open PuTTY.

.. hint::

    You can also save a modified configuration under another name by editing the session name in the text box under :guilabel:`Saved Sessions` and clicking :guilabel:`Save`.

As is obvious from these instructions, SSH key management is not a simple process. We recommend reading the `PuTTY Guide to SSH Keys`_, which is the source for much of this information. If you would like to use a passphrase with your key, please see the `PuTTY Guide to Pageant`_, PuTTY's SSH agent.

.. _PuTTY Guide to SSH Keys: http://the.earth.li/~sgtatham/putty/latest/htmldoc/Chapter8.html#pubkey
.. _PuTTY Guide to Pageant: http://the.earth.li/~sgtatham/putty/latest/htmldoc/Chapter9.html#pageant

.. _win-ssh-tunnel:

.. include:: common/forwarding_intro.rst

Fortunately, port forwarding with PuTTY is quite easy. Fire up PuTTY and select your saved session, then click the :guilabel:`Load`. In the configuration tree to the left, expand :menuselection:`Connection --> SSH` and click on :guilabel:`Tunnels`.

In the :guilabel:`Source port` field, we will enter the port to which traffic should arrive on our local machine. In the destination field, we will enter the host and port from which the traffic should be forwarded in the form :samp:`{host}:{port}`. The host will usually match the EOS machine to which you are connecting using SSH, although this is not required. The radio buttons should be left at :guilabel:`Local` for the forwarding type and :guilabel:`Auto` for the Internet protocol.

For example, where :samp:`eos{XX}.cis.gvsu.edu` is the remote EOS machine, to access a web server running on port 8000 on the EOS machine from your machine on port 5555, enter the following:

+-----------+---------------------------------+
|Source port|5555                             |
+-----------+---------------------------------+
|Destination|:samp:`eos{XX}.cis.gvsu.edu:8000`|
+-----------+---------------------------------+

Click :guilabel:`Add` to add this as a forwarded port, then click :guilabel:`Open` (we will not save this configuration).

You can test the forwarding by running this in the SSH prompt::

    python -m SimpleHTTPServer

and opening http://localhost:5555/ in your local web browser. You should see a web listing of your home directory! Press :kbd:`Control-C` to kill the web server.

The remote host which is hosting the resource need not be the EOS machine to which you are connecting with SSH. Let's access the CIS web server through the SSH tunnel.

Restart PuTTY, load your session, and navigate back to the :guilabel:`Tunnels` screen. Enter the following information:

+-----------+-------------------+
|Source port|5678               |
+-----------+-------------------+
|Destination|``cis.gvsu.edu:80``|
+-----------+-------------------+

Click :guilabel:`Add` and :guilabel:`Open`, then visit http://localhost:5678/ in your local web browser. The CIS home page should appear!

.. include:: common/vnc_intro.rst

Restart PuTTY, load your session, and navigate back to the :guilabel:`Tunnels` screen. Enter the following information:

+-----------+------------------------------------------+
|Source port|5900                                      |
+-----------+------------------------------------------+
|Destination|:samp:`eos{XX}.cis.gvsu.edu:{REMOTE_PORT}`|
+-----------+------------------------------------------+

Go back to :guilabel:`Session` and click :guilabel:`Save`. You are now ready to tunnel your VNC session. Click :guilabel:`Open` to start the tunnel.

.. hint::

    If you clone a session for an EOS machine (using :guilabel:`Load` and :guilabel:`Save`), don't forget to change the tunnel to forward ports to that machine.

The recommended VNC client for Windows is TightVNC_. Download it, install, then open. In the field labelled :guilabel:`Remote Host`, type ``localhost``. Click :guilabel:`Connect` to start the connection.

For future connections, simply start TightVNC and click :guilabel:`Connect`. Alternatively, during the session, you can save the configuration to a file by clicking the :guilabel:`Save` button, shown as a diskette. After saving the configuration to a ``*.vnc`` file, double click the file to start the connection.

.. _TightVNC: http://tightvnc.com/download.php

File Transfer
=============

Graphical
---------

The recommend graphical client for file transfer on Mac OS X is WinSCP_, which can be found on the `WinSCP downloads page`_. We recommend downloading the latest stable installer, labeled *Installation package*. It should be near the top.

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
~~~~~~~~~~~~~~~~~~~~~~~~~

Automatic synchronization of local to remote directories is a very useful advanced feature of WinSCP. It is especially useful when developing a website on EOS. This partially makes up for the lack of a maintained free Windows SSHFS implementation.

To start using it, click :menuselection:`Commands --> Keep Remote Directory up to Date...`. You can get more information about this task and its use in the `WinSCP Keep Remote Directory up to Date documentation`_.

.. _WinSCP Keep Remote Directory up to Date documentation: http://winscp.net/eng/docs/task_keep_up_to_date

For more information on using WinSCP, consult the excellent `WinSCP Documentation`_.

.. _WinSCP Documentation: http://winscp.net/eng/docs/start

Command Line (SCP)
------------------

Files can be transferred on the command line using a utility called SCP, implemented in PuTTY through a command called ``pscp``. Because ``pscp`` uses PuTTY for authentication, if you have set up `Password-less Logins (SSH keys)`_, you will not have to type any passwords. SCP stands for *Secure Copy* and works very similar to the GNU/Linux ``cp`` command, except that it can also transfer files across the network. Make sure you are familiar with the operation of ``cp`` before using SCP.

PuTTY's commands are not added to the Windows `Path`_ by default. To add them to the :envvar:`Path`, open Windows PowerShell from the Start Menu and run the following command. If you installed PuTTY to a non-default location, you will need to change it in the command below.

.. _Path: http://en.wikipedia.org/wiki/PATH_%28variable%29

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

Alternative Clients
===================

Though PuTTY is the recommended SSH client for Windows, OpenSSH is also available. The recommended way of running OpenSSH on Windows is through Cygwin_. Cygwin is not simple to use and configure, but depending on your needs, it may provide a better SSH experience. OpenSSH is well-known as the best SSH client out there, and EOS uses OpenSSH as an SSH server as well.

.. _Cygwin: http://www.cygwin.com/

There are a plethora of alternate VNC viewers available for Windows, many based on the same original RealVNC code.

`UltraVNC <http://www.uvnc.com/>`_ and `TigerVNC <http://tigervnc.org/>`_ offer relatively simple user interfaces with an appropriate amount of configuration options. If you don't like or are having trouble with TightVNC, give UltraVNC a try.

RealVNC `Viewer <http://realvnc.com/download/viewer/>`_ and `Viewer Plus <http://www.realvnc.com/download/viewerplus/>`_ are freeware viewers, but require registration. RealVNC also offers `RealVNC Viewer for Google Chrome <https://chrome.google.com/webstore/detail/vnc-viewer-for-google-chr/iabmpiboiopbgfabjmgeedhcmjenhbla?hl=en>`_, a free Google Chrome extension which does not require registration.

Cyberduck_ is also available for Windows. Cyberduck has a more attractive and intuitive interface than WinSCP. However, unlike WinSCP, Cyberduck does not support automatic synchronization. This is important because high-quality free versions of SSHFS and rsync are not available for Windows.

.. _Cyberduck: http://cyberduck.io/

MobaXterm_ is an all-in-one solution for SSH, SCP, VNC, RDP, and more. Since it is a unified product, it provides a smoother experience than a collection of standalone applications. However, because it includes much more capability, it can be difficult to configure. It is worth a try if your time spent on EOS warrants it.

.. _MobaXterm: http://mobaxterm.mobatek.net/

.. include:: common/filezilla_warning.rst
