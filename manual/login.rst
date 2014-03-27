============================
Logging in to the EOS System
============================

The EOS system uses separate user accounts than the general university computing infrastructure.  The system uses the same network ID given by Grand Valley's IT but authenticates against CIS's own LDAP server.  The accounts are not interchangeable and administrators for one account cannot reset passwords for the other.

How to get a login
==================

At the beginning of each term a report is compiled of all students who have CIS classes [#one]_.  Accounts for these students are automatically generated on the last Friday before classes start, and emails are sent with temporary passwords.  Students need to login once to the system, either locally at a terminal or remotely using SSH and do the following:

* Enter username
* Enter temporary password
* If the temporary was entered correctly the system will ask for the Current Password again.  Enter the temporary again.
* If the two temporary passwords match, the system will ask for a new password.  Note the following rules:
    * Passwords must be at least 7 characters
    * They must not be based on a dictionary word
    * They should not be all numbers (the system will take such a password, but it is incredibly insecure.  Additionally, the system will often not let you login with it).

Please take the time to memorize your password!  Password resets are available by contacting Ira Woodring, but it often takes a day for Ira to get to it. Professors are also able to reset passwords via a SSH reset mechanism, though some remain unaware of this fact.

.. [#one] All students except those in CIS 150, 160, 162, 231, or 253.  Students in these classes should not need the system.
