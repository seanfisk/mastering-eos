.. _linuxbrew-section:

===========
 Linuxbrew
===========

Linuxbrew_ is a package manager for GNU/Linux systems. The main advantage of Linuxbrew over system package managers like Apt and Yum is that it allows installation of software on a per-user basis. Linuxbrew is a Linux port of Homebrew_, the popular package manager for Mac OS X. As such, some of its packages still contain Mac-specific code or do not yet build on GNU/Linux. Your mileage may vary, but in general Linuxbrew works quite well.

.. important::

   Before using Linuxbrew, please make sure that you are comfortable with compiling and installing software manually. Although Linuxbrew generally makes installing user-level software much easier, there is no magic --- it performs the same steps as you would during a manual install. When Linuxbrew does not behave as intended, you will need knowledge of manual installation to fix the problem. What we are saying is this: do not come to |the-sysadmin|_ with Linuxbrew package installation issues unless you have first tried to compile the software on your own.

The Linuxbrew dependencies *should* already be satisfied, so you will be able to install without issue. If they are not, please talk to |the-sysadmin|_. To install, then, please follow the `installation instructions on the homepage`_.

After installation, run the following to uncover possible issues that you may have when installing packages::

   brew doctor

Before moving forward, do your best to correct any issues reported by this command.

Installing packages with Linuxbrew is quite easy. For example,
::

   brew install tmux

installs the latest version of tmux_, the terminal multiplexer.

In this one command, Linuxbrew does a lot for you. It first installs tmux's dependency, libevent_. Then it configures, builds, and installs tmux, setting the prefix to the correct location automatically. Furthermore, it sets the :file:`tmux` executable's rpath (see :ref:`lib-deps`), meaning that the executable will automagically find the necessary libraries within your Linuxbrew prefix::

   $ patchelf --print-rpath ~/.linuxbrew/bin/tmux
   /home/smithj/.linuxbrew/lib

This command uses patchelf_, which can also be installed using Linuxbrew ;)

You can use the version of tmux you just installed by typing::

   $ ~/.linuxbrew/bin/tmux

Continue reading :ref:`user-hierarchies` to find out how to use it without typing the full path and to make your locally-installed version override the system version.

Enjoy installing packages using Linuxbrew!

.. _Linuxbrew: http://brew.sh/linuxbrew/
.. _installation instructions on the homepage: http://brew.sh/linuxbrew/#installation
.. _libevent: http://libevent.org/
.. _tmux: http://tmux.sourceforge.net/
.. _patchelf: http://nixos.org/patchelf.html
