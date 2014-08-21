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
