============================
 Graphical Access (VNC/X11)
============================

.. include:: ../common/openssh/vnc-intro.rst

The recommended VNC client for OS X is Chicken_, which is free and open-source software. Visit the website to download, install as you would any other Mac OS X application, and open.

You will be prompted to create a new server. If not prompted, click :menuselection:`Connection --> Open Connection...` from the menu bar. Double click "New Server" in the list on the left and rename it to "EOS", or create a new session with the :guilabel:`+` button if none exist. Leave the :guilabel:`Host` field as ``localhost`` or fill it in if missing. Leave the :guilabel:`Display or port` field at 0 or fill it in if missing.

Chicken has had some problems with the ZRLE encoding with our server. As this can cause a premature end to your session, our recommendation is to manually disable this encoding. To do this, first click the drop-down menu next to :guilabel:`Profile`, and click :guilabel:`Edit Connection Profiles...`. The :guilabel:`Profile Manager` configuration window will open. In the bottom left, enter "EOS" into the field and click the :guilabel:`+` button. Now click the checkbox next to the ZRLE encoding to disable it for EOS sessions. Close the :guilabel:`Profile Manager` window.

Click :guilabel:`Connect` to begin your VNC session with EOS. To connect in the future, select :menuselection:`Connection --> Open Connection...` from the menu, select your EOS configuration, and click :guilabel:`Connect`.

.. note:: Although Chicken offers an option to tunnel directly through SSH, we have not had luck using this option with our setup. We recommend sticking with the traditional SSH tunnel, as it is tested and works well.

.. _Chicken: http://sourceforge.net/projects/chicken/

X Forwarding
============

Mac OS X has a high-quality X server called XQuartz_. It is based on `X.Org`_, and is partially maintained by Apple. Visit the XQuartz website to download and install the latest release.

.. _XQuartz: http://xquartz.macosforge.org/

.. include:: ../common/openssh/x-forwarding.rst

Upon establishing the connection, you should see the XQuartz app launch (it has the X.Org logo). All remote applications will be rendered within the XQuartz app.

.. include:: ../common/x-forwarding-test.rst

XQuartz will stay open even after your SSH session has ended. Feel free to quit XQuartz when you are finished using it.
