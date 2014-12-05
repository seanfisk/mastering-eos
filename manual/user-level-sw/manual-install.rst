.. _manual-install:

=====================
 Manual Installation
=====================

System package managers like Apt and Yum usually install pre-compiled software, binaries which are typically compiled on a build server infrastructure like Launchpad_. Mac OS X and Windows users are also used to pre-compiled software, as most downloadable programs are distributed as application bundles or ready-to-run EXEs, respectively.

However, due to the myriad of different GNU/Linux distributions, software for GNU/Linux is often distributed in source code form only. This requires a potential user of the software to build the software from its source code, colloquially known as *compiling from source*. In addition, due to the lack of an accepted structure for installing user-level software, almost all software that is installed in a per-user fashion will need to be compiled from source.

.. _ready-prefix:

Ready the Prefix
================

The hierarchy to which a program is installed is typically called its *prefix*. Most build systems will install by default to :file:`/usr/local`, the system hierarchy typically used for custom-installed programs or programs compiled from source. However, because a standard user cannot write to this prefix, we are required to change our installion prefix to a directory within our home directory.

The prefix that we recommend for manually-installed user-level programs is :file:`~/.local`, which is the hidden :file:`.local` directory immediately within your home directory. This directory has some precedent, being `used by Python`_ and `in the Freedesktop specifications`_. Setting this prefix is the primary step to successfully installing user-level software.

To ready your prefix for downloading and compiling source code, run the following command::

    mkdir -p ~/.local/src

This command creates a ``src`` directory inside of your :file:`~/.local` prefix. We will use this directory later for housing downloaded program source code.

.. _Launchpad: https://launchpad.net/
.. _used by Python: http://legacy.python.org/dev/peps/pep-0370/#unix-notes
.. _in the Freedesktop specifications: http://standards.freedesktop.org/basedir-spec/basedir-spec-0.6.html#variables

Download and Extract
====================

To compile and install software, you must first obtain the source code. The first step is to visit the project's web site and ascertain the location of its source code. The source code is typically distributed in a :wikipedia:`tar <Tar_%28computing%29>` or :wikipedia:`zip <Zip_%28file_format%29>` archive, so look for files ending in ``.tar.gz``, ``.tar.bz2``, or ``.zip``. After downloading, the files should be extracted to the source code directory, :file:`~/.local/src`.

Example: GNU Bash and tar archives
----------------------------------

Let's download the source code for `GNU Bash`_, the default shell on the EOS system. First, begin by switching to the directory containing our source code::

    cd ~/.local/src

The latest version of Bash at this time of writing is 4.3, so that is what we will download. Start by visiting the `Bash home page`_. Under :guilabel:`Downloading Bash`, click the HTTP link. You will be taken to a :wikipedia:`directory index <Webserver_directory_index>` which contains a list of downloadable files. Scroll down to find a file named :file:`bash-4.3.tar.gz`.

Although you can download this file directly using your browser, it is often easier to copy the URL and download on the command line. This is especially true if accessing EOS using SSH. Copy the URL by clicking :guilabel:`Copy Link Location` or similar in your browser, then download the source code using :command:`wget`::

    wget http://ftp.gnu.org/gnu/bash/bash-4.3.tar.gz

This should create a :file:`bash-4.3.tar.gz` file in the current working directory. This file is a :wikipedia:`tar archive <Tar_%28computing%29>` which has been compressed with the `GNU zip`_ compression algorithm. A file of this type typically has a ``.tar.gz`` or ``.tgz`` file extension and is colloquially known as a *tarball* [*tarball* refers to tar archives of any or no compression scheme].

The contents of this archive can be extracted using the ``tar`` program as follows::

    tar -xf bash-4.3.tar.gz

.. hint::

    :command:`tar` can automatically detect the compression format by the extension, so passing the compression algorithm as you may see elsewhere is usually unnecessary.

.. warning::

    Most source code tarballs are "well-behaved", meaning that they create one directory which matches the name of the tarball. This is a convention, but is by no means required. Make sure you trust the source of the tarball before extracting the files. You can view the contents of a tarball with the :command:`less` built-in tar viewer::

        less bash-4.3.tar.gz

This command should have created a :file:`bash-4.3` directory in the current working directory. Make that directory your working directory::

    cd bash-4.3

You are now in the root of the GNU Bash source distribution.

.. hint::

   If you do not care about saving the original source tarball, you can download and extract simultaneously with::

        wget http://ftp.gnu.org/gnu/bash/bash-4.3.tar.gz -O - | tar -xz

   Note that you must pass the compression algorithm to :command:`tar` because it is not able to detect the type by file extension when input is given through a pipe.

.. _Bash home page:
.. _GNU Bash: http://www.gnu.org/software/bash/
.. _GNU zip: http://www.gzip.org/

Example: EditorConfig and zip archives
--------------------------------------

For our zip example, we will download the source code for the `EditorConfig C Core`_. EditorConfig is a project which helps developers establish formatting standards for a project (and is used by |title|!). First switch to the directory containing our source code::

    cd ~/.local/src

