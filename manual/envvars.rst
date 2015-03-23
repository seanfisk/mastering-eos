.. _env-vars:

=======================
 Environment Variables
=======================

This page contains a list of all environment variables referred to in the manual. Another list is the `Guide to Unix's Environment Variables section`_.

.. _Guide to Unix's Environment Variables section: http://en.wikibooks.org/wiki/Guide_to_Unix/Environment_Variables

.. envvar:: CPPFLAGS

   Flags given to the C pre-processor during compilation. See the `Autoconf manual on Preset Output Variables`_.

.. envvar:: EDITOR

   The command for the editor to run when a file needs editing. Can be used by crontab, :ref:`linuxbrew-section`, and various version control systems. There is no standard for how it is interpreted. Depending on the program reading it, it could be interpreted as a command-line interpreted by the shell (by likely calling :posix:`popen <functions/popen>`) or a single name or path to an editor (by likely calling the :posix:`exec family <functions/exec>`). For maxiumum portability, set the value to a name or path without spaces so that it can be utilized in both ways.

.. envvar:: INFOPATH

   The search path for manual pages readable by :cmd:`info`. See :ref:`man-info-paths` for instructions on how to set it.

.. envvar:: LD_LIBRARY_PATH

   Additional paths in which the dynamic linker should search for shared libraries. See `Russ Allbery's notes on Shared Library Search Paths`_, the `Autoconf manual on Preset Output Variables`_, and the `Wikipedia entry on rpath`_.

.. envvar:: LDFLAGS

   Flags given to the linker during compilation. See the `Autoconf manual on Preset Output Variables`_.

.. envvar:: MANPATH

   The search path for manual pages readable by :cmd:`man`. See :ref:`man-info-paths` for instructions on how to set it.

.. envvar:: PATH

   The GNU/Linux search path for executable files. See :ref:`shell-path-manip` for how to manipulate it and :ref:`user-hierarchies-path` for how to set it correctly for user-level hierarchies.

.. envvar:: PWD

   The current working directory. This variable is usually set and exported by the shell.

.. envvar:: Path

   The Windows search path for executable files.
