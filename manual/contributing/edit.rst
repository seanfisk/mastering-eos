====================
 Editing the Manual
====================

Sync Your Fork
==============

Unless you have just forked the repository, always begin every editing session by `syncing your fork`_.

.. _syncing your fork: https://help.github.com/articles/syncing-a-fork/

Make Your Changes
=================

Let's start by making our actual changes to the document. As mentioned before, the manual is written using Sphinx_ in the markup language reStructuredText_. Unless your changes are very minor, at least a surface understanding of reStructuredText is necessary. We recommend fully reading `Sphinx's reStructuredText Primer`_ to start. Because |title| makes heavy use of Sphinx and reStructuredText features, you can also look around at existing source documents and their output to get an idea of how documents are written in Sphinx.

Consider the following sentence:

   I like spinach.

Let's change this very sentence. We'll use this as an example throughout this section. Although we're using this example, feel free to adapt the example to your actual changes.

Everyone loves bacon, so we'll change it to that instead.

Fire up your editor to open the file::

   gedit manual/contributing/edit.rst

Find the sentence and make the change.

As shown in the previous section, you will want to :ref:`contributing-build-docs` and :ref:`contributing-view-results` after you make your change. Once you are happy with how it looks, it is time to create a branch on which to commit your change.

.. _Sphinx's reStructuredText Primer: http://sphinx-doc.org/rest.html

Create a Feature Branch
=======================

The next step is to create a *feature branch* for your change. A feature branch represents the addition of one cohesive set of changes. For example, a feature branch could contain related changes to sections on SSH and SCP, but should not contain unrelated changes to the personal website and VNC sections.

Try to pick a name for your branch that represents your change. Create a new feature branch for our example with::

   git checkout -b bacon-rules-spinach-drools

.. hint::

   In this example, we only make one commit on the feature branch. Although one commit is fine, you are free to make more commits on a feature branch as well.

Commit Your Change
==================

Once you have made your change, it's time to commit. First, let's ask Git for a status report:

.. code-block:: console

   $ git status
   On branch bacon-rules-spinach-drools
   Changes not staged for commit:
     (use "git add/rm <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working directory)

           modified:   manual/contributing/edit.rst

As you can see, Git is aware of our change, but we have not yet told Git that we intended to make them.

Assure Git of our intentions with::

   git add manual/contributing/edit.rst

Looking at the status now yields:

.. code-block:: console

   $ git status
   On branch bacon-rules-spinach-drools
   Changes to be committed:
     (use "git reset HEAD <file>..." to unstage)

           modified:   manual/contributing/edit.rst

We are now ready to commit our change. As part of the commit, you will be asked for a commit message. The commit message should be a short (less than 50 characters), high-level summary of what has been done in this commit. Before writing a message for this commit, look back at commit messages for prior commits with::

   git log

These messages should give you an idea of what a typical commit message for this project looks like. Press :kbd:`q` to quit the log viewer. To commit your change, run the following::

   git commit

This should open gedit, or another editor if you have configured one. Enter your commit message:

   I like bacon, not spinach. Geez; get it right.

Push The Branch
===============

Your changes have now been committed. The last step in this section is to push them to your fork. Do so with the following::

   git push -u origin bacon-rules-spinach-drools

Your branch has now been pushed to your forked repository! Continue on to the next section to find out how to propose them as changes to the |title| official repository.

Git Resources
=============

This guide illustrates the bare minimum amount of Git commands that you will need to complete this task. For more guidance on using Git, please check out `GitHub's list of Git resources`_. In particular, GitHub's `Try Git`_ is great for beginners.

.. _GitHub's list of Git resources: https://help.github.com/articles/what-are-other-good-resources-for-learning-git-and-github/
.. _Try Git: https://try.github.com/
