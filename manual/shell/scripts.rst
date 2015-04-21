=================
 Shell Scripting
=================

.. _shell-shebang:

Shebang
=======

The shebang is a feature of Unix-like operating systems that allows text-based interpreted programs to be treated as executable files. The :wikipedia:`Shebang Wikipedia article <Shebang_(Unix)>` does a great job of explaining how the shebang works. There are two common shebangs used for Bash scripts::

   #!/bin/bash
   echo 'This script runs with the system Bash interpreter.'

::

   #!/usr/bin/env bash
   echo 'This script runs with the Bash interpreter on the PATH.'

Each shebang is relatively self-explanatory. The second uses the :cmd:`env` utility (see :ref:`shell-env-vars`) to execute with the first Bash interpreter found on the :envvar:`PATH`. Unless you have reason to specify the system Bash interpreter, the ``#!/usr/bin/env bash`` shebang is preferred because it gives the user greater flexibility over which Bash interpreter to use.

Boilerplate
===========

Although shell scripts allow rapid development, they suffer from a number of weaknesses. However, some of these weaknesses can be mitigated by making shell scripts more responsive to possible errors.

By default, Bash continues to execute commands in a script even if a command fails. This is rather non-intuitive, and usually not desired because each successive command typically depends on the result of previous ones. To tell Bash to report errors by exiting when a command fails, use the ``errexit`` option at the top of your script::

   set -o errexit

In addition, by default Bash substitutes an empty string for any undefined variable references. This is usually not desired because this typically represents a typo of some sort. To tell Bash to report any undefined variables, use the ``nounset`` option at the top of your script::

   set -o nounset

Combining these options with the shebang above yields the following shell script boilerplate::

   #!/usr/bin/env bash

   set -o errexit
   set -o nounset

By using these options, you will increase the chances of having robust, error-free scripts.

When to Shell Script
====================

Shell scripts can become unwieldy very quickly. When writing shell scripts, you must remember their trade-offs: although they frequently allow you to accomplish tasks very quickly, they are often ugly and error-prone. In this case, it is usually better to rewrite said scripts in a more full-featured programming language such as Python_ or Ruby_.
