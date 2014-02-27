==========
 Mac OS X
==========

Mac OS X comes preinstalled with OpenSSH, the most popular implementation of the SSH protocol. The client can be run from the command-line and is simply called ``ssh``.

.. include:: common/basic_openssh.rst

.. include:: common/keys_intro.rst

.. code-block:: bash

    ssh smithj@eos01.cis.gvsu.edu 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub

.. include:: common/keys_outro.rst
