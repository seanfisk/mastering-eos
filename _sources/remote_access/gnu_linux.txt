===========
 GNU/Linux
===========

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
.. include:: common/openssh/forwarding.rst

.. _gnu-linux-vnc:

There are a number of capable VNC clients for GNU/Linux. Which one you choose depends on desktop environment and personal preference. For KDE, KRDC_ (KDE Remote Desktop Client) is the standard application. For GNOME, the standard remote desktop viewer is called Vinagre_. If you would also like to use :ref:`RDP with Winserv <gnu-linux-rdp>`, you may want to try Reminna_, a third-party free and open-source remote desktop viewer. You should install these from your package manager.

TigerVNC_ and `RealVNC Viewer`_ are also available for GNU/Linux. RealVNC also offers `RealVNC Viewer for Google Chrome`_, a free viewer which runs inside the Google Chrome browser.

Operation of each of these applications is similar. For the host, enter in the hostname of the EOS machine to which you have SSH'ed. If a display is requested, enter ``0``. If a port is requested, enter ``5900`` (these mean the same thing). If the viewer offers support for multiple protocols, make sure you select "VNC".

.. _KRDC: http://kde.org/applications/internet/krdc/
.. _Vinagre: https://wiki.gnome.org/Apps/Vinagre
.. _Reminna: http://remmina.sourceforge.net/
.. _TigerVNC: http://tigervnc.org/
.. _RealVNC Viewer: http://realvnc.com/download/viewer/
.. _RealVNC Viewer for Google Chrome: https://chrome.google.com/webstore/detail/vnc-viewer-for-google-chr/iabmpiboiopbgfabjmgeedhcmjenhbla?hl=en

.. include:: common/openssh/advanced/intro.rst

**TODO: Add configuration for GNU/Linux.**

.. include:: common/openssh/advanced/outro.rst
