===================
 Microsoft Windows
===================

The most popular SSH client for Windows is called PuTTY_. It can be installed by visiting the `PuTTY download page`_. We recommend installing via the Windows installer, labeled *A Windows installer for everything except PuTTYtel*.

.. _PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/
.. _PuTTY download page: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html

Logging In
==========

The first we will do is create a saved session for our EOS connection configuration. This will save time for future logins.

Open PuTTY and enter your username and the hostname of the EOS machine to which you would like to log into the :guilabel:`Host Name` field. This will take the form *user@host*, for example, :samp:`doej@eos{XX}.cis.gvsu.edu`, where :samp:`XX` is the number of the chosen machine.

In the field under :guilabel:`Saved Sessions`, type :samp:`EOS` (this name is not strictly required, but is assumed in the next section). Click :guilabel:`Save`.

To log in to EOS, click :guilabel:`Open`. For future logins, you may now simply select the session you created and click :guilabel:`Open` to connect.

Checking Host Fingerprints
==========================

When logging in to an EOS machine for the first time, you will see a dialog like this:

.. image:: /_static/putty-security-alert.png
    :alt: PuTTY Security Alert

.. include:: common/checking_fingerprints.rst

Password-less Logins
====================

It is often handy to be able to SSH into a host without having to type a password, for instance as part of a script. First, we need to generate our public/private. Open PuTTYgen_ from the PuTTY distribution to begin the generation process. Click :guilabel:`Generate` and do the mouse nonsense to generate your keys.

Copy the text from the field labelled :guilabel:`Public key for pasting into OpenSSH authorized_keys file`. Open Notepad and paste this text. Save it to the desktop as :file:`id_rsa.pub`. Now open Windows PowerShell from the Start Menu and run the following command. If your EOS saved session is named something other than "EOS", you will need to change it.

.. code-block:: powershell

    Get-Content "$env:USERPROFILE\Desktop\id_rsa.pub" | & "$env:PROGRAMFILES\PuTTY\plink" -pw ([Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($(Read-Host -AsSecureString Password)))) EOS 'umask u=rwx,go= && mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'

.. _PuTTYgen: http://the.earth.li/~sgtatham/putty/0.63/htmldoc/Chapter8.html#pubkey-puttygen

Your public key has now been uploaded to EOS. The file :file:`id_rsa.pub` may be deleted now.

However, we still need to be able to tell PuTTY to use your private key to log in to EOS. Back in PuTTYgen, click :guilabel:`Save private key` and save the resulting PPK file to a location of your choosing. We recommend your home directory. Answer *Yes* when you are warned about saving the private key without a passphrase.

.. note::

    If you would like to use a passphrase for your key, see the `PuTTY Guide to Pageant`_ after completing this guide. Setting up an SSH agent is out of the scope of this guide.

Now start up PuTTY, click your saved session, then click :guilabel:`Load`. In the configuration tree to the left, expand :menuselection:`Connection --> SSH` and click on :guilabel:`Auth`. Click :guilabel:`Browse...` to the right of the field labelled :guilabel:`Private key file for authentication`. Select the PPK file you saved earlier.

Go back to :guilabel:`Session` and click :guilabel:`Save`. PuTTY is now configured to use this private key to connect to EOS. Click :guilabel:`Open` and you should be able to log in without a password.

As is obvious from these instructions, SSH key management is not a simple process. We recommend reading the `PuTTY Guide to SSH Keys`_, which is the source for much of this information. If you would like to use a passphrase with your key, please see the `PuTTY Guide to Pageant`_, PuTTY's SSH agent.

OpenSSH is also available for Windows, though PuTTY is the recommended client.

.. _PuTTY Guide to SSH Keys: http://the.earth.li/~sgtatham/putty/latest/htmldoc/Chapter8.html#pubkey
.. _PuTTY Guide to Pageant: http://the.earth.li/~sgtatham/putty/latest/htmldoc/Chapter9.html#pageant
