=========================
 Reviewing Pull Requests
=========================

.. note::

   This section assumes general familiarity with `pull requests`_. If you are not familiar with pull requests, please read up on them first.

Reviewing `pull requests`_ is a common part of developing and contributing to |title|. The diff view is handy when reviewing changes made to content, but is not particularly helpful when reviewing entirely new sections. In this case, it is often more convenient to look at the content in built form.

Luckily, this is not difficult. Since we are not planning to edit the code, only build and review it, we can check out the remote branch directly. First, find out the name of the branch by looking at the pull request. We'll go with the bacon example here::

   git fetch
   git checkout origin/bacon-rules-spinach-drools

Git will now alert you that you are in `detached head`_ state. Don't worry, that's OK. Now, build and open the docs as usual, for example::

   ./waf ohtml

You can now view the documentation with the changes mentioned in the pull request. If the pull request is updated, you can see the new changes with::

   git fetch
   git checkout origin/bacon-rules-spinach-drools

Notice that these are the same commands as before.

To return to a named branch, just check it out::

   git checkout master

.. _detached head: http://git-scm.com/docs/git-checkout#_detached_head