The latest version of the EditorConfig C Core at this time of writing is 0.21.1, so that is what we will download. Visit the `download page for EditorConfig C Core 0.12.0`_ and select the link for the source code zip archive. The project also offers a tarball download, but we will use the zip for the purposes of this example.

Download the file with :command:`wget` as shown in the earlier example::

    wget http://sourceforge.net/projects/editorconfig/files/EditorConfig-C-Core/0.12.0/source/editorconfig-core-c-0.12.0.zip

This should create a :file:`editorconfig-core-c-0.12.0.zip` file in the current working directory. This file is a :wikipedia:`zip archive <Zip_%28file_format%29>` just like those you may have seen on your desktop operating system. This file can be extracted using the InfoZip_ :command:`unzip` utility::

    unzip editorconfig-core-c-0.12.0.zip

.. warning::

     Unlike source tarballs, zip files sometimes have all files in one directory or sometimes have all files immediately in the root directory. Again, however, this is convention --- make sure you trust the source of the archive before extracting the files. You can view the contents of a zip archive with :command:`less` built-in zip viewer::

        less editorconfig-core-c-0.12.0.zip

This command should have created a :file:`editorconfig-core-c-0.12.0.zip` directory in the current working directory. Make that directory your working directory::

    cd editorconfig-core-c-0.12.0

You are now in the root of the Editorconfig C Core source distribution.

.. _EditorConfig C Core: https://github.com/editorconfig/editorconfig-core-c
.. _download page for EditorConfig C Core 0.12.0: http://sourceforge.net/projects/editorconfig/files/EditorConfig-C-Core/0.12.0/source/
.. _InfoZip: http://www.info-zip.org/

Build the Software
==================

Almost all professional-grade software projects use a build system for compilation and installation. A build system automates the tedious task of constructing compiler commands and installing files to the proper places. Using a build system should not be viewed as running a program which automagically produces another program, but rather as a practical solution to a real problem.

There are several build systems used by typical software on GNU/Linux. Read the following sections to learn about the different build system and how to identify and use them.

Autotools
---------

Autotools_, also known as the GNU Build System, is the build system currently used by most programs on GNU/Linux. You can usually identify a program using Autotools by the presence of a :file:`configure` script in the root of the source distribution.

The software which makes up Autotools itself is usually not necessary to build a program using Autotools as a build system. Instead, the functionality is embedded into the :file:`configure` script itself. Autotools build systems typically only require the presence of Make.

Example: GNU Bash
`````````````````

An example of a piece of software that uses Autotools is `GNU Bash`_, the subject of our earlier example. We will compile the version of GNU Bash that we extracted earlier. Start by switching to the source code root directory if not already there::

    cd ~/.local/src/bash-4.3

The next step is to create the build directory, which we'll create inside the source directory for convenience::

    mkdir build
    cd build

Now, we must configure the software by running the :file:`configure` script.  It is to the :file:`configure` script that we must also pass the all-important ``--prefix`` option. Run the following::

    ../configure --prefix ~/.local

You will see many lines printed to the terminal, which is the script doing various checks on the system and compiler and adjusting the build to our specific system.

:file:`configure` scripts typically also accept a myriad of other options, which can be viewed with::

    ../configure --help | less

Passing other options is typically unnecessary unless you would like to customize the build. Piping to :command:`less` is recommended due to the usual length of the output.

.. warning::

    Note that::

        ../configure --prefix=~/.local

    will *not* work, as Bash will not `expand the tilde`_ properly unless the path is its own argument.

    .. _expand the tilde: http://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html#Tilde-Expansion

.. important::

    Many build systems (including Autotools) support both *in-source* and *out-of-source* builds. In-source builds take place when the :file:`configure` script is run in the same directory as the source code, that is::

        ./configure

    Running the :file:`configure` script in any other directory is referred to as an out-of-source build. Out-of-source builds are generally preferred because they allow separation of build artifacts from the source code. However, not all build systems or projects support out-of-source builds. The build illustrated in this example is an out-of-source build.

After configuring the software, it is time to build. This can be accomplished with::

    make

Running this command typically produces an avalanche of output. The lines that you see printed are primarily compiler commands, which are printed as they are being run.

After running this command, you should have a workable version of the Bash shell. Test this out by running:

.. code-block:: console

    $ ./bash --version
    GNU bash, version 4.3.0(1)-release (x86_64-unknown-linux-gnu)
    Copyright (C) 2013 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

    This is free software; you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

The final step is to install the files generated by the build. Do this with::

    make install

GNU Bash has now been installed to your home directory! Continue reading to find out how to make your locally-installed version override the system version.

.. _cmake-section:

CMake
-----

CMake_ is a popular alternative to Autotools as a build system on GNU/Linux. You can usually identify a CMake build system by the presence of a :file:`CMakeLists.txt` file in the root of the source distribution.

The :command:`cmake` program needs to be installed in order to build projects using CMake as a build system. It is installed by default on EOS.

.. _CMake: http://www.cmake.org/

Example: EditorConfig
`````````````````````

.. Note: EditorConfig depends on libpcre, which is installed on EOS at this time of writing. If this changes, this example will need to change.

