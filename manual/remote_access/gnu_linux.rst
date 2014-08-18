===========
 GNU/Linux
===========

.. contents::
   :local:

SSH
===

The most popular implementation of the SSH protocol on GNU/Linux is OpenSSH_. The SSH client can be run from the command-line and is simply called :program:`ssh`.

Many GNU/Linux distributions come with OpenSSH_ pre-installed. If your GNU/Linux distribution does not have it installed by default, please install it with your package manager. You should not install this software from scratch or on your own.

On Debian-based systems (Ubuntu, Linux Mint, and friends), run the following command::

    sudo apt-get install openssh-client

On Red Hat-based systems (Fedora, CentOS, RHEL, and friends), run the following command::

    sudo yum install openssh-clients

With other distributions (Arch, etc.), you are on your own.

.. _OpenSSH: http://www.openssh.com/

.. include:: common/openssh/connect.rst

.. include:: common/openssh/fingerprints.rst

.. include:: common/keys/intro.rst

::

    ssh-copy-id smithj@eos01.cis.gvsu.edu

.. include:: common/keys/outro.rst

.. |text_editor| replace:: gedit
.. _gnu-linux-ssh-tunnel:
.. include:: common/openssh/forwarding.rst

.. _gnu-linux-vnc:

There are a number of VNC clients for GNU/Linux, but the most capable and intuitive is Remmina_ (formerly tsclient_). Remmina also supports RDP, so you can use it with :ref:`Winserv <winserv-gnu-linux>`. It installed by default in Ubuntu 14.04. If it is not installed in your distribution, you should install from your package manager.

In addition, Remmina supports automatic SSH tunneling. You do not need to establish a tunnel beforehand as shown in the previous section. However, if you need a shell or otherwise want to do it that way, there is nothing stopping you as it works just as well.

To configure Remmina for VNC with automatic SSH tunneling, open Remmina and select :menuselection:`Connection --> New` to create a new connection. Under the :guilabel:`Basic` and :guilabel:`SSH` tabs, respectively, enter the following information. This configuration uses EOS10 and port 5907, but use the host of your choice and the port which matches your resolution from the previous section. Because :guilabel:`Public Key` is selected, if you have set up password-less login earlier, the login should be automatic.

.. _Remmina: http://remmina.sourceforge.net/
.. _tsclient: http://sourceforge.net/projects/tsclient/

.. image:: /images/vnc/remmina/basic.png
   :alt: Remmina Basic Tab

.. image:: /images/vnc/remmina/ssh.png
   :alt: Remmina SSH Tab

File Transfer
=============

.. include:: common/openssh/scp.rst

Alternative Clients
===================

We have tried various VNC clients, but found Remmina to be the easiest to use. However, other VNC clients for GNU/Linux exist and include:

* `KRDC <http://kde.org/applications/internet/krdc/>`_ --- free and open-source, part of KDE
* `Vinagre <https://wiki.gnome.org/Apps/Vinagre>`_ --- free and open-source, part of GNOME
* `TigerVNC <http://tigervnc.org/>`_ --- command-line based, free and open-source
* `RealVNC Viewer <http://realvnc.com/download/viewer/>`_ --- free and paid versions available
* `RealVNC Viewer for Google Chrome <https://chrome.google.com/webstore/detail/vnc-viewer-for-google-chr/iabmpiboiopbgfabjmgeedhcmjenhbla?hl=en>`_ --- free Google Chrome extension

Operation of each of these applications is similar. For the host, enter in the hostname of the EOS machine to which you have SSH'ed. If a display is requested, enter ``0``; if a port is requested, enter ``5900`` (these mean the same thing). If the viewer offers support for multiple protocols, make sure you select "VNC".

.. include:: common/filezilla_warning.rst

.. include:: common/openssh/advanced/intro.rst

Proxy configuration varies from distro to distro. These steps show how to configure a system-wide SOCKS proxy on Ubuntu 14.04, but other distros may be similar.

First, from the menu, select :menuselection:`System Settings --> Network --> Network Proxy`. For :guilabel:`Method`, select :guilabel:`Manual`, and under :guilabel:`Socks Host` enter ``localhost`` and ``5555``. Then click :guilabel:`Apply system wide` and enter your password to turn on the proxy. To turn off the proxy, switch :guilabel:`Method` back to :guilabel:`None` and click :guilabel:`Apply system wide`.

.. image:: /images/socks-ieee/ubuntu-socks.png
   :alt: Ubuntu SOCKS Configuration

.. include:: common/openssh/advanced/outro.rst
