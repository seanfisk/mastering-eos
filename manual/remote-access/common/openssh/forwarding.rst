.. include:: common/forwarding-intro.rst

Port forwarding can be accomplished with OpenSSH by passing arguments to the command-line client or by editing the client configuration file.

Forwarding on the Command Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Forwarding local ports on the command-line can be accomplished using the following syntax::

    ssh -L local_port:remote_host:remote_port user@host

For example, to access a web server running on port 8000 on ``eos01.cis.gvsu.edu`` from your machine on port 5555, use the following command line::

    ssh -L 5555:eos01.cis.gvsu.edu:8000 smithj@eos01.cis.gvsu.edu

You can test the forwarding by running this in the SSH prompt::

    python -m SimpleHTTPServer

and opening http://localhost:5555/ in your local web browser. You should see a web listing of your home directory! Press :kbd:`Control-C` to kill the web server.

The remote host which is hosting the resource need not be the EOS machine to which you are connecting with SSH. For example, to access the CIS web server through your SSH tunnel, you can run::

    ssh -L 5678:cis.gvsu.edu:80 smithj@eos01.cis.gvsu.edu

and visit http://localhost:5678/ in your local web browser. The CIS home page should appear!

Forwarding in the Config File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The command-line works well for one-off tunnels, but for frequently established tunnels, it pays to alter the OpenSSH client configuration file. The OpenSSH client configuration resides on your local machine in the file :file:`~/.ssh/config`. This is a file inside a hidden directory inside your home directory. The easiest way to open this file, creating it if it doesn't exist, is to run:

.. parsed-literal::

    umask u=rwx,go= && mkdir -p ~/.ssh && touch ~/.ssh/config && |text-editor| ~/.ssh/config

To establish the CIS web server forwarding shown in the last section, one could use the following configuration:

.. The OpenSSH config has a similar format to the Apache config, so syntax highlighting works quite well!
.. code-block:: apacheconf

    Host eoscisweb
    HostName eos01.cis.gvsu.edu
    User smithj
    LocalForward 5678 cis.gvsu.edu:80

To use this host from the command line, simply type::

    ssh eoscisweb

.. include:: common/vnc-intro.rst

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
