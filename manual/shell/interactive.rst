.. highlight:: console

.. _shell-interactive:

=======================
 Interactive Shell Use
=======================

Most shells may be used in one of two modes: interactive or batch. In interactive mode, the shell waits for you to type commands, then evaluates them when you press :kbd:`Enter`. This is called a :wikipedia:`Read-eval-print loop <Read-eval-print_loop>`. In batch mode, the shell runs commands listed in a script file, just like a regular interpreted programming language like Python_ or Ruby_.

Most of the following features are usable in both interactive or batch mode. Some features are more useful in one than the other. For example, :ref:`shell-aliases` are seldom used in scripts, while the :ref:`shell-shebang` is never used interactively.

.. warning::

   These examples are expected to be run with :ref:`bash` 4 on EOS. Most of them will also work in a POSIX-compatible shell (:ref:`sh`) and :ref:`zsh`. Bash 4 is the default shell, that is, the shell that you are presented with when starting a terminal through a GUI session or logging in through SSH.

.. contents::
   :local:
   :depth: 1

.. _shell-aliases:

Aliases
=======

An alias can be a shortcut to typing a frequently-used command. For example, if you visit a certain directory often::

   $ alias hw='cd ~/classes/cis452/hw/01'
   $ pwd
   /home/smithj
   $ hw
   $ pwd
   /home/smithj/classes/cis452/hw/01

After running the :cmd:`alias` command, :cmd:`hw` will now switch to that directory when typed.

An alias can also be used to remember a lesser-used command. For example::

   $ alias extract='tar -xvf'
   $ extract bash-4.3.tar.gz
   bash-4.3/
   ...

Notice that we can still pass arguments to the alias. In fact, it is almost exactly like typing those characters at the command-line.

.. _shell-builtins:

Built-Ins
=========

For a typical command, the shell finds an executable file on the system and executes it. An example is the :cmd:`ls` command, which is an executable on the system, typically located at :file:`/usr/bin/ls`::

   $ /usr/bin/ls mydir
   file1.txt  file2.txt

However, some commands are actually part of the shell, called *shell built-ins*. A shell built-in differs from a normal command in that it typically operates on things *within the shell itself*, rather than just for one command. A prime example is :cmd:`cd`, which changes the current working directory within the shell, affecting all subsequent commands::

   $ pwd
   /home/smithj
   $ cd mydir
   $ pwd
   /home/smithj/mydir

To find out if a command is an executable or a shell built-in, use the :cmd:`type` command::

   $ type ls
   ls is /usr/bin/ls
   $ type cd
   cd is a shell builtin
   $ type type
   type is a shell builtin

The :cmd:`type` command is also a shell built-in!

To see all shell built-ins, :bash:`consult the Bash manual <Shell-Builtin-Commands>`.

Quoting
=======

In certain cases, Bash will interpret the command you give it in a different way than you might expect::

   $ ls directory name with spaces
   ls: directory: No such file or directory
   ls: name: No such file or directory
   ls: spaces: No such file or directory
   ls: with: No such file or directory

This is because Bash splits the command line it is given based upon spaces, and passes each argument to the program in question. To get Bash to interpret the spaces as an actual character, use :bash:`single quotes <Single-Quotes>`::

   $ ls 'directory name with spaces'
   file1.txt  file2.txt

Single quotes remove any special meaning from all the characters inside them. *Always use single quotes when the characters inside the quotes should not be interpreted by the shell.*

:bash:`Double quotes <Double-Quotes>` may be used to expand only the meaning of certain shell meta-characters. They are most often used for variable substitution. For example, to print your current working directory::

   $ echo "My current directory is: $PWD"
   My current directory is: /home/smithj/directory name with spaces

Double quotes are very frequently used, but it is easy to use them incorrectly. Know their behavior and test your commands with different values to make sure they are behaving correctly.

.. _shell-env-vars:

Environment Variables
=====================

