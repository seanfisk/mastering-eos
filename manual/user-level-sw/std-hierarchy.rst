.. _std-hierarchy:

========================
 The Standard Hierarchy
========================

Before installing software on your own, it is important to understand the concept of the standard hierarchy. The standard hierarchy is a way of organizing files on the filesystem such that it may be used cohesively by multiple programs. If you are a Windows or Mac OS X user, you may be used to programs having their own subdirectories of :file:`C:\\Program Files` or :file:`/Applications`, respectively. However, UNIX-like machines do not typically work in this way, electing instead to separate installed files by type or purpose.

The root hierarchy, :file:`/`, is the directory which contains all other files. Files which are absolutely essential to the system's operation may be installed here. The primary hierarchy for programs used by a typical user is the :file:`/usr` hierarchy. Both these hierarchies can contain each of the following directories:

+----------------------+------------------------------------------------------------------------------------------+
|Name                  |Purpose                                                                                   |
+======================+==========================================================================================+
|``bin``               |Program executable files; *bin* stands for *binary* which is another name for *executable*|
+----------------------+------------------------------------------------------------------------------------------+
|``sbin``              |Programs used for system administration                                                   |
+----------------------+------------------------------------------------------------------------------------------+
|``include``           |Include files (headers) for the C programming language                                    |
+----------------------+------------------------------------------------------------------------------------------+
|``lib``               |Shared libraries, which frequently correspond to headers in the ``include`` directory     |
+----------------------+------------------------------------------------------------------------------------------+
|``etc``               |Configuration files [#etc]_                                                               |
+----------------------+------------------------------------------------------------------------------------------+
|``src``               |Source code for programs installed to said hierarchy                                      |
+----------------------+------------------------------------------------------------------------------------------+
|``man``, ``share/man``|Manual pages for programs installed to said hierarchy                                     |
+----------------------+------------------------------------------------------------------------------------------+
|``share/info``        |Info documentation for programs installed to said hierarchy                               |
+----------------------+------------------------------------------------------------------------------------------+

Although there are more directories which can be present in each hierarchy, these directories are the most important ones with which to be familiar.

For more information on the standard hierarchy, please see the very well-written `Filesystem Hierarchy Standard`_, which is the source of most of this information.

.. _Filesystem Hierarchy Standard: http://www.pathname.com/fhs/
.. [#etc] Unlike most hierarchy directories which contain files related to other files in their hierarchy, configuration files in :file:`/etc` are usually used to configure programs in many different hierarchies. Software configuration is a complex beast --- consult each specific piece of software's documentation for the exact files used for configuration.

Files in the root and :file:`/usr` hierarchies are usually readable but not writable by ordinary users. Ordinary users typically only have one directory to where persistent data can be written: their home directory. This is typically :samp:`/home/{username}`. As such, this is the place where a user installs their own programs. Although the system hierarchies cannot be written by a standard user, the structure of these system hierarchies is typically mirrored by hierarchies created in a user's home directory.

.. tip::

   A hierarchy is not a special directory, simply a sane way of organizing files. It can be created by a build system like :ref:`cmake-section` or :ref:`autotools-section`, a package manager like :ref:`linuxbrew-section`, or manually on your own!

Programs typically look in the system hierarchies for programs, headers, libraries, configuration files, and other data files which they may use or need. Special considerations usually need to be applied in order to make programs compile and run correctly from a user's home directory.

After installing programs to a user-level hierarchy, follow the directions in :ref:`user-hierarchies` in order to correctly use them.
