==========
 Mac OS X
==========

SSH
===

Mac OS X comes preinstalled with OpenSSH, the most popular implementation of the SSH protocol. The client can be run from the command-line and is simply called ``ssh``.

.. include:: common/openssh/connect.rst

.. include:: common/openssh/fingerprints.rst

.. include:: common/keys/intro.rst

.. code-block:: bash

    ssh smithj@eos01.cis.gvsu.edu 'umask u=rwx,go= && mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub

.. include:: common/keys/outro.rst

.. |text_editor| replace:: open -t
.. include:: common/openssh/forwarding.rst

The recommended VNC client for OS X is Chicken_, which is free and open-source software. Visit the website to download, install as you would any other Mac OS X application, and open.

You will be prompted to create a new server. If not prompted, click :menuselection:`Connection --> Open Connection...` from the menu bar. Double click "New Server" in the list on the left and rename it to "EOS", or create a new session with the :guilabel:`+` button if none exist. Leave the :guilabel:`Host` field as ``localhost`` or fill it in if missing. Leave the :guilabel:`Display or port` field at 0 or fill it in if missing.

Chicken has had some problems with the ZRLE encoding with our server. As this can cause a premature end to your session, our recommendation is to manually disable this encoding. To do this, first click the drop-down menu next to :guilabel:`Profile`, and click :guilabel:`Edit Conneciton Profiles...`. The :guilabel:`Profile Manager` configuration window will open. In the bottom left, enter "EOS" into the field and click the :guilabel:`+` button. Now click the checkbox next to the ZRLE encoding to disable it for EOS sessions. Close the :guilabel:`Profile Manager` window.

Click :guilabel:`Connect` to begin your VNC session with EOS. To connect in the future, select :menuselection:`Connection --> Open Connection...` from the menu, select your EOS configuration, and click :guilabel:`Connect`.

.. note:: Although Chicken offers an option to tunnel directly through SSH, we have not had luck using this option with our setup. We recommend sticking with the traditional SSH tunnel, as it is tested and works well.

.. _Chicken: http://sourceforge.net/projects/chicken/

Alternatives
------------

Chicken is not the only VNC viewer available for Mac OS X. Some alternatives are:

* `RealVNC <https://www.realvnc.com/products/vnc/documentation/5.0/installing-removing/macosx>`_ -- free and paid versions available
* `RealVNC Viewer for Google Chrome <https://chrome.google.com/webstore/detail/vnc-viewer-for-google-chr/iabmpiboiopbgfabjmgeedhcmjenhbla?hl=en>`_ -- free Google Chrome extension
* `JollysFastVNC <http://www.jinx.de/JollysFastVNC.html>`_ -- trial available
* `TigerVNC <http://tigervnc.org/>`_ -- free and open source, command-line connection interface only
* `Chicken of the VNC <http://sourceforge.net/projects/cotvnc/>`_ -- older version of Chicken, not recommended

.. include:: common/openssh/advanced.rst
