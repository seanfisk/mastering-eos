=====================
 Alternative Clients
=====================

We have tried various VNC clients, but found Remmina to be the easiest to use. However, other VNC clients for GNU/Linux exist and include:

* `KRDC <http://kde.org/applications/internet/krdc/>`_ --- free and open-source, part of KDE
* `Vinagre <https://wiki.gnome.org/Apps/Vinagre>`_ --- free and open-source, part of GNOME
* `TigerVNC <http://tigervnc.org/>`_ --- command-line based, free and open-source
* `RealVNC Viewer <http://realvnc.com/download/viewer/>`_ --- free and paid versions available
* `RealVNC Viewer for Google Chrome <https://chrome.google.com/webstore/detail/vnc-viewer-for-google-chr/iabmpiboiopbgfabjmgeedhcmjenhbla?hl=en>`_ --- free Google Chrome extension

Operation of each of these applications is similar. For the host, enter in the hostname of the EOS machine to which you have logged in to using SSH. If a display is requested, enter ``0``; if a port is requested, enter ``5900`` (these mean the same thing). If the viewer offers support for multiple protocols, make sure you select "VNC".

.. include:: ../common/filezilla-warning.rst
