======================
 Rules and Procedures
======================

It is important that some basic rules and procedures be established to help maintain the lab and aid in its shared use.  To those ends, please be aware of the following guidelines:


Disk Space
==========

You are given a limited amount of disk space with which to store files, which may be checked with the :command:`quota` command:

.. code-block:: console

    $ quota --human-readable
    Disk quotas for user smithj (uid 1234):
         Filesystem   space   quota   limit   grace   files   quota   limit   grace
    148.61.162.101:/home
                      8989M   9728M  10240M            303k       0       0

The output of this command is two sets of four columns. The first four refer to physical disk space, while the second four refer to the number of files. The columns have the following meanings:

+------+-------------------------------------------------+
|Column|Meaning                                          |
+======+=================================================+
|space |The amount of disk space you are currently using.|
+------+-------------------------------------------------+
|files |The number of files in your home directory.      |
+------+-------------------------------------------------+
|quota |The soft limit for space or files. You may exceed|
|      |this for the time listed in the grace period.    |
+------+-------------------------------------------------+
|limit |The hard limit for space or files. You may never |
|      |exceed this limit.                               |
+------+-------------------------------------------------+
|grace |The amount of time for which you can exceed the  |
|      |soft limit.                                      |
+------+-------------------------------------------------+

Once you exceed the hard limit or the grace period, you can no longer write new data to the filesystem. This often leads to being unable to login via a graphical session, as the desktop manager must be able to write to disk. You must then log in via a text-based console and delete files to make space.

For the previous output there is no grace period set, so the user is able to write files until reaching the hard limit. There is also no limit on the number of files the user can create, only a limit on the amount of space consumed.

Copyrighted Material
====================

Any files may be stored in your home directory. This includes games, movies, and music. However, allowing others to transfer copyrighted material may constitute a copyright infringement.

These incidents are usually caused by unintentional permissions issues or deliberate misuse of the system. Whatever the cause, copyright infringement is a violation of school policy.

These cases are taken very seriously. Your user account will be terminated immediatly upon discovering the infringement. Additionally, this offense is against our school's honor code, so you may be expelled or even face criminal proceedings.

Suffice to say, please be very careful when dealing with copyrighted materials within the EOS system. Be familiar with how permissions work, and take the time to set them correctly.

Food and Drink
==============

You are encouraged to eat and drink in the labs --- these labs were made for you and we want them to be as comfortable and useful as possible. Many restaraunts in the area deliver to the labs, including Papa John's and Jimmy John's. However, it is your responsibility to clean up after yourself. If the lab becomes too messy, policies to limit food and drinks will be instituted.

Overnight Parking
=================

Even if you have a parking pass, it is still neccessary to obtain a special permit to park overnight. These permits are granted by Campus Safety. Parking overnight without one of these permits can result in a ticket or towing.

Living in the Lab
=================

It should go without saying (but hasn't in the past) that you cannot live in the lab. People have been found living in the lab for brief periods of time between leases, etc. We must note that this is not only a huge safety violation but is illegal. If caught living in the lab, you will be removed and Campus Safety notified.

Malicious Activity
==================

The infrastructure provided by the EOS Labs includes very powerful tools that can be used to secure network infrastructure.  Unfortunately, these tools may also be used for malicious purposes. We provide these tools for you to learn to defend future systems it may be your job to secure. Under no circumstances should these tools be used to attack other students, machines, or entities. We do not provide these resources without reasonable oversight as to their use, and those using them illegally will be noticed and face strong consequences --- possibly including removal from the university and criminal charges.

Games
=====

We encourage playing games in the lab. However, if you are playing games and all machines are currently in use, please be polite and yield your machine to students needing to complete coursework.  Failure to do so may result in suspension of your account, or all games being removed from the system.
