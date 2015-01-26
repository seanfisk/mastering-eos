rsync
=====

rsync_ is the go-to tool for remote synchronization. rsync is the best choice for file transfer when the desire is to mirror a large file or directory of data, transferring it between your local machine and an EOS system. The rsync program is almost always installed by default.

.. _rsync: http://rsync.samba.org/

Operation of rsync is very similar to SCP. The main difference between rsync and SCP is that rsync features a remote-update protocol which transfers only the differences between the local and remote files, decreasing sync time and bandwidth.

A typical use of rsync is as follows::

   rsync \
       --verbose \
       --archive \
       --compress \
       classes/cis163/projects \
       eos01.cis.gvsu.edu:classes/cis163/projects

This syncs a local projects directory with a remote one. The ``--verbose`` option instructs rsync to tell you what it is doing, the ``--archive`` option tells rsync to duplicate the files almost exactly, and the ``--compress`` option tells rsync to use compression within the protocol.

Here is another example for deploying a website. Specifically, this deploys a |title| build to your user's personal website::

   rsync \
       --verbose \
       --archive \
       --compress \
       --delete \
       --chmod=go=rX \
       build/website \
       eos01.cis.gvsu.edu:public_html/mastering-eos

The ``--delete`` option tells rsync to delete files on the remote machine not present on the local machine. This allows true synchronization of the two directories. However, be careful with this option, as it will delete files without confirmation!

The ``--chmod=go=rX`` option tells rsync to set the permissions of the files to represent the correct permissions for use on a website.

Because rsync command lines can get quite long, it is often useful to record them in a script. See :manpage:`rsync(1)` by running ``man rsync`` for more information on the use of rsync.

There is also an rsync GUI available called Grsync_, though we cannot attest to its effectiveness.

.. _Grsync: http://www.opbyte.it/grsync/
