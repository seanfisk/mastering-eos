Advanced OpenSSH
================

OpenSSH can do much more than simply allow the user to establish connections with remote servers. If you use OpenSSH, there are a great many neat tricks available to you.

This section is based in large part on the `Smylers SSH Productivity Tips blog post`_. Please visit this post for *even more SSH awesomeness!*

.. _Smylers SSH Productivity Tips blog post: http://blogs.perl.org/users/smylers/2011/08/ssh-productivity-tips.html

Hostname Aliases
----------------

It's useful not to have to type out the entire full-qualified domain names to EOS machines. What you might normally type would be something like this::

    ssh smithj@eos02.cis.gvsu.edu
    # or
    ssh smithj@arch04.cis.gvsu.edu

By adding a section to the config file, this becomes easier. Add this to your :file:`~/.ssh/config` as mentioned earlier:

.. code-block:: apacheconf

    # EOS
    # Match all eos01, eos11, arch08, etc.
    Host eos?? arch??
    HostName %h.cis.gvsu.edu
    User smithj

With this, now you need only type::

    ssh eos02
    # or
    ssh arch04

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

Persistent Connections
----------------------

It is often useful to keep connections open in the background even after the terminal has actually been closed. This is useful as it allows OpenSSH to reconnect to the server without re-establishing a connection. Turning this behavior on is trivially simple. Add the following line under the host for which you would like connections to persist:

.. code-block:: apacheconf

    # Persist connections for 2 hours.
    ControlPersist 2h

For GitHub users, this is especially useful when using Git over SSH. Within this period, OpenSSH does not need to re-establish a connection to the Git server, which makes pushes and pulls much faster.

Multi-Hop Connections
---------------------

Oftentimes a machine is only available when SSH'ing into another machine. For example, this is the case with the DEN's Okami server, used in CIS 677 High-Performance Computing. In addition, Okami's SSH server is only available on a non-standard port. This typically results in the user going through this process::

    local$ ssh smithj@eos01.cis.gvsu.edu
    eos01$ ssh -p 43022 okami
    okami$ # Finally here!

This is annoying and unnecessary. By using the ``ProxyCommand`` keyword in our config file, we can automate this process:

.. code-block:: apacheconf

    # DEN Okami
    Host okami
    User smithj
    Port 43022
    ProxyCommand ssh eos01 -W %h:%p

.. We use the standard rST syntax `Section`_ instead of :ref:`Section` here because we *want* to link only within this document. Otherwise Sphinx yells at us because the file is included multiple times and the label is therefore duplicated. See here <http://sphinx-doc.org/markup/inline.html#role-ref>.

The ``-W`` flag allows us to hop through the first host to the host and port specified by the variables (``okami:43022``). Note that the use of ``eos01`` here requires presence of the aliases set up in `Hostname Aliases`_.

The process has now been simplified to::

    local$ ssh okami
    okami$ # Yay! Easy!

Using SSH as a Proxy
--------------------

It is also possible to use SSH as a proxy for all network traffic. This can be useful if there are resources available from the SSH server that are not available from the local machine.

An example of such a resource is the `IEEE Xplore Digital Library`_, which contains technical articles targeted at computer scientists and engineers. GVSU subscribes to this library, but access to the subscription is only available while *on campus*. If you try to access it off campus, you will see the following:

.. _IEEE Xplore Digital Library: http://ieeexplore.ieee.org/

.. image:: /images/socks-ieee/denied.png
   :alt: IEEE Xplore Login Page

By using a proxy through the EOS machines, we can transparently access the IEEE library as if we were on campus.

OpenSSH support the SOCKS protocol for proxying. Activating the SOCKS feature is accomplished with the ``-D`` flag like so::

    ssh -D 5555 eos01

This establishes a SOCKS proxy with EOS01 served up on the local machine on port 5555. Now we must configure our operating system or browser to use this proxy.
