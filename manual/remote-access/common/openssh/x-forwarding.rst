The :cmd:`ssh` program needs to be told to initiate X forwarding when the connection is started. This can be done with the ``-X`` command-line flag::

   ssh -X smithj@eosXX.cis.gvsu.edu

This can also be accomplished in the SSH configuration file:

.. code-block:: apacheconf

   Host eosx
   HostName eos01.cis.gvsu.edu
   User smithj
   ForwardX11 yes
