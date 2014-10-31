Hostname Aliases
----------------

It's useful not to have to type out the entire full-qualified domain names to EOS machines. What you might normally type would be something like this::

    ssh smithj@eos02.cis.gvsu.edu
    # or
    ssh smithj@arch04.cis.gvsu.edu

By adding a section to the config file, this becomes easier. Add this to your :file:`~/.ssh/config` as mentioned earlier:

.. code-block:: apacheconf

    # EOS
    # Match all eos01, eos11, arch08, etc.
    Host eos?? arch??
    HostName %h.cis.gvsu.edu
    User smithj

With this, now you need only type::

    ssh eos02
    # or
    ssh arch04
