===============
 Inter-EOS SSH
===============

EOS Lab machines are installed with OpenSSH, the most popular implementation of the SSH protocol. Because EOS machines run GNU/Linux, please read the :ref:`GNU/Linux Remote Access <remote-access-gnu-linux>` section for details.

Additional information specific to EOS follows.

.. _inter-eos-trust:

Trust All EOS Machines
======================

For certain tasks (e.g., :wikipedia:`MPI <Message_Passing_Interface>` for HPC, :ref:`contributing`, or just plain utility) it can be useful to SSH into any EOS machine from any other EOS machine without a password. To accomplish this, follow the commands in this script. You do not need to run :cmd:`ssh-keygen` if you have done so before:

.. literalinclude:: ../../common/inter-eos-ssh.bash

.. note::

    These commands temporarily disable ``StrictHostKeyChecking``, which refers to the showing of :ref:`this confirmation prompt <linux-fingerprints>`. Since we are operating within the EOS network, this is probably OK.
