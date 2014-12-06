====================
 Writing Guidelines
====================

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
* Description of :wikipedia:`Imperative Mood on Wikipedia <Imperative_mood>`

reStructuredText Conventions
============================

Because there are many ways to write reStructuredText, we have set some conventions to be followed when editing the documentation.

Section Headers
---------------

Although docutils avoids "imposing a fixed number and order of section title adornment styles", ahdering to conventions produces results of higher quality and greater consistency. Please use *the exact order* used in the description of `reStructuredText Sections`_ when writing documentation. See the source code of this page for an example.

When using the first two header styles, pad the title with a space on both sides as shown in `reStructuredText Sections`_ (typing a space is not necessary on the right; just make it look correct).

.. _reStructuredText Sections: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#sections

Backticks and Hyperlinks
------------------------

When creating hyperlinks in rST, do not use backticks when they are not necessary:

* **Good:** ``abcd_``, ``ab-cd_``, ``ab.cd_``, ```ab cd`_``, ```ab+cd`_``
* **Bad:** ```abcd`_``, ```ab-cd_```, ```ab.cd_```
