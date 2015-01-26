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
|Data Communications Lab (Datacomm Lab)      |MAK 1-1-167                   |studying networking              |
+--------------------------------------------+------------------------------+---------------------------------+
|Hardware Lab                                |MAK 1-1-105                   |studying hardware; multi-purpose |
+--------------------------------------------+------------------------------+---------------------------------+

When addressing this collections of labs, we often refer to it simply as *EOS*. Though the EOS Lab is only one of the CIS department's  computing labs, it was the original lab and other labs are largely based upon it. It is also the one most often used by the greatest variety of students.

Physical Access (Keycards)
==========================

The EOS Labs contain equipment specific to the CIS majors and are therefore closed to the general public. To access the labs, you are required to obtain a keycard. To be eligible for a keycard, you must be currently enrolled in a course which utiltizes the lab you'd like to access. After registration, visit the computing office in MAK C-2-100 to receive your card. A $25 deposit paid from your student account is charged upon receipt of the card. When the card is returned in acceptable condition, the deposit will be refunded.  Please note that once the $25 deposit has been posted to your student account you must pay the balance, otherwise you will be charged a late fee.  The late fee will not be refunded once you return the keycard.

To then gain entry to a lab to which you have been granted access, simply swipe the card at the reader next to the door to unlock it. In addition to room access, the card grants 24-hour access to Mackinac Hall. The courtyard door which is closest to the Architecture Lab possesses a reader which will open when the key is swiped. No other building doors are equipped with readers.

It is important that you do not allow anyone else to use your card. In addition, do not keep the card in your wallet, as the cards contain tiny hair-like wires that break easily when the card is flexed.

Computer Access (Credentials)
=============================

The EOS system uses separate user accounts from the general university computing infrastructure. EOS uses the same network ID given by GVSU's IT department, but authenticates against the CIS department's own :wikipedia:`LDAP <Lightweight_Directory_Access_Protocol>` server. The accounts are not interchangeable and administrators for one account cannot reset passwords for the other.

If you are registered for one or more eligible CIS courses [#eligible-cis-courses], you qualify for an EOS account. On the Friday before the semester starts, an account will be automatically created for you and a temporary password sent to your GVSU email address. To activate your account, you need to log in to the system once, either at a physical machine or :ref:`remotely using SSH <remote-access>`, and follow these steps:

* Enter your username.
* Enter the temporary password you have been given.
* If the temporary was entered correctly, you will be asked for the Current Password again. Enter the temporary password again.
* If the two temporary passwords match, you will be asked to create a new password.

Note the following rules when creating a new password:

* Your password must be at least 7 characters.
* Your password must not be based on a dictionary word.
* Your password should not be all numbers. The system will accept such a password, but it is incredibly insecure. Additionally, the system will often prevent login with such a password.

Please take the time to memorize your password! Password resets are available by contacting |the-sysadmin|_, but it often takes a day to get to it. Professors are also able to reset passwords via an SSH reset mechanism, though some are unaware of this mechanism.

.. [#eligible-cis-courses] All CIS courses except 150, 160, 162, 231, or 253. These courses do not require access.
