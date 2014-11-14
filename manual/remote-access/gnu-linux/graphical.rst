============================
 Graphical Access (VNC/X11)
============================

.. _linux-vnc:

.. include:: ../common/openssh/vnc-intro.rst

There are a number of VNC clients for GNU/Linux, but the most capable and intuitive is Remmina_ (formerly tsclient_). Remmina also supports RDP, so you can use it with :ref:`Winserv <winserv-gnu-linux>`. It installed by default in Ubuntu 14.04. If it is not installed in your distribution, you should install from your package manager.

In addition, Remmina supports automatic SSH tunneling. You do not need to establish a tunnel beforehand as shown in the previous section. However, if you need a shell or otherwise want to do it that way, there is nothing stopping you as it works just as well.

To configure Remmina for VNC with automatic SSH tunneling, open Remmina and select :menuselection:`Connection --> New` to create a new connection. Under the :guilabel:`Basic` and :guilabel:`SSH` tabs, respectively, enter the following information. This configuration uses EOS10 and port 5907, but use the host of your choice and the port which matches your resolution from the previous section. Because :guilabel:`Public Key` is selected, if you have set up password-less login earlier, the login should be automatic.

.. _Remmina: http://remmina.sourceforge.net/
.. _tsclient: http://sourceforge.net/projects/tsclient/

.. image:: /images/vnc/remmina/basic.png
   :alt: Remmina Basic Tab

.. image:: /images/vnc/remmina/ssh.png
   :alt: Remmina SSH Tab

X Forwarding
============

Almost all GNU/Linux distributions come pre-installed with a fully functional X server (typically `X.Org`_), so no installation is needed.

.. include:: ../common/openssh/x-forwarding.rst

.. include:: ../common/x-forwarding-test.rst
