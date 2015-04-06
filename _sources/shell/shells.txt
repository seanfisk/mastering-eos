==================
 Available Shells
==================

.. _bash:

Bash
====

`GNU Bash`_ (*Bourne-again shell*) is the default shell on many Unix-like systems, including most GNU/Linux distributions and OS X. It is a full-featured shell with many capabilities. Although other shells exist, we recommend first learning Bash because of its ubiquity and popularity. In addition, by learning Bash, you will have a better understanding of other shells if you choose to use them.

The `GNU Bash Manual`_ is the comprehensive guide to all of the workings of the shell. It is a reference manual, so it does not provide a lot of examples. However, it is clear and concise and recommended reading for Bash users. It is also available for the version specific to EOS by typing ``info bash`` on any EOS computer.

.. warning::

   OS X is notorious for including a very outdated version of Bash as the default shell. If you use Bash under OS X, you are recommended to install a newer version using a package manager such as Homebrew_.

.. _GNU Bash: http://www.gnu.org/software/bash/
.. _GNU Bash Manual: http://www.gnu.org/software/bash/manual/bash.html

.. _sh:

sh
===

The :wikipedia:`Bourne shell <Bourne_shell>` (also known by sh) is one of the original Unix shells. It is the precursor to many modern shells, including :ref:`bash` and :ref:`zsh`. Although it is still used for scripts, its use as an interactive shell is primarily historical.

The sh interpreter is specified by :posix:`POSIX <nframe>` in the :posix:`sh <utilities/sh>` and :posix:`Shell Command Language <utilities/V3_chap02>` pages. On many systems, the command :cmd:`sh` actually activates :ref:`bash` in an sh-emulation mode (try ``sh --version``).

.. _zsh:

Zsh
===

`Z shell`_ (Zsh) is a very capable shell based on the Bourne shell with too many features to count. Although it is not directly related to :ref:`bash`, those who are proficient in Bash will undoubtedly feel comfortable using Zsh. In many ways, Zsh can be seen as having a superset of Bash's features.

.. _Z shell: http://zsh.sourceforge.net/

.. _fish:

fish
====

Another interesting shell is `fish <http://fishshell.com/>`__, the friendly interactive shell. fish aims to be a modern shell that works well out-of-the-box. It is especially focused on interactive features such as on-the-fly syntax highlighting, auto-suggestions, and auto-completion. However, it also focuses on having a clean, consistent command interface.

fish is not installed by default on EOS, so you will have to install using :ref:`linuxbrew-section` or compile it manually.

Other Shells for Unix-like Systems
==================================

Two other traditional shells are Tcsh and KornShell. Tcsh_ (TENEX C SHell) is a modern shell based on the C shell. Kornshell_ is an older shell developed at AT&T Bell Laboratories based on the best features of the Bourne and C shells. For an overview of Unix shell history, and comparison of these shells as well as those listed above, see the `UNIX shell differences`_ article.

The concept of a shell is neither complex nor set in stone. Many projects have striven to create alternative shells. These are usually based on enhanced interaction with a specific programming language or environment, yet retain some of the usage and concepts of traditional shells:

+---------------+-----------+
|Shell          |Environment|
+===============+===========+
|Eshell_        |Emacs_     |
+---------------+-----------+
|Zoidberg_, psh_|Perl_      |
+---------------+-----------+
|IPython_       |Python_    |
+---------------+-----------+
|ShellJS_       |NodeJS_    |
+---------------+-----------+
|Pry_           |Ruby_      |
+---------------+-----------+

