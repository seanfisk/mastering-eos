.. _gnu-linux-advanced-openssh:

.. include:: ../common/openssh/advanced/intro.rst

Proxy configuration varies from distro to distro. These steps show how to configure a system-wide SOCKS proxy on Ubuntu 14.04, but other distros may be similar.

First, from the menu, select :menuselection:`System Settings --> Network --> Network Proxy`. For :guilabel:`Method`, select :guilabel:`Manual`, and under :guilabel:`Socks Host` enter ``localhost`` and ``5555``. Then click :guilabel:`Apply system wide` and enter your password to turn on the proxy. To turn off the proxy, switch :guilabel:`Method` back to :guilabel:`None` and click :guilabel:`Apply system wide`.

.. image:: /images/socks-ieee/ubuntu-socks.png
   :alt: Ubuntu SOCKS Configuration

.. include:: ../common/openssh/advanced/outro.rst
