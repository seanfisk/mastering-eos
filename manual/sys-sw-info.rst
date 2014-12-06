.. -*- coding: utf-8 -*-

=================================
 System and Software Information
=================================

For various reasons, it is sometimes necessary to know the version of a piece of hardware or software that you are using on EOS. Rather than list the versions of everything here, this section instructs you on *how to obtain version information* from the piece of software or operating system.

System
======

All-In-One Tools
----------------

These tools show large amounts of information about the system, including but not limited to information on the operating system, hardware, and network.

..
   Other tools which we have considered:

   - lshw: installable via yum; displays a warning about needing root
   - lshw-gui: GUI for lshw; installable via yum; tries to run as root and crashes when it can't
   - hwinfo: deprecated

inxi
````

inxi_ is a full-featured Bash script that can be used to obtain information about many parts of the system including the operating system and hardware. inxi is unfortunately not installed on EOS computers by default, but is not difficult to install. It is unnecessary but beneficial to be familiar with the steps involved in :ref:`manual-install` as well.

First, follow the instructions in :ref:`ready-prefix`. Then run the following commands to install the inxi script and its man page::

    pushd ~/.local
    (mkdir -p bin && cd bin && wget http://smxi.org/inxi && chmod +x inxi)
    (mkdir -p share/man/man1 && cd share/man/man1 && wget http://inxi.googlecode.com/svn/trunk/inxi.1.gz)
    popd

After installing, follow the steps for :ref:`adjust-env`. You should now be able to run :cmd:`inxi` from the command line. inxi is a command-line program, so it can be run through SSH or a graphical terminal emulator.

To show a basic, medium-length output::

    inxi -b

To show most everything::

    inxi -v 7 -Z

For more information on the options, run::

    man inxi

.. _inxi: https://code.google.com/p/inxi/

HardInfo
````````

HardInfo_ is far and away the best tool to obtain organized information related to the system. HardInfo displays on the operating system, kernel, hardware, peripherals, network and more. Furthermore, it can also run benchmarks on the CPU, FPU, and GPU.

Unfortunately, it is not installed by default on the EOS computers, so it must be compiled from source. Don't be afraid, though --- by following these steps, you should be able to install HardInfo quickly and simply. It is unnecessary but beneficial to be familiar with the steps involved in :ref:`manual-install` as well.

.. _HardInfo: http://hardinfo.org/

First, follow the steps to :ref:`ready-prefix`. Then download the source code::

    cd ~/.local/src
    wget https://github.com/lpereira/hardinfo/archive/master.tar.gz -O - | tar -xz
    cd hardinfo-master

HardInfo uses :ref:`cmake-section` as a build system, so the steps will be very similar to those shown in that section. First, create the build directory and configure the build system::

    mkdir build
    cd build
    cmake -Wno-dev -DCMAKE_INSTALL_PREFIX="$HOME/.local" ..

.. warning::

    If you use :ref:`linuxbrew-section` as a package manager, CMake may find your locally-installed version of pkg-config_ and fail. To remedy this, run::

        cmake -Wno-dev -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DCMAKE_INSTALL_PREFIX="$HOME/.local" ..

.. _pkg-config: http://www.freedesktop.org/wiki/Software/pkg-config/

Next, build and install the program::

    cmake --build . --target install

After installing, follow the steps for :ref:`adjust-env`. Once this is done, run::

    hardinfo

HardInfo is a graphical program, so make sure to run it at a physical machine or through VNC. A GUI should pop up containing copious amounts of information on different parts of the current system. Enjoy using HardInfo!

Specific Tools
--------------

Although the all-in-one tools provide convenient ways to access lots of information about the system, sometimes all that is needed is one specific piece of information. This can be useful for scripts or when the other information simply isn't needed.

GNU/Linux Distribution
``````````````````````

The :cmd:`lsb_release` Standard Base) command will show you information regarding your distribution:

.. code-block:: console

    $ lsb_release -a
    No LSB modules are available.
    Distributor ID: CentOS
    Description:    CentOS release 6.5 (Final)
    Release:        6.5
    Codename:       Final

Linux Kernel
````````````

The :cmd:`uname` command will tell you about the operating system, including the Linux kernel version:

.. code-block:: console

    $ uname -a
    Linux eos04.cis.gvsu.edu 3.10.0-123.8.1.el7.x86_64 #1 SMP Mon Sep 22 19:06:58 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux

The third value is the Linux kernel version.

For more information, please see the following nixCraft articles:

* `Linux Command: Show Linux Version <http://www.cyberciti.biz/faq/command-to-show-linux-version/>`_
* `HowTo: Find Out My Linux Distribution Name and Version <http://www.cyberciti.biz/faq/find-linux-distribution-name-version-number/>`_

References
----------

The following links contain many commands that can be used to obtain information from the operating system.

- http://www.binarytides.com/linux-commands-hardware-info/
- http://www.cyberciti.biz/tips/linux-command-to-gathers-up-information-about-a-linux-system.html
- http://www.cyberciti.biz/faq/linux-list-hardware-information/
- http://www.cyberciti.biz/faq/linux-display-information-about-installed-hardware/

Software
========

Most programs respond to the ``--version`` option by printing their version, for example:

.. code-block:: console
    :emphasize-lines: 2

    $ bash --version
    GNU bash, version 4.2.45(1)-release (x86_64-redhat-linux-gnu)
    Copyright (C) 2011 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

    This is free software; you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

However, this is a de-facto standard, and may not work for all programs. A notable example is Java:

.. code-block:: console

    $ java --version
    Unrecognized option: --version
    Error: Could not create the Java Virtual Machine.
    Error: A fatal exception has occurred. Program will exit.

The correct way is to use the ``-version`` flag:

.. code-block:: console
    :emphasize-lines: 2

    $ java -version
    java version "1.7.0_65"
    OpenJDK Runtime Environment (rhel-2.5.1.2.el7_0-x86_64 u65-b17)
    OpenJDK 64-Bit Server VM (build 24.65-b04, mixed mode)

Be aware that there is also no standard for displaying the version of the program, so other information may be provided.

If the program was installed with a package manager, the package manager is able to output information about the program in a standard format. Yum is the package manager on CentOS and will print the following information on a package:

.. code-block:: console
    :emphasize-lines: 7

    $ yum info bash
    Loaded plugins: fastestmirror, langpacks
    Loading mirror speeds from cached hostfile
    Installed Packages
    Name        : bash
    Arch        : x86_64
    Version     : 4.2.45
    Release     : 5.el7_0.4
    Size        : 3.5 M
    Repo        : installed
    From repo   : updates
    Summary     : The GNU Bourne Again shell
    URL         : http://www.gnu.org/software/bash
    License     : GPLv3+
    Description : The GNU Bourne Again shell (Bash) is a shell or command language
                : interpreter that is compatible with the Bourne shell (sh). Bash
                : incorporates useful features from the Korn shell (ksh) and the C shell
                : (csh). Most sh scripts can be run by bash without modification.

If you use :ref:`linuxbrew-section`, it will also print information about its packages:

.. code-block:: console
    :emphasize-lines: 4

    $ brew info bash
    bash: stable 4.3.30, HEAD
    http://www.gnu.org/software/bash/
    /home/smithj/.linuxbrew/Cellar/bash/4.3.30 (59 files, 7.9M) *
      Built from source
    From: https://github.com//homebrew/blob/master/Library/Formula/bash.rb
    ==> Dependencies
    Required: readline ✔
    ==> Caveats
    In order to use this build of bash as your login shell,
    it must be added to /etc/shells.

Note that Linuxbrew shows the current version of the package (line 2) *and* the version that is installed (highlighted line) [if one is installed].

Web Server
==========

For PHP development or general web development using EOS, it is sometimes necessary to obtain information about PHP and Apache, the web server. To do this, follow these steps to enable a so-called PHPInfo page::

    echo '<?php phpinfo(); ?>' > ~/public_html/info.php
    chmod o+x ~ ~/public_html
    chmod o+r ~/public_html/info.php

Now visit :samp:`http://cis.gvsu.edu/~{smithj}/info.php` in your browser, replacing with your username where appropriate. Upon visiting the page, PHP will dump a large amount of information on itself and the web server.

While this page in itself does not present a security risk, it can be a valuable tool for potential attackers. You are therefore requested to remove the page after you have obtained the necessary information::

    rm ~/public_html/info.php

Please contact |the-sysadmin|_ with further questions about PHP and the web server.
