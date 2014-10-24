===============
 File Transfer
===============

Graphical
=========

GNOME
-----

The GNOME desktop features the `GNOME Virtual Filesystem`_ (GVFS), which has native support for SFTP. First, start up the file manager (:wikipedia:`GNOME Files <GNOME_Files>`, formerly known as Nautilus). On the left pane, click :menuselection:`Network ---> Connect to Server`. In the :guilabel:`Server Address` field, enter :samp:`sftp://{smithj}@eos01.cis.gvsu.edu`. Your files on EOS should be displayed.

.. _GNOME Virtual Filesystem: https://wiki.gnome.org/action/show/Projects/gvfs

If you need to access these files from the command line, you can find your EOS account mounted as a subdirectory of this directory::

    ls $XDG_RUNTIME_DIR/gvfs

KDE
---

KDE's file manager, Dolphin_, also support SFTP URLs. First, click :menuselection:`Places ---> Network` in the pane on the left. Then, click :guilabel:`Add Network Folder`. Select :guilabel:`Secure shell (ssh)` as the type and click :guilabel:`Next`. Fill out the form as follows, then click :guilabel:`Save & Connect`:

.. image:: /images/kde-file-transfer.png
    :alt: SSH file transfer with KDE Dolphin

Both the SFTP and FISH protocols *should* work, although we have had the most luck with the FISH protocol.

.. _Dolphin: https://www.kde.org/applications/system/dolphin/

Other Desktop Managers
----------------------

With desktop managers besides GNOME and KDE, you are on your own. However, many GNU/Linux file managers are very similar, and most offer support for SSH file transfer. Consult your desktop's document for more information, or just try to figure it out on your own.

.. |ssh-keys| replace:: :ref:`gnu-linux-ssh-keys`
.. include:: ../common/openssh/scp.rst