For a more complete list of shells, see Wikipedia's :wikipedia:`shell comparison <Comparison_of_command_shells>` and :wikipedia:`article on Unix shells <Unix_shell>`. For a side-by-side comparison of the syntax of different shells, see `Hyperpolyglot's Unix shells section`_.

.. _Tcsh: http://www.tcsh.org/
.. _KornShell: http://www.kornshell.org/
.. _Eshell: http://www.gnu.org/software/emacs/manual/html_mono/eshell.html
.. _Zoidberg: https://github.com/jberger/Zoidberg
.. _psh: http://gnp.github.io/psh/
.. _Perl: http://www.perl.org/
.. _IPython: http://ipython.org/ipython-doc/2/interactive/shell.html
.. _ShellJS: http://documentup.com/arturadib/shelljs
.. _NodeJS: http://nodejs.org/
.. _Pry: http://pryrepl.org/
.. _UNIX shell differences: http://www.faqs.org/faqs/unix-faq/shell/shell-differences/
.. _Hyperpolyglot's Unix shells section: http://hyperpolyglot.org/unix-shells

Which Shell?
============

When deciding which shell to use, it is important to consider both types of use: *interactive work* and *scripting*. When choosing to use a shell interactively, you are really making that decision only for yourself. However, when deciding which shell to use for a script, you are choosing that shell for the script's audience. That could be for yourself only, for the members of your project, or for the world if the script is part of a public project. It is also obviously an advantage to use the same shell for both interactive and script work.

For interactive work, we recommend starting with :ref:`bash`. Bash is currently the default shell on OS X and most GNU/Linux distributions (including EOS systems). Because Bash is prevalent on many systems and is a full-featured shell, we recommend becoming comfortable with it first.

Bash is a great shell even for power users. However, there are other shells that offer more built-in features and opportunity for extensibility. Once you have become proficient in Bash, we recommend trying :ref:`zsh`. Zsh offers a similar experience to Bash but has even more features, plugins, and frameworks.

For those who have tried :ref:`bash` or :ref:`zsh` and are looking for something more modern and different, :ref:`fish` is a good choice. However, be aware that because it is less popular, less programs, plugins, and frameworks are compatible with it.

When it comes to scripting, we once again recommend using :ref:`bash`. More exotic shells such as :ref:`zsh` and :ref:`fish` are often not found on systems, meaning that the shell has to be installed before the script can be run. However, Bash's prevalence means that it is installed by default on many systems, making it a good choice for scripting. If scripting features of more advanced shells are needed, we recommend instead moving straight to a true programming language such as Python_ or Ruby_.

You may find some recommendations to use :ref:`sh` for scripting because it is specified by POSIX while Bash is not. Because Bash is widely available and offers significant benefits over sh, we recommend that you script on the EOS machines using Bash. You will certainly get differing recommendations on this, but we feel Bash's features and availability justify its use for scripting.

Windows Shells
==============

While Unix-like operating systems are known for full-featured shells, Windows also has quite a few shells available.

.. _cmd.exe:

Command Prompt
--------------

:wikipedia:`Command Prompt <Cmd.exe>` (or cmd.exe) is the classic Windows shell, inherited mostly from the :wikipedia:`DOS` shell :wikipedia:`COMMAND.COM`. It is a relatively limited shell, with only a basic set of commands. For those looking for a daily shell on Windows, you are recommended to look elsewhere.

.. _powershell:

Windows PowerShell
------------------

`Windows Powershell`_ is a relatively new advanced shell for Windows released by Microsoft in 2006. Different versions of PowerShell are distributed with Windows starting from Windows 7. PowerShell is based on the :wikipedia:`.NET Framework <.NET Framework>`, but is inspired by Unix shells like :ref:`bash`.

Since it has been released, PowerShell has become increasingly popular with developers looking for a decent shell on Windows, and a large number of scripts and plugins have been developed by the community. This makes it a great choice for your Windows shell.

If you are interested in learning PowerShell and already know Bash, see `Hyperpolyglot's OS automation section`_ for a side-by-side comparison of POSIX shell, Command Prompt, and PowerShell features.

.. tip::

   Although Microsoft created a great shell with :ref:`powershell`, they did nothing to replace the terrible :wikipedia:`Win32 console <Win32_console>` provided with Windows, which runs both :ref:`cmd.exe` and :ref:`powershell` by default. For a better console on Windows, we recommending checking out ConEmu_ or `Console 2`_.

.. _Console 2: http://sourceforge.net/projects/console/
.. _ConEmu: https://code.google.com/p/conemu-maximus5/
.. _Windows PowerShell: http://microsoft.com/powershell
.. _Hyperpolyglot's OS automation section: http://hyperpolyglot.org/shell

Cygwin
------

Cygwin_ is a project which provides a Unix-like environment for Windows, including shells such as :ref:`Bash`. If you are looking for many of the tools and libraries you use on Unix-like operating systems, but on Windows, Cygwin is a great choice.

.. _Cygwin: https://cygwin.com/
