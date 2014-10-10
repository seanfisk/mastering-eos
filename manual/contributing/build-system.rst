========================
 Using the Build System
========================

Configure the Build
===================

For building the documents, we use Waf_ as a build system. Waf is similar to build systems like Autotools_ and CMake_ in that it has a separate configuration and build stages. To configure the project, run::

    ./waf configure --no-ssh-auto-update

Waf will check that all the requirements are met before preparing the build. If any are not met, please re-check your steps in :ref:`contributing-prereqs` or talk to |the-sysadmin|_. The ``--no-ssh-auto-update`` option disables re-building of the SSH fingerprints table. Since the deployment of |title| is automated, there is no reason for a contributor to leave auto-update on. A shortcut for this command is::

    ./waf configure -m

.. _contributing-build-docs:

Build the Documentation
=======================

After configuration, building is rather easy::

    ./waf build

You will see various build steps being executed as they are printed to the screen. This command builds both the manual and the poster and places the build artifacts in the :file:`build/manual` and :file:`build/poster` directories, respectively.

.. warning::

    From time to time, you may see a warning like this:

    .. code::

        Warning, treated as error:
        WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.

    The error is spurious and we believe it is rooted with running the Sphinx EPUB builder in parallel with other builders. For now, the workaround is just to re-run the build.

.. _contributing-view-results:

View the Results
================

The build will create outputs in various formats, which may viewed with the following commands::

    xdg-open build/manual/html/index.html             # HTML
    man build/manual/man/eos.7                        # Man page
    info build/manual/info/eos.info                   # Info docs
    xdg-open build/manual/latexpdf/mastering-eos.pdf  # PDF

Although we'd like all the outputs to look good, we primarily focus on the HTML output. The build also produces an e-book (EPUB) output, but EOS does not currently have an e-book reader installed.

Other commands
==============

In certain circumstances, it is useful to do a full rebuild. The command::

    ./waf clean

undoes the actions of ``./waf build``, meaning that the build artifacts are removed (but the build directory still exists). The command::

    ./waf distclean

undoes the actions of both ``./waf configure`` and ``./waf build``, meaning that the build directory is removed and the project must be re-configured to be rebuilt again.

If you would like to see (almost) exactly what a user visiting the |title| website sees, run::

    ./waf archive

This command creates the directory :file:`build/website`, which contains all the files that will be uploaded to the official website. You can then view the website in this directory with::

    xdg-open build/website/index.html

It is also possible to run multiple commands at once, for example::

    ./waf distclean configure -m build

This runs a full rebuild all in one command.
