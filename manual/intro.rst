==============
 Introduction
==============

The Exploratory Operating Systems Labs (EOS Labs) are a collection of computer labs maintained by the GVSU School of Computing and Information Systems. Some are for general CIS student use, and others are specific to certain courses, labs, or applications. The labs within the EOS Lab umbrella include:

+--------------------------------------------+------------------------------+---------------------------------+
|Name                                        |Location                      |Purpose                          |
+============================================+==============================+=================================+
|Exploratory Operating Systems Lab (EOS Lab) |MAK A-1-171                   |studying operating systems;      |
|                                            |                              |general CIS computing use        |
+--------------------------------------------+------------------------------+---------------------------------+
|Architecture Lab (Arch Lab)                 |MAK A-1-101                   |studying computer architectures; |
|                                            |                              |general CIS computing use        |
+--------------------------------------------+------------------------------+---------------------------------+
|Data Communications Lab (Datacom Lab)       |MAK 1-1-167                   |studying networking              |
+--------------------------------------------+------------------------------+---------------------------------+
|Hardware Lab                                |MAK 1-1-105                   |studying hardware; multi-purpose |
+--------------------------------------------+------------------------------+---------------------------------+

When addressing this collections of labs, we often refer to it simply as *EOS*. Though the EOS Lab is only one of our specialized computing labs, it was the original custom lab and the other labs are largely based upon it. It is also the one most often used by the greatest variety of students.

Physical Access (Keycards)
==========================

The EOS Labs are highly-specialized labs paid for and maintained with department resources. These machines are not for the general computing public. Students are therefore required to obtain a keycard before they can gain access to the labs. To obtain a keycard, students must

- be currently enrolled in a course which utiltizes the lab they would like to access
- visit the computing office in MAK C-2-100
- pay a $25 deposit that is refunded to the student when the card is returned

We charge a deposit on the cards because they are costly for us to purchase and we need to ensure they will be returned in acceptable condition. The $25 deposit is charged to the student's account, so no money actually changes hands. A refund of $25 will be placed on the student's account when the card is returned.

The keycard will allow students access to the EOS and Architecture Labs. In addition, the card grants the holder 24-hour access to Mackinac Hall. The courtyard door which is closest to the Architecture Lab possesses a card reader similar to the lab readers which will open when the key is swiped. No other building doors are equipped with readers.

It is important that students

- do not allow anyone else to use their card
- do not keep the card in their wallet, as the cards contain tiny hair-like wires that break easily

Computer Access (Credentials)
=============================

The EOS system uses separate user accounts from the general university computing infrastructure. EOS uses the same network ID given by GVSU's IT department, but authenticates against the CIS department's own LDAP_ server. The accounts are not interchangeable and administrators for one account cannot reset passwords for the other.

.. _LDAP: http://en.wikipedia.org/wiki/LDAP

At the beginning of each term, a report is compiled of all students who have CIS classes [#cis_classes]_. Accounts for these students are automatically generated on the last Friday before classes start, and emails are sent with temporary passwords. Students need to login to the system once, either locally at a terminal or remotely using SSH, and follow these steps:

* Enter your username.
* Enter the temporary password you have been given.
* If the temporary was entered correctly, the system will ask for the Current Password again. Enter the temporary password again.
* If the two temporary passwords match, the system will ask for a new password.

Note the following rules when creating a new password:

* Passwords must be at least 7 characters.
* Password must not be based on a dictionary word.
* Passwords should not be all numbers. The system will accept such a password, but it is incredibly insecure. Additionally, the system will often prevent login with such a password.

Please take the time to memorize your password! Password resets are available by contacting |the_sysadmin|, but it often takes a day to get to it. Professors are also able to reset passwords via an SSH reset mechanism, though some are unaware of this mechanism.

.. [#cis_classes] All students except those in CIS 150, 160, 162, 231, or 253. Students in these classes should not need access to the system.
