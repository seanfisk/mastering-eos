Password-less Logins
====================

It is often handy to be able to ``ssh`` into a host without having to type a password, for instance as part of a script. First, you need to generate your public/private key pairs with the command::

    ssh-keygen

Accept the default values unless you know what you are doing. Once the keys have been generated you can copy the public key over to the remote system by entering:
