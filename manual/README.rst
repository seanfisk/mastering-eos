======================
 Mastering EOS Manual
======================

The Mastering EOS manual serves as the "new EOS documentation." It is written in Sphinx_, and built and deployed using the Fabric_ SSH framework.

.. _Sphinx: http://sphinx-doc.org/
.. _Fabric: http://docs.fabfile.org/en/latest/

Tips for using Fabric
=====================

Fabric is used to build and deploy the documentation. To deploy the documentation in typical fashion, run::

    fab --parallel deploy_html_pdf_epub

This deploys the said formats to the user's personal web directory in their EOS account.

If your EOS username doesn't match your local username, you may specify it with::

    fab --parallel --user smithj deploy_html_pdf_epub

The EOS SSH fingerprints table is generated only if the file doesn't exist. If you want to re-generate the fingerprints table, re-run the task specifically::

    fab --parallel generate_fingerprints_table

This will re-generate the fingerprints table in ``common/ssh/fingerprints.rst``. The ``--parallel`` flag is recommended as it runs SSH connections in parallel and is much faster.

If you are having trouble with some EOS SSH hosts being down, but still want to generate the table, you can run the following to ignore down hosts::

    fab --skip-bad-hosts --parallel generate_fingerprints_table

This will skip the down hosts when generating the table. This isn't recommended for deployment, as it may miss hosts in the table, but is OK for a quick test.

To see all tasks that are available via Fabric, run::

    fab --list

To see all Fabric options, run the typical::

    fab --help

Enjoy deploying with Fabric!
