==========
 Mac OS X
==========

.. contents::
   :local:

SSH
===

Mac OS X comes preinstalled with OpenSSH, the most popular implementation of the SSH protocol. The client can be run from the command-line and is simply called ``ssh``.

.. include:: common/openssh/connect.rst

.. include:: common/openssh/fingerprints.rst

.. _mac-ssh-keys:

.. include:: common/keys/intro.rst

.. code-block:: bash

    ssh smithj@eos01.cis.gvsu.edu 'umask u=rwx,go= && mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub

.. include:: common/keys/outro.rst

.. |text-editor| replace:: open -t
.. _mac-ssh-tunnel:
.. include:: common/openssh/forwarding.rst

The recommended VNC client for OS X is Chicken_, which is free and open-source software. Visit the website to download, install as you would any other Mac OS X application, and open.

You will be prompted to create a new server. If not prompted, click :menuselection:`Connection --> Open Connection...` from the menu bar. Double click "New Server" in the list on the left and rename it to "EOS", or create a new session with the :guilabel:`+` button if none exist. Leave the :guilabel:`Host` field as ``localhost`` or fill it in if missing. Leave the :guilabel:`Display or port` field at 0 or fill it in if missing.

Chicken has had some problems with the ZRLE encoding with our server. As this can cause a premature end to your session, our recommendation is to manually disable this encoding. To do this, first click the drop-down menu next to :guilabel:`Profile`, and click :guilabel:`Edit Connection Profiles...`. The :guilabel:`Profile Manager` configuration window will open. In the bottom left, enter "EOS" into the field and click the :guilabel:`+` button. Now click the checkbox next to the ZRLE encoding to disable it for EOS sessions. Close the :guilabel:`Profile Manager` window.

Click :guilabel:`Connect` to begin your VNC session with EOS. To connect in the future, select :menuselection:`Connection --> Open Connection...` from the menu, select your EOS configuration, and click :guilabel:`Connect`.

.. note:: Although Chicken offers an option to tunnel directly through SSH, we have not had luck using this option with our setup. We recommend sticking with the traditional SSH tunnel, as it is tested and works well.

.. _Chicken: http://sourceforge.net/projects/chicken/

File Transfer
=============

Graphical
---------

The recommend graphical client for file transfer on Mac OS X is Cyberduck_. It is quite easy to use. Download the application, install as normal, and start Cyberduck.

.. _Cyberduck: http://cyberduck.io/

Click :guilabel:`Open Connection`. From the drop-down box, select :guilabel:`SFTP (SSH File Transfer Protocol)`. Type in the EOS machine to which you'd like to connect in the :guilabel:`Server` field and fill in your username.

If you have set up `Password-less Logins (SSH keys)`_, click the :guilabel:`Use Public Key Authentication` checkbox and select the file :file:`id_rsa`. This is the identity file that you use to log in to EOS. If you have not set up your keys, you can still use password authentication, although this is not recommended.

If you have created a config file as in `Hostname Aliases`_, you may also notice Cyberduck auto-detect your configuration and fill in some information.

Your connection information should look something like this:

.. image:: /images/mac-cyberduck-conf.png
   :alt: Cyberduck Configuration

After connecting, we recommend creating a bookmark so that you can easily return. Click :menuselection:`Bookmark --> New Bookmark` to create one. You can change the nickname if you like. When you start Cyberduck again, simply click your bookmark to connect.

Most of Cyberduck's action are available through the :guilabel:`File` menu or the right-click context menu. In addition, Cyberduck has great support for dragging between it and Finder.

.. include:: common/openssh/scp.rst

Alternative Clients
===================

Chicken is not the only VNC viewer available for Mac OS X. Some alternatives are:

.. Note: We've considered using TigerVNC over Chicken as the primary client for Mac OS X. TigerVNC has no connection problems and is actively maintained. Chicken, on the other hand, has the issue with the ZRLE encoding and appears inactive. However, TigerVNC's interface is unintuitive, unattractive, and in general inferior to Chicken's. Given these tradeoffs, we've decided to stay with Chicken. If TigerVNC gets better or Chicken gets worse, we should consider switching to TigerVNC again.

* `TigerVNC <http://tigervnc.org/>`_ is a capable free and open source VNC viewer. Its interface is not as Mac-friendly as Chicken, but it works well. If you are having problems with Chicken, try TigerVNC.
* `RealVNC Viewer <http://realvnc.com/download/viewer/>`_ is a freeware viewer, but requires registration. RealVNC also offers `RealVNC Viewer for Google Chrome <https://chrome.google.com/webstore/detail/vnc-viewer-for-google-chr/iabmpiboiopbgfabjmgeedhcmjenhbla?hl=en>`_, a free Google Chrome extension which does not require registration.
* `JollysFastVNC <http://www.jinx.de/JollysFastVNC.html>`_ is a full-featured VNC client with trial and paid versions available.
* `Chicken of the VNC <http://sourceforge.net/projects/cotvnc/>`_ is an older version of Chicken and is not recommended.

.. include:: common/filezilla-warning.rst

.. include:: common/openssh/advanced/intro.rst

On Mac OS X, configuring your system to use our SOCKS proxy is quite simple. First, open :guilabel:`System Preferences`. From here, choose :menuselection:`Network --> Advanced... --> Proxies --> SOCKS Proxy`. Under the label :guilabel:`SOCKS Proxy Server`, enter ``localhost`` and ``5555`` to match the port passed to the ``-D`` flag. This can be any port as long as these numbers match. Check the box next to :guilabel:`SOCKS Proxy`, then click :guilabel:`OK` and :guilabel:`Apply` to turn on the proxy.

.. include:: common/openssh/advanced/outro.rst
