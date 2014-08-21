.. include:: ../common/openssh/advanced/intro.rst

On Mac OS X, configuring your system to use our SOCKS proxy is quite simple. First, open :guilabel:`System Preferences`. From here, choose :menuselection:`Network --> Advanced... --> Proxies --> SOCKS Proxy`. Under the label :guilabel:`SOCKS Proxy Server`, enter ``localhost`` and ``5555`` to match the port passed to the ``-D`` flag. This can be any port as long as these numbers match. Check the box next to :guilabel:`SOCKS Proxy`, then click :guilabel:`OK` and :guilabel:`Apply` to turn on the proxy.

.. include:: ../common/openssh/advanced/outro.rst
