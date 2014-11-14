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
