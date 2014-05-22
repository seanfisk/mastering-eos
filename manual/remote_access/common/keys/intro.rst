Password-less Logins
--------------------

It is often handy to be able to SSH into a host without having to type a password, for instance as part of a script. First, generate your public/private key pair with::

    ssh-keygen

Accept the default values by pressing :kbd:`Enter` at each prompt unless you know what you are doing. Once the keys have been generated, you can copy the public key over to the remote system by entering:
