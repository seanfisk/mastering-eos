==============================
 Accessing EOS Remotely (SSH)
==============================

If you are not sitting in the EOS or Arch lab, EOS can be accessed from home using a protocol called Secure Shell (SSH). SSH allows you to remotely run commands on any EOS machine.

The hostnames for the EOS machines are organized as follows: :samp:`eos{XX}.cis.gvsu.edu` where :samp:`{XX}` is 01 through 24 and :samp:`arch{XX}.cis.gvsu.edu` where :samp:`{XX}` is 01 through 10. Use these names to connect to a specific EOS machine.

Your SSH client of choice depends on your machine's operating system.

.. toctree::
   :maxdepth: 1

   windows
   mac_os_x
   gnu_linux


Checking Host Fingerprints
==========================

When logging in to an EOS machine for the first time, you will see a message like this on Mac OS X and GNU/Linux::

    The authenticity of host 'eos01.cis.gvsu.edu (148.61.162.101)' can't be established.
    RSA key fingerprint is 6d:29:fd:23:c5:26:c7:c9:a5:6e:6e:c2:34:60:ea:54.
    Are you sure you want to continue connecting (yes/no)?

or a dialog like this on Windows:

.. image:: /_static/putty-security-alert.png
    :alt: PuTTY Security Alert

This is your SSH client requesting you to validate the identity of the machine to which you are connecting.

Each EOS machine has a so-called fingerprint, a series of characters which is used to verify its identity. To ensure that an attacker between your client and the actual EOS machine is not pretending to be an EOS machine, you must check that the machine's fingerprint matches the table below. Please report any mismatches to the system administrator immediately.

.. include:: common/fingerprints.rst
