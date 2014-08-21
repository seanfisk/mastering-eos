===============
 File Transfer
===============

Graphical
=========

The recommend graphical client for file transfer on Mac OS X is Cyberduck_. It is quite easy to use. Download the application, install as normal, and start Cyberduck.

.. _Cyberduck: http://cyberduck.io/

Click :guilabel:`Open Connection`. From the drop-down box, select :guilabel:`SFTP (SSH File Transfer Protocol)`. Type in the EOS machine to which you'd like to connect in the :guilabel:`Server` field and fill in your username.

If you have set up :ref:`mac-ssh-keys`, click the :guilabel:`Use Public Key Authentication` checkbox and select the file :file:`id_rsa`. This is the identity file that you use to log in to EOS. If you have not set up your keys, you can still use password authentication, although this is not recommended.

If you have created a config file with hostname aliases, you may also notice Cyberduck auto-detect your configuration and fill in some information.

Your connection information should look something like this:

.. image:: /images/mac-cyberduck-conf.png
   :alt: Cyberduck Configuration

After connecting, we recommend creating a bookmark so that you can easily return. Click :menuselection:`Bookmark --> New Bookmark` to create one. You can change the nickname if you like. When you start Cyberduck again, simply click your bookmark to connect.

Most of Cyberduck's action are available through the :guilabel:`File` menu or the right-click context menu. In addition, Cyberduck has great support for dragging between it and Finder.

.. |ssh-keys| replace:: :ref:`mac-ssh-keys`
.. include:: ../common/openssh/scp.rst
