=========================
 Contributing to |title|
=========================

This manual is a living document. It is maintained by its authors, but students (you!) are encouraged to contribute to the guide. The manual is written by GVSU CIS students for GVSU CIS students.

The easiest way to to contribute is by reporting an issue or requesting a section with our `issue tracker`_. One of the authors should respond to your issue and give feedback.

The |title| manual is written using Sphinx_, an excellent multi-target documentation generator. The documentation is written in the markup language reStructuredText_. The poster is written in LaTeX_ using Beamer_ and beamerposter_, although contribution to that is not necessarily as useful for obvious reasons. All of our tooling is written in Python_. Although these tools may seem overwhelming, intimate familiarity with them is not necessary for contribution.

The source code for |title| is `hosted on GitHub`_. GitHub is a popular site for hosting code repositories using Git_, a popular version control system. If you are familiar with the GitHub contribution process, contributing to |title| is exactly the same.

For those unfamiliar with Git_ and GitHub_, contributing to |title| may seem rather involved. However, by following the steps outlined, it should be rather straightforward. We request that you first give it a try on your own, but failing that, please don't hesitate to contact the authors. We want your contributions!

To contribute to |title|, follow these steps:

* Read `GitHub's guide to Contributing to a Project`_.
* `Set Up Git`_ if you have not already done so.
* Fork_ the |title| repository and make your changes.
* Create a `pull request`_ to the original repo containing your changes.

An author should respond to your pull request, and with any luck, your changes should go live! We look forward to seeing your contributions!

.. _issue tracker: https://github.com/seanfisk/mastering-eos/issues
.. _hosted on GitHub: https://github.com/seanfisk/mastering-eos
.. _Git: http://git-scm.com/
.. _GitHub: https://github.com/
.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText:
.. _LaTeX: http://latex-project.org/
.. _Beamer:
.. _beamerposter: http://www-i6.informatik.rwth-aachen.de/~dreuw/latexbeamerposter.php
.. _Python: http://python.org/
.. _hosted on GitHub: https://github.com/seanfisk/mastering-eos
.. _GitHub's guide to Contributing to a Project: https://guides.github.com/activities/contributing-to-open-source/#contributing
.. _Set Up Git: https://help.github.com/articles/set-up-git
.. _Fork: https://help.github.com/articles/fork-a-repo
.. _pull request: https://help.github.com/articles/using-pull-requests

Writing Style
=============

When writing technical documentation, it is important to follow a consistent writing style. Within this manual, we attempt to follow the `OpenStack writing conventions`_. Their documentation presents a great summary of how to write coherent technical documentation.

.. _OpenStack writing conventions: https://wiki.openstack.org/wiki/Documentation/Conventions/Writing_style#Writing_style

Sphinx uses SmartyPants_ to transform quotes, dashes, and ellipses into typographically correct entities for HTML output. You can use straight quotes, straight apostrophes, and three dots --- they will be transformed into the correct characters. For dashes, first read up on `the three types of dash`_. The transformations are as follows: Hyphens stay as is, two hyphens will be transformed into an en dash, and three hyphens will be transformed into an em dash.

.. _SmartyPants: http://daringfireball.net/projects/smartypants/
.. _the three types of dash: http://csswizardry.com/2010/01/the-three-types-of-dash/

Please also see the following links for writing technical documentation:

* `ACS Distance Education Guidelines for Technical Writing <http://www.acs.edu.au/info/environment/bio-science/technical-documentation.aspx>`_
* `Novell Open Source Documentation Style Quick Start <http://www.novell.com/documentation/osauthoring/ex_osstyle/data/ex_osstyle.html>`_
* `BlueBream Documentation Guidelines <http://bluebream.zope.org/doc/1.0/dev/writing.html>`_
* Description of `Imperative Mood on Wikipedia <http://en.wikipedia.org/wiki/Imperative_mood>`_
