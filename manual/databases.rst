=========
Databases
=========

Learning to setup and maintain a database is essential to any Computer Science curriculum.  The EOS infrastructure supports multiple database variants depending on the user's needs.  To save space and setup time database accounts are only given to those who need them for a class, a specific project, etc.  Contact your professor and the Systems Administrator if you need a database account for any reason.

MySQL
=====

MySQL is a powerful open source database.  To access it via the command-line, login to an EOS/Arch machine and enter

``mysql -u <USERNAME> -p -h cis.gvsu.edu``

This attempts to log you in with the provided username, using a password, to the host cis.gvsu.edu (our MySQL server).

Oracle
======

Oracle is a very powerful and complex enterprise quality system.  Once you have been granted access you can access it with the command

``sqlplus <USERNAME>@orcl``

Please note that when you change your password for Oracle that you must not use the ``@`` character.  Oracle will accept this but you will be unable to login.

Oracle APEX
===========

Oracle also provides the APEX system for web based database development.  An APEX account is separate from the normal Oracle account; a password for one will not work for the other.  You may login to APEX once you have been granted access by opening your web browser to the URL

http://dbserv.cis.gvsu.edu:5560/apex

You will need to provide a workspace name, username, and password.  If your username is doej a sample login would use

Workspace:  ``doej_ws``
Username:   ``doesj``
Password:   ``**********``

Do not attempt to use the 'Reset Password' feature on the APEX homepage; it has never worked properly.  If you attempt to use it you will be unable to login until a Systems Administrator can delete and recreate your account.
