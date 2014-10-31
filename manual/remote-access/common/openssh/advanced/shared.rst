Shared Connections
------------------

There is a about a minute timeout between allowed successive connnections to each individual EOS machine. This can prove very annoying when establishing multiple SSH connections to use :program:`scp` to copy files or opening multiple terminals (but see terminal multiplexing). One way to mitigate this annoyance is by using GVSU's VPN. Another way is to used SSH shared connections. These solutions are also not mutually exclusive.

Shared connections are established by creating a socket which multiplexes multiple connections. This socket is controlled by the ``ControlMaster`` and ``ControlPath`` keywords. The first connection is called the "master" and creates the socket. Subsequent connections use the already-created socket. This behavior can be automated by setting ``ControlMaster`` to the value ``auto``. ``ControlPath`` specifies the path to the socket, with variables substituted as necessary. The following config amend the previous config to add connection sharing to EOS machines.

.. code-block:: apacheconf

    # EOS
    # Match all eos01, eos11, arch08, etc.
    Host eos?? arch??
    HostName %h.cis.gvsu.edu
    User smithj
    ControlMaster auto
    #                       Host
    #                         |Port
    #                         |  | Username
    #                         V  V  V
    ControlPath /tmp/ssh_mux_%h_%p_%r

Connection sharing may be useful to enable for most hosts. However, it needs to be done with care because it typically conflicts with X forwarding and port forwarding.