:wikipedia:`A process' environment <Environment_variable>` is a mapping of key-value pairs possessed by every running process in the system. They are typically used to modify the behavior of programs. You are probably familiar with some common ones; for example, :envvar:`PATH`, :envvar:`EDITOR`, and :envvar:`PWD`. Environment variable names on Linux are case-sensitive and can contain most characters, although by convention they are usually named in all caps with words separated by underscores.

Bash supports manipulation of the environment variables for programs it runs (*child processes*) in various ways. To see what environment variables Bash is giving to its child processes, use the :cmd:`env` program::

   $ env
   ...

You should see a list of ``VAR=value`` printed. These are the variables and values Bash is giving to its child processes.

In Bash, regular variables can be set in any shell session rather easily::

   $ GVSU_CS='Computer Science'
   $ GVSU_IS='Information Systems'

However, these variables are only seen by commands built into the shell. After settings these variables, verify this with :cmd:`env`::

   $ env | grep -E '^GVSU'

You should see no output. However, you can instruct Bash to send these variables to child processes by using the :cmd:`export` built-in::

   $ export GVSU_CS
   $ env | grep -E '^GVSU'
   GVSU_CS=Computer Science

Notice that ``GVSU_CS`` has been sent to the program, but ``GVSU_IS`` has not. When the value of the variable is changed, the value sent to the child processes is also changed. It does not need to be exported again::

   $ GVSU_CS='Cool Stuff'
   $ env | grep -E '^GVSU'
   GVSU_CS=Cool Stuff

To see all variables in Bash marked for export, use the following command::

   $ declare -x
   ...
   declare -x GVSU_CS="Cool Stuff"
   ...

Here some other shortcuts to do with environment variables::

   $ export GVSU_CS='Cool Stuff' # Set and export in one line
   $ GVSU_CS='Not my major' env | grep -E '^GVSU' # Set for one command only
   GVSU_CS=Not my major

.. _shell-env-vars-example:

Example
-------

A real-life example of an environment variable in use is the :envvar:`EDITOR` environment variable. Various programs use this variable to determine what editor they should use when a file needs to be edited. An example is the ``crontab -e`` command. Try the following commands::

   $ EDITOR=nano crontab -e # type Ctrl-X to exit
   $ EDITOR=vim  crontab -e # type :q<Enter> to exit

You should see each respective editor open up when the command is run!

.. note::

   :wikipedia:`Cron` is not set up for GVSU students; this command just edits your Cron configuration file. You do not need to modify it.

Pipelines
=========

The concept of a :wikipedia:`pipeline <Pipeline_(Unix)>` is central to the philosophy of Unix-like operating systems. A pipeline is typically used to combine the capabilities of multiple programs to perform a task. This is accomplished by sending the output of each program to the next program in the series. Pipelines can be formed easily using the shell with the vertical bar (aka pipe) character::

   $ ls | grep -F cis162 # Look for files/directories with 'cis162' in the name

Example: Paging
---------------

