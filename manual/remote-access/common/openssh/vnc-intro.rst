.. include:: ../common/vnc-intro.rst

To create the tunnel, use the following command line::

    ssh -L 5900:eosXX.cis.gvsu.edu:REMOTE_PORT smithj@eosXX.cis.gvsu.edu

Or the following configuration file:

.. code-block:: apacheconf

    Host eosvnc
    HostName eosXX.cis.gvsu.edu
    User smithj
    LocalForward 5900 eosXX.cis.gvsu.edu:REMOTE_PORT

If you used the configuration file, run the following to create the tunnel::

    ssh eosvnc

You are now ready to tunnel your VNC session.
