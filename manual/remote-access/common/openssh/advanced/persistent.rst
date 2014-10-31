Persistent Connections
----------------------

It is often useful to keep connections open in the background even after the terminal has actually been closed. This is useful as it allows OpenSSH to reconnect to the server without re-establishing a connection. Turning this behavior on is trivially simple. Add the following line under the host for which you would like connections to persist:

.. code-block:: apacheconf

    # Persist connections for 2 hours.
    ControlPersist 2h

For GitHub users, this is especially useful when using Git over SSH. Within this period, OpenSSH does not need to re-establish a connection to the Git server, which makes pushes and pulls much faster.
