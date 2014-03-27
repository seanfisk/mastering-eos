=========
Databases
=========

Learning to setup and maintain a database is essential to any Computer Science curriculum.  The EOS infrastructure supports multiple database variants depending on the user's needs.  To save space and setup time database accounts are only given to those who need them for a class, a specific project, etc.  Contact your professor and the Systems Administrator if you need a database account for any reason.

MySQL
=====

MySQL is a powerful open source database.  To access it via the command-line, login to an EOS/Arch machine and enter::

    mysql -u smithj -p -h cis.gvsu.edu

This attempts to log you in with the provided username, using a password, to the host cis.gvsu.edu (our MySQL server).

Oracle
======

Oracle is a very powerful and complex enterprise quality system.  Once you have been granted access you can access it with the command::

    sqlplus smithj@orcl

Please note that when you change your password for Oracle that you must not use the ``@`` character.  Oracle will accept this but you will be unable to login.

Oracle APEX
===========

Oracle also provides the APEX system for web based database development.  An APEX account is separate from the normal Oracle account; a password for one will not work for the other.  You may login to APEX once you have been granted access by opening your web browser to the URL

http://dbserv.cis.gvsu.edu:5560/apex

You will need to provide a workspace name, username, and password.  If your username is :samp:`smithj`, a sample login would be

:Workspace: smithj_ws
:Username: smithj
:Password: \**********

Do not attempt to use the *Reset Password* feature on the APEX homepage; it has never worked properly.  If you attempt to use it you will be unable to login until a system administrator can delete and recreate your account.

MSSQL
=====

Microsoft also provides an enterprise quality database server that we provide.  Microsoft's database is called MSSQL.  We host MSSQL on the Winserv machine, and accounts are granted when needed.

SQLite
======

The SQLite system is a relational database that can exist in the personal file structure of a project.  SQLite is different from the above mentioned databases in that it does not operate as a client/server set of processes, but instead can be linked to the application being programmed.  As many databases as need be created (within storage limits) can be created by EOS users, as each database is merely a separate file on the filesystem.

Outside of a programming context, SQLite can be accessed from the commandline with::

    sqlite3

This will provide users with a command-line interface from which they can work with their database useing SQL statements.

Remote Database Connections
===========================

It is often advantageous for programmers to connect their programs to databases to do work.  There are a variety of ways to accomplish this task, and many are language specific.  It is of note though that our databases are not accessible from outside of our network due to firewall restrictions.  Programs running from within the EOS infrastructure can make connections to databases however.
