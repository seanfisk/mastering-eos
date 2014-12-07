============================
 Graphical Access (VNC/X11)
============================

.. include:: ../common/vnc-intro.rst

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

X Forwarding
============

There are a few X servers available for Windows, but the most popular is Xming_, a native Windows X server based on X.Org_. Download and install the public domain release from the `Xming release page`_. During installation, feel free to choose not to install an SSH client if you already have PuTTY installed (which you should).

First, start up the Xming server by simply opening it. Next, open PuTTY and load your EOS session.

.. _Xming: http://www.straightrunning.com/XmingNotes/
.. _Xming release page: http://sourceforge.net/projects/xming/files/Xming/6.9.0.31/

In the configuration tree to the left, expand :menuselection:`Connection --> SSH` and click on :guilabel:`X11`. Tick the checkbox labeled :guilabel:`Enable X11 forwarding`. You may open the session immediately or go back to the :guilabel:`Session` screen to save a session with X forwarding automatically enabled.

.. include:: ../common/x-forwarding-test.rst

Xming will stay open even after your PuTTY session has ended. Feel free to quit Xming from the system tray when you are finished using it.

Another alternative X server for Windows is `Cygwin/X`_, Cygwin's X server.

.. _Cygwin/X: http://x.cygwin.com/
