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

Although docutils avoids "imposing a fixed number and order of section title adornment styles", adhering to conventions produces results of higher quality and greater consistency. Please use *the exact order* used in the description of `reStructuredText Sections`_ when writing documentation. See the source code of this page for an example.

When using the first two header styles, pad the title with a space on both sides as shown in `reStructuredText Sections`_ (typing a space is not necessary on the right; just make it look correct).

.. _reStructuredText Sections: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#sections

Indentation
-----------

`Indentation in reStructuredText`_ is both simple and complex. Instead of dictating that the indent must be a certain number of spaces, or use tabs, indentation is always relative to the prior input. Unfortunately, this tends to make things confusing, so we've set some conventions.

Default indentation is 3 spaces, and should be used for almost everything including :rest-primer:`literal blocks <source-code>`, :rest-primer:`directives`, and :rest-primer:`comments`:

.. code-block:: rest

   This is some Python::

      print('This is Python')
      if True:
          print('so we still indent 4 spaces *within* the code')

   .. toctree::
      :maxdepth: 2

      one
      two
      three

   ..

      Here is a comment.
      And a second line.

The 3-space indent is used because it looks better than 2 or 4 when using the directive syntax.

:rest-primer:`Lists <lists-and-quote-like-blocks>` differ from the 3-space indent. Each item should include one space after its delimiting character, and the contents of the item should be lined up with that, as shown in the primer example. Here is another example:

.. code-block:: rest

   - First item
   - Some Bash:

     .. code-block::

        ls -l

   - Here we have
     two lines.

   #. This list
   #. has a different
      indent

.. _Indentation in reStructuredText: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#indentation

Correct Usage of Roles
----------------------

- When referring to a command or program, use our project-specific ``:cmd:`` role:

  .. code-block:: rst

     The :cmd:`ls` command lists files in a directory.

  However, when referring inline to a command line to be run, use the inline literal syntax:

  .. code-block:: rst

     The ``ls -l`` command lists files in a directory in a long format.

  Never use the :sphinx-role:`command role <command>` or :sphinx-role:`program role <program>`.
- Use the :sphinx-role:`envvar role <envvar>`  when appropriate, and create a corresponding entry in :ref:`env-vars`.
- Do not use the :sphinx-role:`option role <option>`, as it emits a warning if a corresponding :sphinx-directive:`option directive <option>` is not found. This would be fine, but we want to remain warning free. Instead, just use normal literal text.

Backticks and Hyperlinks
------------------------

When creating hyperlinks in rST, do not use backticks when they are not necessary:

.. code-block:: rest

   .. Good
   abcd_
   ab-cd_
   ab.cd_
   `ab cd`_
   `ab+cd`_

   .. Bad
   `abcd`_
   `ab-cd`_
   `ab.cd`_

Linking to Sections
-------------------

Although regular reST supports `implicit hyperlink targets`_ to section titles, etc., we recommend using the Sphinx-specific :sphinx-role:`ref role <ref>` for cross-referencing. See the last sentence of the :sphinx-role:`ref` documentation if you are curious as to why.

.. _implicit hyperlink targets: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#implicit-hyperlink-targets
