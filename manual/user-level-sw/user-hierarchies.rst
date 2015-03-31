.. highlight:: console

.. _user-hierarchies:

========================
 User-level Hierarchies
========================

To use programs in a user-level hierarchy effectively, certain environment variables must be manipulated. This section shows how to accomplish this for a well-functioning environment.

.. warning::

   The examples in this section assume you have followed through extraction, compilation, and installation of the GNU Bash example in :ref:`manual-install`.

.. _user-hierarchies-path:

Executable Path
===============

You can always use executables installed to your home directory by typing the full path to the executable, for example::

   $ ~/.local/bin/bash --version
   GNU bash, version 4.3.0(1)-release (x86_64-unknown-linux-gnu)
   Copyright (C) 2013 Free Software Foundation, Inc.
   License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

   This is free software; you are free to change and redistribute it.
   There is NO WARRANTY, to the extent permitted by law.

For obvious reasons, typing the full path can get tedious if you are using the executable frequently. In addition, other utilities may assume that the executable in question is available on the :envvar:`PATH` and not in a custom prefix. If you are installing an executable that is already present on the system, there is yet another consideration --- you may want to override the system version with the version that you installed to your home directory. This is typically useful if you would like to use a newer version of a program than one installed to a system hierarchy.

Begin by reading :ref:`shell-path-manip` to learn how to effectively manipulate the executable path. Then, add the following line to your :file:`.bash_profile`:

.. code-block:: bash

   export PATH=~/.local/bin:$PATH

This line prepends the path of your locally-installed executables to the executable search path. Your executable will now not only be accessible without typing the full path, but it will also override any executables of the same name in system hierarchies.

Follow the directions for your session for :ref:`shell-startup-apply`. After this, the following should yield::

   $ command which bash
   ~/.local/bin/bash

Now you should be able to simply type::

   $ bash

to start the GNU Bash installed to your home directory!

.. _man-info-paths:

Man and Info Paths
==================

Although you are now able to run your new Bash without typing the full path, the commands::

   $ man bash
   $ info bash

still show the Bash documentation for the system Bash. Although this may not seem like a big deal, small changes between versions of the same program can be the difference between a working and non-working script. Locally-installed, version-correct documentation helps avoid this problem. To allow :cmd:`man` and :cmd:`info` to find the locally-installed documentation, add the following lines to your :file:`~/.bash_profile`:

.. code-block:: bash

   export MANPATH=~/.local/share/man:~/.local/man:$MANPATH
   export INFOPATH=~/.local/share/info:$INFOPATH

There is unfortunately some inconsistency with the location of installed man pages, which why we added both directories to the :envvar:`MANPATH`. :envvar:`INFOPATH` does not have these problems.

Follow the directions for your session for :ref:`shell-startup-apply`. After this, the commands at the beginning of this section should bring up the correct documentation.

Managing Paths
==============

Although the previous ``export`` commands work fine, there is a lot of repetition, especially if you would like to use :ref:`linuxbrew-section` as well. In this case, the following snippet from the :ref:`shell-example-files` is recommended as a replacement:

.. literalinclude:: ../shell/profile.bash
   :language: bash
   :lines: 9-35