An example of a project that uses CMake as a build system is the `EditorConfig C Core`_, the subject of our earlier example. We will compile the version of the EditorConfig C Core that we extracted earlier. Start by switching to the source code root directory if not already there::

    cd ~/.local/src/editorconfig-core-c-0.12.0

The next step is to create the build directory, which we'll create inside the source directory for convenience::

    mkdir build
    cd build

Now, we must configure the software by running CMake. Similar to the :file:`configure` script, we tell CMake the install prefix at this stage. Run the following::

    cmake -DCMAKE_INSTALL_PREFIX="$HOME/.local" ..

You will see various checks on the system and compiler printed to the terminal as with Autotools.

After configuring the software, it is time to build. This can be accomplished with::

    cmake --build .

During the build, CMake will display which file is currently being built along with a percentage of files built on the left.

After running this command, you should have a workable version of EditorConfig. Test this out by running:

.. code-block:: console

    $ bin/editorconfig --version
    EditorConfig C Core Version 0.12.0

The final step is to install the files generated by the build. Do this with::

    cmake --build . --target install

Other Build Systems
-------------------

The majority of C and C++ software that you may want to install to your EOS account likely uses Autotools or CMake as its build system. For those that don't, we recommend consulting the project's :file:`README` or :file:`INSTALL` file or the project's documentation or website for compilation instructions.

.. _adjust-env:

Adjusting the Environment
=========================

Executable Path
---------------

You can always use executables installed to your home directory by typing the full path to the executable, for example:

.. code-block:: console

    $ ~/.local/bin/bash --version
    GNU bash, version 4.3.0(1)-release (x86_64-unknown-linux-gnu)
    Copyright (C) 2013 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

    This is free software; you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

For obvious reasons, typing the full path can get tedious if you are using the executable frequently. In addition, other utilities may assume that the executable in question is available on the :envvar:`PATH` and not in a custom prefix.

If you are installing an executable that is already present on the system, there is another consideration --- you may want to override the system version with the version that you installed to your home directory. This is typically useful if you would like to use a newer version of a program than one installed to a system hierarchy.

To illustrate this, note that when typing:

.. code-block:: console

    $ which bash
    /usr/bin/bash

the shell will still default to using the system Bash, which happens to be :file:`/usr/bin/bash`.

To resolve both of these issues, we can add the executable's parent directory to executable search path, stored in the environment variable :envvar:`PATH`. Open your :file:`~/.bash_profile` in an editor and add the following line to the end::

    export PATH=~/.local/bin:$PATH

This line prepends the path of your locally-installed executables to the executable search path. Your executable will now not only be accesible without typing the full path, but it will also override any executables of the same name in system hierarchies.

*Restart your shell to effect the changes to your* :file:`~/.bash_profile` *by logging out and logging back in.* After logging back in, the following should yield:

.. code-block:: console

    $ which bash
    ~/.local/bin/bash

Now you should be able to simply type::

    bash

to start the GNU Bash installed to your home directory!

Man and Info Paths
------------------

Although you are now able to run your new Bash without typing the full path, the commands::

    man bash
    info bash

still show the Bash documentation for the system Bash. Although this may not seem like a big deal, small changes between versions of the same program can be the difference between an working and non-working script. To allow :command:`man` and :command:`info` to find locally-installed documentation, add the following lines to your :file:`~/.bash_profile`::

    export MANPATH=~/.local/share/man:~/.local/man:$MANPATH
    export INFOPATH=~/.local/share/info:$INFOPATH

There is unfortunately some inconsistency with the location of installed man pages, which why we added both directories to the :envvar:`MANPATH`. :envvar:`INFOPATH` does not have these problems.

After restarting your shell, the commands at the beginning of this section should bring up the correct documentation.

.. _lib-deps:

Library Dependencies
====================

Bash and the EditorConfig C Core both compile without issue on EOS. However, programs frequently have compile-time dependencies: libraries which need to be installed before compiling the program.

As with the project itself, one option is to ask the |the-sysadmin|_ to install the library for you. If you would like to compile and install the dependency on your own, it is possible, but is currently out of the scope of this guide. Here are some hints:

* When compiling the program, you may need to set the :envvar:`CPPFLAGS` and :envvar:`LDFLAGS` environment variables to allow the compiler to locate headers and libraries, respectively. See the `Autoconf manual on Preset Output Variables`_ for descriptions of each of these variables. Some build systems are able to locate headers and libraries automatically in the specified install prefix.
* If you installed the libraries to your home directory, the operating system will not know to search for them there when running a program (even if that program is in your home directory). To allow the program to find its shared library dependencies at runtime, you must either set its rpath_ (recommended) or use the :envvar:`LD_LIBRARY_PATH` environment variable (not recommended). See the following links for hints on this topic:

  - `Russ Allbery's notes on Shared Library Search Paths`_
  - The `Autoconf manual on Preset Output Variables`_
  - The `Wikipedia entry on rpath`_

  You can see the default paths in which the system looks for libraries by running::

      ldconfig -v | less

Conclusion
==========

As you can see, manual installation of programs is a complex but predictable process. This is where package managers like :ref:`linuxbrew-section` become useful.
