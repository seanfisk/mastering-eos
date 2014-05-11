Tunnelling / Port Forwarding
----------------------------

The SSH protocol possesses a special feature which allows it to tunnel other protocols within itself. This is called tunnelling or port forwarding. SSH can forward local ports (allowing the local machine access to resources on the remote machine) and remote ports (allowing the remote machine access to resources on the local machine). Port forwarding can be accomplished by passing arguments to the OpenSSH command-line client or editing the OpenSSH client configuration file.

Local port forwarding is the more used feature, and is explained in the following sections. Remote port forwarding is similar but is outside the scope of this guide.

Forwarding on the Command Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Forwarding local ports on the command-line can be accomplished using the following syntax::

    ssh -L local_port:remote_host:remote_port user@host

For example, to access a web server running on port 8000 on ``eos01.cis.gvsu.edu`` from your machine on port 5555, use the following command line::

    ssh -L 5555:eos01.cis.gvsu.edu:8000 smithj@eos01.cis.gvsu.edu

You can actually test this by running this in the SSH prompt::

    python -m SimpleHTTPServer

and opening http://localhost:5555/ in your local web browser.

The remote host which is hosting the resource need not be the EOS machine to which you are connecting with SSH. For example, to access the CIS web server through your SSH tunnel, you can run::

    ssh -L 5678:cis.gvsu.edu:80 smithj@eos01.cis.gvsu.edu

and visit http://localhost:5678/ in your local web browser. The CIS home page should appear!

Forwarding in the Config File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The command-line works well for one-off tunnels, but for frequently established tunnels, it pays to alter the OpenSSH client configuration file. The OpenSSH client configuration resides on your local machine in the file :file:`~/.ssh/config`. This is a file inside a hidden directory inside your home directory. The easiest way to open this file, creating it if it doesn't exist, is to run:

.. highlight:: bash
.. parsed-literal::

    umask u=rwx,go= && mkdir -p ~/.ssh && touch ~/.ssh/config && |text_editor| ~/.ssh/config

To establish the CIS web server forwarding shown in the last section, one could use the following configuration:

.. The OpenSSH config has a similar format to the Apache config, so syntax highlighting works quite well!
.. code-block:: apacheconf

    Host eoscisweb
    HostName eos01.cis.gvsu.edu
    User smithj
    LocalForward 5678 cis.gvsu.edu:80

To use this host from the command line, simply type::

    ssh eoscisweb

VNC
===

First, we need to create a tunnel in order to forward VNC through our SSH connection. The remote port to which we must connect depends on the desired resolution of the remote desktop. Select a desired resolution from the following table, and note the port to which it corresponds.

.. include :: common/vnc_port_geometry_table.rst

Replace ``REMOTE_PORT`` with the port that you have selected in the following command or file.

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
