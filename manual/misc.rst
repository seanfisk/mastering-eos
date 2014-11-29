=============
Miscellaneous
=============

This section contains tips that are useful but are not at home in the other sections.

Kill the X Server
=================

If another user has a session on a computer you would like to use, it is possible to log them out and return to the login screen. The key combination :kbd:`Control-Alt-Backspace` kills the :wikipedia:`X server <X_Window_System>`, which ends the current user's desktop session. This is also useful should your session crash or freeze.

.. warning::

    Be advised that any of the current user's unsaved data will be lost.

Directory Navigation
====================

These tools help you navigate directories quickly.

pushd
-----

The command :samp:`pushd {dir}` will save your current directory on the stack and move you to ``dir``.

popd
----

After you have used ``pushd`` and stored one or more directories on the stack, you can use ``popd`` to move back to your previous directory.

dirs
----

``dirs`` allows you to see what directories you have stored on the stack. The far left directory is the most recently saved. Another way to view the directory from most recent to least recent is by using the commmand ``dirs -v``.

Uptime
======

The command ``uptime`` will display the following information in one line: the current time, the amount of time the system has been running, the number of users currently logged in, and system load averages for the past 1, 5, and 15 minutes.

User Interactions
=================

w
-

The ``w`` command provides a summary of the current users on the machine. The header displays the same information as the ``uptime`` command.

last
----

``last`` displays all the users that have logged into the machine since the creation of the wtemp log file. The date and time that file was created is shown at the bottom of the output.

To show the output without the hostname field::

	last -R

To limit the number of rows to output use::

	last -num

For more information and options run::

	man last

users
-----

``users`` prints a list of all the users currently logged in to a host.

write
-----

The ``write`` command allows communication with other users through the terminal.

The usual syntax is::

	write user [tty]
