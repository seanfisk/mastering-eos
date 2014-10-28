=====
 SSH
=====

The most popular SSH client for Windows is called PuTTY_. It can be installed by visiting the `PuTTY download page`_. We recommend installing via the Windows installer, labeled *A Windows installer for everything except PuTTYtel*.

.. _PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/
.. _PuTTY download page: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html

Logging In
==========

The first step we will take is to create a saved session for our EOS connection configuration. This will save time for future logins.

Open PuTTY and enter your username and the hostname of the EOS machine into the :guilabel:`Host Name` field. This has the form *user@host*, for example, :samp:`smithj@eos{XX}.cis.gvsu.edu`, where :samp:`XX` is the number of the chosen machine.

In the field under :guilabel:`Saved Sessions`, type :samp:`EOS` (this name is not strictly required, but is assumed in the next section). Click :guilabel:`Save`.

To log in to EOS, click :guilabel:`Open`. For future logins, simply select the session you created and click :guilabel:`Open` to connect.

Checking Host Fingerprints
==========================

When logging in to an EOS machine for the first time, you will see a dialog like this:

.. image:: /images/putty-security-alert.png
    :alt: PuTTY Security Alert

.. include:: ../common/fingerprints/checking.rst

.. _win-ssh-keys:

Password-less Logins (SSH keys)
===============================

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

.. include:: ../common/forwarding-intro.rst

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
