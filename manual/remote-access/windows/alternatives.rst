=====================
 Alternative Clients
=====================

Though PuTTY is the recommended SSH client for Windows, OpenSSH is also available. The recommended way of running OpenSSH on Windows is through Cygwin_. Cygwin is not simple to use and configure, but depending on your needs, it may provide a better SSH experience. OpenSSH is well-known as the best SSH client out there, and EOS uses OpenSSH as an SSH server as well.

.. _Cygwin: http://www.cygwin.com/

There are a plethora of alternate VNC viewers available for Windows, many based on the same original RealVNC code.

`UltraVNC <http://www.uvnc.com/>`_ and `TigerVNC <http://tigervnc.org/>`_ offer relatively simple user interfaces with an appropriate amount of configuration options. If you don't like or are having trouble with TightVNC, give UltraVNC a try.

RealVNC `Viewer <http://realvnc.com/download/viewer/>`_ and `Viewer Plus <http://www.realvnc.com/download/viewerplus/>`_ are freeware viewers, but require registration. RealVNC also offers `RealVNC Viewer for Google Chrome <https://chrome.google.com/webstore/detail/vnc-viewer-for-google-chr/iabmpiboiopbgfabjmgeedhcmjenhbla?hl=en>`_, a free Google Chrome extension which does not require registration.

Cyberduck_ is also available for Windows. Cyberduck has a more attractive and intuitive interface than WinSCP. However, unlike WinSCP, Cyberduck does not support automatic synchronization. This is important because high-quality free versions of SSHFS and rsync are not available for Windows.

.. _Cyberduck: http://cyberduck.io/

MobaXterm_ is an all-in-one solution for SSH, SCP, VNC, RDP, and more. Since it is a unified product, it provides a smoother experience than a collection of standalone applications. However, because it includes much more capability, it can be difficult to configure. It is worth a try if your time spent on EOS warrants it.

.. _MobaXterm: http://mobaxterm.mobatek.net/

.. include:: ../common/filezilla-warning.rst
