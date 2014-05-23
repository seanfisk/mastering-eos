If you again try to access the `IEEE Xplore Digital Library`_, you should see the following:

.. image:: /images/socks-ieee/granted.png
    :alt: IEEE Xplore Accessible

You have now successfully used OpenSSH to establish a SOCKS proxy!

.. warning::

   By using a SOCKS proxy, *all* your network traffic is sent through the proxy. This has two implications:

   * Network access will likely be slower.
   * GVSU will be able to monitor your traffic as they do when you are on campus.

   Please keep this in mind when using the proxy feature.

Example
-------

For an example OpenSSH configuration file, see `Sean's SSH config`_.

.. _Sean's SSH config: https://github.com/seanfisk/dotfiles/blob/master/.ssh/config
