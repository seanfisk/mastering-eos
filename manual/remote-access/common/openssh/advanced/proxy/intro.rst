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
