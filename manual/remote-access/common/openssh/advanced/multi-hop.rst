Multi-Hop Connections
---------------------

Oftentimes a machine is only available when SSH'ing into another machine. For example, this is the case with the DEN's Okami server, used in CIS 677 High-Performance Computing. In addition, Okami's SSH server is only available on a non-standard port. This typically results in the user going through this process:

.. code-block:: console

    smithj@local$ ssh smithj@eos01.cis.gvsu.edu
    smithj@eos01$ ssh -p 43022 okami
    smithj@okami$ # Finally here!

This is annoying and unnecessary. By using the ``ProxyCommand`` keyword in our config file, we can automate this process:

.. code-block:: apacheconf

    # DEN Okami
    Host okami
    User smithj
    Port 43022
    ProxyCommand ssh eos01 -W %h:%p

.. We use the standard rST syntax `My Section`_ instead of :ref:`My Section` here because we *want* to link only within this document. Otherwise Sphinx yells at us because the file is included multiple times and the label is therefore duplicated. See here <http://sphinx-doc.org/markup/inline.html#role-ref>.

The ``-W`` flag allows us to hop through the first host to the host and port specified by the variables (``okami:43022``). Note that the use of ``eos01`` here requires presence of the aliases set up in `Hostname Aliases`_.

The process has now been simplified to:

.. code-block:: console

    smithj@local$ ssh okami
    smithj@okami$ # Yay! Easy!
