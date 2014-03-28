When you SSH into EOS now, you should be able to do so without having to provide a password::

    ssh smithj@eos01.cis.gvsu.edu

.. note::

    In this setup, we created our public/private key pair without a passphrase, which is less secure. If you would like to use a passphrase, please see `Mark Hershberger's excellent guide to ssh-agent`_ and `Github's guide to SSH passphrases`_.

.. _Mark Hershberger's excellent guide to ssh-agent: http://mah.everybody.org/docs/ssh
.. _Github's guide to SSH passphrases: https://help.github.com/articles/working-with-ssh-key-passphrases#platform-mac