Often times, a command will produce output which fills the screen. The :cmd:`dmesg` command reports kernel events and frequently has lots of output::

   $ dmesg
   [    0.000000] Initializing cgroup subsys cpuset
   [    0.000000] Initializing cgroup subsys cpu
   [    0.000000] Initializing cgroup subsys cpuacct
   [    0.000000] Linux version 3.10.0-123.20.1.el7.x86_64 (builder@kbuilder.dev.centos.org) (gcc version 4.8.2 20140120 (Red Hat 4.8.2-16) (GCC) ) #1 SMP Thu Jan 29 18:05:33 UTC 2015
   [    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-3.10.0-123.20.1.el7.x86_64 root=UUID=967c544c-50b5-4497-900d-0b5014ecdd71 ro vconsole.keymap=us crashkernel=auto vconsole.font=latarcyrheb-sun16 rhgb quiet LANG=en_US.UTF-8
   [    0.000000] e820: BIOS-provided physical RAM map:
   [    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009d7ff] usable
   [    0.000000] BIOS-e820: [mem 0x000000000009d800-0x000000000009ffff] reserved
   [    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000fffff] reserved
   [    0.000000] BIOS-e820: [mem 0x0000000000100000-0x000000001fffffff] usable
   ...

If you want to see anything besides the last screenful of output, one option is to use the scrollback feature provided by most terminal emulators (just scroll up). However, scrollback is limited and does not work under multiplexers such as tmux (although tmux has its own scrollback buffer). Another option is to use a pager. A *pager* is a program that allows you to browse and scroll through the output of a command, much like opening the output of the command in an editor. Two default pagers available on most Unix-like systems are :cmd:`less` and :cmd:`more`. While :cmd:`more` allows only paging forward, :cmd:`less` allows scrolling forward and back, making :cmd:`less` the preferred choice for most tasks. To page the output of :cmd:`dmesg`, type::

   $ dmesg | less

You will be taken into a text-based user interface in which you can use arrow keys, Vim keys, or Emacs keys to scroll around. Press ``q`` to quit.

Example: Filtering
------------------

Sometimes, the entire output of a program is not needed. One of the most common uses of a pipeline is to filter output of a command using :wikipedia:`grep`. For example, to find all files with a ``.png`` extension in the current directory::

   $ ls
   a.jpg
   b.jpg
   c.jpg
   d.png
   e.png
   f.png
   g.gif
   h.gif
   i.gif
   $ ls | grep '\.png$'
   d.png
   e.png
   f.png

:cmd:`grep` only prints the lines that match the given regular expression. For more information on :cmd:`grep` and the regular expression syntaxes it supports, see the man page.

Example: Extraction
-------------------

While :cmd:`grep` excludes certain lines based on a pattern, sometimes we wish to filter or exclude based on different criteria. Let's attempt to print the last 10 people who logged on to this computer.

To begin, the :cmd:`last` command will output a "table" of previous logins to the machine on which you are currently working::

   $ last
   smithj   pts/0        148.61.121.9     Wed Mar 11 14:30   still logged in
   smithj   pts/1        148.61.121.9     Wed Mar 11 13:00 - 14:00  (01:00)
   woodriir pts/0        :0.0             Wed Mar 11 12:00 - 12:30  (00:30)
   millers  pts/1        148.61.121.9     Wed Mar 11 11:30 - 11:45  (00:15)
   woodriir pts/0        :0.0             Wed Mar 11 11:00 - 11:15  (00:15)
   woodriir pts/0        :0.0             Wed Mar 11 10:00 - 10:15  (00:15)
   ...

   wtmp begins Tue Nov 25 09:26:28 2014

The first column is the username. We want to extract the usernames for further use in the pipeline. That's doable, but we have a two-line footer that we first need to remove. We can use the :cmd:`head` utility to print out all of the lines *except for the last two*::

   $ last | head --lines -2
   smithj   pts/0        148.61.121.9     Wed Mar 11 14:30   still logged in
   smithj   pts/1        148.61.121.9     Wed Mar 11 13:00 - 14:00  (01:00)
   woodriir pts/0        :0.0             Wed Mar 11 12:00 - 12:30  (00:30)
   millers  pts/1        148.61.121.9     Wed Mar 11 11:30 - 11:45  (00:15)
   woodriir pts/0        :0.0             Wed Mar 11 11:00 - 11:15  (00:15)
   woodriir pts/0        :0.0             Wed Mar 11 10:00 - 10:15  (00:15)
   ...

Perfect! Now, we need to remove all the information besides the username. We can use the :cmd:`cut` utility to extract it::

   $ last | head --lines -2 | cut --fields 1 --delimiter ' '
   smithj
   smithj
   woodriir
   millers
   woodriir
   woodriir
   ...

Looks good. Now, let's use the :cmd:`uniq` utility to delete repeated lines, effectively collapsing repeated logins::

   $ last | head --lines -2 | cut --fields 1 --delimiter ' ' | uniq
   smithj
   woodriir
   millers
   woodriir
   ...

Great! Lastly, the output is rather long. We only want to see the last 10, so we can use :cmd:`head` again to truncate the results::

   $ last | head --lines -2 | cut --fields 1 --delimiter ' ' | uniq | head
   smithj
   woodriir
   millers
   woodriir
   reboot
   millers
   smithj
   millers
   smithj
   reboot

That's it! See the manual pages for each of these utilities to learn more about them.

Example: Advanced
-----------------

Although the last example was neat, pipelines need not stop there. You can chain many programs together to create a new tool which does something uniquely useful. For example, we can combine various tools to find all lunch items served at `Fresh Food`_ this week, highlighting all items involving chicken. First, write a file that will be used in the pipeline, and set a variable:

.. _Fresh Food: http://www.campusdish.com/en-US/CSMW/GVSU/Menus/FreshFoodCompany.htm

.. important::

   This example works only with Bash 4 (the default shell on EOS). Ensure you are running Bash 4 with::

      $ echo $BASH_VERSION
      4.2.45(1)-release

   The first number should be 4.

.. code-block:: bash

   cat <<'EOF' >/tmp/fresh-menu.xsl
   <?xml version="1.0" encoding="UTF-8"?>
   <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
       <xsl:template match="/">
           <xsl:for-each select="//a[@class='recipeLink']">
               <xsl:value-of select="."/>
               <xsl:if test="position() != last()">
                   <xsl:text>&#xA;</xsl:text>
               </xsl:if>
           </xsl:for-each>
       </xsl:template>
   </xsl:stylesheet>
   EOF
   readonly URL='http://www.campusdish.com/en-US/CSMW/GVSU/Menus/FreshFoodCompany.htm'

Next, run the pipeline, which pages the menu items, one per line, with chicken items highlighted!

.. code-block:: bash

   wget --quiet --output-document - "$URL"                | # download web page
     xsltproc --html /tmp/fresh-menu.xsl - 2>/dev/null    | # parse HTML
     tail --lines +2                                      | # trim initial XML declaration
     sort --unique                                        | # sort, collapse unique items
     sed 's/&amp;/\&/g'                                   | # replace '&amp;' with '&'
     while read -r line; do                                 # embedded shell loop
       line=${line,,}                                       # make lowercase
       line=($line)                                         # convert to array
       echo ${line[@]^}                                     # capitalize each word
     done                                                 | # loop: all-caps to title case
     tee lunch-menu.txt                                   | # write to file
     grep -E --ignore-case --color=always '.*chicken.*|$' | # highlight chicken dishes
     less --RAW-CONTROL-CHARS                               # page the output

Once you are done, press ``q`` to exit the pager. You should also see that the lunch menu items were written to the file, :file:`lunch-menu.txt`, in the current directory::

   $ less lunch-menu.txt

As you can see, pipelines can be used to accomplish any number of tasks. Although they are not always the solution, they are a great choice when batch processing is needed.

Pipelines can also be created in most programming languages. Languages such as `Python <https://docs.python.org/library/subprocess.html#replacing-shell-pipeline>`__ and `Ruby <http://ruby-doc.org/stdlib-2.0.0/libdoc/open3/rdoc/Open3.html#method-c-pipeline>`__ offer facilities to easily create pipelines, and most pipeline implementations (including most shells) are implemented using the POSIX C API calls :posix:`fork <functions/fork>`, :posix:`exec <functions/exec>`, and :posix:`pipe <functions/pipe>`.

Enjoy creating your own pipelines!

Redirection
===========

Many commands provide the option to read input from and write output to files. For example, a C compiler::

   $ cc -o main main.c

In this case, :file:`main.c` is the C source code input file while :file:`main` is the output executable.

However, many commands have no option to specify an input or output file. For example, back to the most basic: :cmd:`ls` features no way to send its output to a file::

   $ ls # outputs to terminal
   a.jpg  b.jpg  c.jpg  d.png  e.png  f.png  g.gif  h.gif  i.gif

And the :ref:`write` command offers no option to read from a file::

   $ write smithj # waiting for input

However, this does not mean that it is not possible to write to or read from files using these commands!

Enter redirection. Redirection is a shell feature which allows you to send output of a command to a file or send the contents of a file as input to a command.

Basic Redirection
-----------------

Output redirection is accomplished with the greater-than sign::

   $ ls >myfiles.txt # no output; output was written to the file

The file :file:`myfiles.txt` will now contain the usual output of :cmd:`ls`. Input redirection is accomplished using the less-than sign::

   $ write smithj <hello-john.txt # does not wait for input

Both input and output redirection can be used simultaneously. To find all words which have the letters "eos" in them, and write them to a file::

   $ grep --fixed-strings --ignore-case eos </usr/share/dict/words >eos-words.txt

.. tip::

   Many programs including :cmd:`grep` offer the option to read from file. So the previous example could also be written without input direction using::

      $ grep --fixed-strings --ignore-case eos /usr/share/dict/words >eos-words.txt

   Far fewer commands support writing to an output file, making output redirection the more frequently-used feature.

Error Redirection
-----------------

So far, we have only talked about the basic input and output streams, stdin and stdout. However, there is one more standard stream, stderr, to which well-behaved programs will write error messages. When redirecting output, these error messages will not be redirected. For example, we can count the number of lines in the :wikipedia:`password file <Passwd#Password_file>` file and write that to a file using :cmd:`wc`::

   $ wc --lines /etc/passwd >num-lines.txt

No output is written to the terminal. However, if we try to access the :wikipedia:`shadow file <Passwd#Shadow_file>`, which has different permissions::

   $ wc --lines /etc/shadow >num-lines.txt
   wc: /etc/shadow: Permission denied

This will create an empty file :file:`num-lines.txt` and write the error to the terminal.

In many cases, this is the desired behavior, since you will be notified of errors immediately when they happen. However, there are times when you would like to log both errors and output. This can be done by using the stderr :wikipedia:`file descriptor <File_descriptor>` as such::

   $ wc --lines /etc/shadow >out.txt 2>err.txt

It is also possible to combine both stdout and stderr by redirecting stderr to the stdout file descriptor::

   $ wc --lines /etc/shadow 2>&1 >out-and-err.txt

.. tip::

   In :ref:`bash` 4 and :ref:`zsh`, a shortcut to this syntax is::

      $ wc --lines /etc/shadow &>out-and-err.txt

Discarding Output
-----------------

Sometimes a command produces unnecessary output that is not useful. For example, to look for TXT files in the :file:`/var` directory::

   $ find /var -name '*.txt'
   ...

Because :cmd:`find` tries to look in all subdirectories, you will likely see an avalanche of *Permission denied* errors. To eliminate this from the output, we can discard all :cmd:`find` errors by sending them to the :wikipedia:`null device <Null_device>`::

   $ find /var -name '*.txt' 2>/dev/null
   ...

The output should now be much more reasonable, and not include any *Permission denied* errors!

.. warning::

   Be aware that redirecting stderr to :file:`/dev/null` discards *all* error messages, not just *Permission denied* errors. For example, if the :file:`/var` directory did not exist (unlikely, but possible), the error message reporting that would not be shown.

Appending Files
---------------

When using output redirection, the destination file is truncated (contents are erased) before writing the output of the command. To append to the file instead of truncating, use ``>>``::

   $ echo 'this command truncates the file' >out.txt
   $ echo 'this command appends to the file' >>out.txt

.. _shell-path-manip:

Path Manipulation
=================

Using the shell, it is possible to invoke programs by typing the full path to the executable file::

   $ /usr/bin/ls mydir
   file1.txt  file2.txt

However, this gets unwieldy quickly. Fortunately, the operating system (which the shell uses) provides a feature that can be used to address this issue, yielding the more normal-looking::

   $ ls mydir
   file1.txt  file2.txt

This feature is the the :envvar:`PATH` environment variable, and it is a very important concept on Unix-like systems, both for interactive and scripted commands. Despite its importance, the concept is rather simple: the :envvar:`PATH` environment variable contains a list of paths to search for executables.

The :envvar:`PATH` variable contains a list of paths separated by colons (``:``). When instructed to do so, the shell searches through these paths looking for a executable with the given relative path. You can view your :envvar:`PATH` with::

   $ echo $PATH
   /usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin

Your output will probably contain more paths, and trying to decipher them from a long string can be headache-inducing. For a nicer output, instruct Bash to replace the colons with newlines::

   $ echo "${PATH//:/$'\n'}"
   /usr/local/bin
   /usr/bin
   /usr/local/sbin
   /usr/sbin
   $ alias path-print='echo "${PATH//:/'$'\n''}"' # create an alias (nasty quoting)

.. tip::

   :ref:`zsh` users can use one of::

      $ (IFS=$'\n'; echo "${path[*]}") # zsh maintains the array $path as a mirror of string $PATH
      /usr/local/bin
      /usr/bin
      /usr/local/sbin
      /usr/sbin
      $ alias path-print='(IFS='"$'\n'"'; echo "${path[*]}")' # similar to the Bash technique
      $ echo "${PATH//:/\n}"
      /usr/local/bin
      /usr/bin
      /usr/local/sbin
      /usr/sbin
      $ alias path-print='echo "${PATH//:/\n}"'

When you type :cmd:`ls`, the shell searches for an executable named ``ls`` in each of the directories listed in the :envvar:`PATH`, starting from the top. To confirm where Bash is finding :cmd:`ls`, use the :cmd:`which` command::

   $ command which ls
   /usr/bin/ls

.. note::

   Some shells (e.g., :ref:`zsh`) offer :cmd:`which` as one of a number of :ref:`shell-builtins`. We use ``command which`` instead of just :cmd:`which` to access the actual executable file for consistent output.

Now that you know how the :envvar:`PATH` works, and how to view it, you can manipulate it for your own use. Let's add a script which implements our own version of :cmd:`ls` that "emphasizes privacy", overriding the default version. We'll put this script in :file:`~/bin`, which is the conventional location for a user's personal scripts::

   $ mkdir -p ~/bin # create the scripts directory
   $ cat <<EOF > ~/bin/ls # write the script
   #!/usr/bin/env bash
   echo 'Nothing to see here. Move along.'
   EOF
   $ chmod +x ~/bin/ls # make the script executable

You can now run this script with ``~/bin/ls``. However, just typing ``ls`` results in the real :cmd:`ls` being run::

   $ ~/bin/ls
   Nothing to see here. Move along.
   $ ls
   file1.txt  file2.txt

To allow our version of :cmd:`ls` to be run, we need to add our :file:`~/bin` directory to the front of the :envvar:`PATH`. We can do that with::

   $ export PATH=~/bin:"$PATH"
   $ path-print
   /home/smithj/bin
   /usr/local/bin
   /usr/bin
   /usr/local/sbin
   /usr/sbin

.. note::

   Exporting the :envvar:`PATH` variable is not necessary for this example to work. However, in most cases it is desirable to also give the value of :envvar:`PATH` to any scripts run from the shell, in addition to using it within the shell itself.

Now, running plain ``ls`` runs our version::

   $ ls
   Nothing to see here. Move along.

Success! However, the :file:`~/bin` directory will not be on the :envvar:`PATH` for future shells. To make this change permanent, add it to your :file:`.bash_profile`::

   $ echo 'export PATH=~/bin:"$PATH"' >> ~/.bash_profile

The ``export`` line should now be the last line of your :file:`.bash_profile`. Now follow the directions for :ref:`shell-startup-apply`. :cmd:`ls` should now permanently run our version!

.. important::

   **Help! Give me my** :cmd:`ls` **back!**

   After following this example, to restore the :cmd:`ls` command to its former glory, run::

      $ rm ~/bin/ls

   This will remove the modified :cmd:`ls` example script. You can also always access the real :cmd:`ls` by running::

      $ /usr/bin/ls
      file1.txt  file2.txt

Startup Files
=============

The behavior of Bash can be customized by modifying its *rc files* (runtime configuration files). These are files containing Bash commands which are run within the current shell session at different points throughout the session.

Although there are more files which are run, two of the most important Bash rc files are :file:`.bashrc` and :file:`.bash_profile`. There is a lot of confusion about when these files are run. However, for an interactive Bash session [#noninteractive]_, the answer is simple:

- :file:`.bash_profile` is run for login shells.
- :file:`.bashrc` is run for non-login shells.

So what is a login shell? A login shell is a shell that is run when you first log into the computer. For example, when you SSH into EOS, you have started a login shell. All subsequent shells started from that shell are non-login shells (unless otherwise specified by the ``--login`` option). Desktop environment terminal emulators (such as GNOME Terminal) typically start non-login shells by default (though this can be configured otherwise).

Here is a table describing where your shell customizations should go:

+------------------------------+---------------------+
|Customization                 |File                 |
+==============================+=====================+
|:ref:`Exported variables      |:file:`.bash_profile`|
|<shell-env-vars>`             |                     |
+------------------------------+---------------------+
|Non-exported variables        |:file:`.bashrc`      |
+------------------------------+---------------------+
|:ref:`shell-aliases`          |:file:`.bashrc`      |
+------------------------------+---------------------+
|Functions                     |:file:`.bashrc`      |
+------------------------------+---------------------+
|Key bindings                  |:file:`.bashrc`      |
+------------------------------+---------------------+
|:wikipedia:`Umask`            |:file:`.bash_profile`|
+------------------------------+---------------------+
|Shell Prompt (falls under     |:file:`.bashrc`      |
|non-exported variables)       |                     |
+------------------------------+---------------------+
|:ref:`shell-path-manip` (falls|:file:`.bash_profile`|
|under exported variables)     |                     |
+------------------------------+---------------------+

.. [#noninteractive] Handling of startup files for non-interactive (also known as *script* or *batch*) sessions are more complex, and there is more variation between shells in how they are handled. For more information on which files are run in which scenarios, consult `this blog post <https://shreevatsa.wordpress.com/2008/03/30/zshbash-startup-files-loading-order-bashrc-zshrc-etc/>`_ for an excellent table and flowchart.

Your startup files contain the heart of your shell customizations. Almost any command that you would run interactively or in a script can go in your startup files.

.. _shell-example-files:

Example Startup Files
---------------------

Here are some example startup files which illustrate many of the features mentioned in this chapter. Although these are a good example, you are recommended to use these only as a starting point for your own personal startup files. The path manipulation is useful if you are using software installed through :ref:`manual-install` or :ref:`linuxbrew-section`. You can read more about it in :ref:`user-hierarchies`.

.. If you edit 'profile.bash', make sure that the line numbers in the "Managing Paths" section in 'manual/user-level-sw/user-hierarchies.rst' gets updated to match.

.. literalinclude:: profile.bash
   :language: bash

.. literalinclude:: rc.bash
   :language: bash

.. _shell-startup-apply:

Applying the Changes
--------------------

To allow changes to your shell startup files to take effect, you need to restart processes which have read it in addition to the children of such processes. See the table below for what this means:

+--------------------------+-------------------------------------------+------------------------------------------+
|Type of session           |Modified :file:`.bash_profile`             |Modified :file:`.bashrc`                  |
+==========================+===========================================+==========================================+
|Physical graphical session|Log out and log back in.                   |Close the terminal tab and re-open it.    |
|                          |                                           |Restarting the terminal emulator is not   |
|                          |                                           |necessary.                                |
+--------------------------+-------------------------------------------+------------------------------------------+
|VNC session               |Log out and log back in. Closing your VNC  |Close the terminal tab and re-open it.    |
|                          |window or terminating your SSH tunnel is   |Restarting the terminal emulator is not   |
|                          |unnecessary (unless you are typing commands|necessary.                                |
|                          |in the SSH tunnel session; see below).     |                                          |
+--------------------------+-------------------------------------------+------------------------------------------+
|SSH session               |End the session and SSH back in.           |Close the shell and start it again. If you|
|                          |                                           |only have one shell open (e.g., not using |
|                          |                                           |tmux), this will be the same as ending    |
|                          |                                           |your SSH session and logging back in.     |
+--------------------------+-------------------------------------------+------------------------------------------+
|Text terminal             |End the session and log back in.           |Close the shell and start it again. If you|
|                          |                                           |only have one shell open (e.g., not using |
|                          |                                           |tmux), this is the same as ending your    |
|                          |                                           |session and logging back in.              |
+--------------------------+-------------------------------------------+------------------------------------------+

.. warning::

   What doesn't [always] work?

   #. Any of ``source .bashrc``, ``source .bash_profile``, ``. .bashrc``, ``. .bash_profile`` (``source`` and ``.`` perform the same function). This does not start a new shell, but simply re-runs the commands in the specified file.
   #. ``exec bash``. This starts a new shell, but does it within the current shell's environment.

   Why not? Commands like ``export PATH=~/bin:"$PATH"`` unconditionally add a path to the existing value of :envvar:`PATH`. Running these commands again in the same shell can result in duplicate paths being added. In addition, removing these commands from the startup file and re-running the startup file in the same shell doesn't remove these paths from the actual environment.

   In general, commands in the startup files represent how to change the initial existing environment changed rather than representing the desired state of the environment. Because of this, they must always be executed from the same context.

Utilities
=========

Various utilities can help streamline your use of the shell. Although they take some effort to install and use, the time saved by using them usually outweighs the setup cost.

Directory Navigation
--------------------

One frequent task which can be expedited by utilities is changing directories. There are a few different tools which are popular for this task.

The first entry in this field is autojump_. autojump is *a cd command that learns*. By simply changing directories with :cmd:`cd` as usual, you can teach autojump to learn your most frequently-used directories. You can then jump to a frequently-used directory with the :cmd:`j` command. autojump uses Python and is available under a `variety of shells <https://github.com/joelthelion/autojump#requirements>`_.

z_ is utility inspired by autojump which also takes the recency of a directory's visit into account. Unlike autojump, it is implemented in pure shell script and is available for :ref:`bash` and :ref:`zsh`.

fasd_ is a tool inspired by autojump and z which extends the concept of z beyond directory navigation. fasd allows opening frequent/recent files and directories with pre-configured programs. It is available under a `wide variety of shells <https://github.com/clvv/fasd#compatibility>`_.

If you want to use any of these tools on EOS, the recommended method of installation is :ref:`linuxbrew-section`.

.. _autojump: https://github.com/joelthelion/autojump
.. _z: https://github.com/rupa/z/
.. _fasd: https://github.com/clvv/fasd

Programming Language Version Management
---------------------------------------

Serious users of specific programming languages may want to have different versions of the language installed simultaneously. For this task, version managers are extremely helpful. Here is a list of version managers for various languages.

- **Python:** `pyenv <https://github.com/yyuu/pyenv>`_
- **Ruby:** `rbenv <https://github.com/sstephenson/rbenv>`_, `RVM <http://rvm.io/>`_
- **Java:** `jenv <http://www.jenv.be/>`_
- **Perl:** `plenv <https://github.com/tokuhirom/plenv>`_, `perlbrew <http://perlbrew.pl/>`_

Many of these tools can be installed using :ref:`linuxbrew-section`.

Frameworks
==========

There are a great many frameworks out there for shell enhancement and customization. One of the first to become popular was `Oh My Zsh`_, a giant framework of functions, themes, and plugins for :ref:`zsh`. Zsh also has a number of other frameworks, listed in unixorn's list of awesome-zsh-plugins_, which includes a list of frameworks, many based on Oh My Zsh. Oh My Zsh has spawned a number of frameworks for other shells, including `Bash it`_ for :ref:`bash` and `Oh My Fish!`_ for :ref:`fish`.

Because the so-called "dotfiles" are an important part of customizing your terminal experience, many people use version control to track and store their dotfiles. We recommend visiting dotfiles.github.io_, an unofficial guide to storing your dotfiles on GitHub_ using Git_. This site includes example dotfiles, lists of frameworks for shells and editors, and dotfile management utilities. For anything more than trivial customizations, tracking your dotfiles with a version control system is highly recommended.

.. _Oh My Zsh: http://ohmyz.sh/
.. _awesome-zsh-plugins: https://github.com/unixorn/awesome-zsh-plugins
.. _Bash it: https://github.com/revans/bash-it
.. _Oh My Fish!: https://github.com/bpinto/oh-my-fish
.. _dotfiles.github.io: http://dotfiles.github.io/
