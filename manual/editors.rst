.. See here for how we did the floats: http://stackoverflow.com/a/12988688
   We used 'clearfix' instead of 'clearer' because our theme supports it, and just used raw HTML because the LaTeX output doesn't support the floats anyway (not that it couldn't, but Sphinx doesn't, at least as far as we know).

.. |clearfix| raw:: html

    <div class="clearfix"></div>

=========
 Editors
=========

Choosing an editor is an important step for any programmer. As the task of programming is composed primarily of writing code, you will be spending a lot of time in your editor. We encourage you to try out many different editors before choosing the one that is right for you. Once you have chosen an editor, we encourage you to spend time becoming proficient with it --- it will reward you throughout your career.

This section lists various editors and explains the different classes under which they fall. These classes are not official; they are used only for the purposes of grouping like options together. All editors listed directly under their class are available on EOS; editors listed under the *Other* sections are not available on EOS but can be downloaded for other platforms (or in some cases, self-installed on EOS).

Basic Text Editors
==================

Basic text editors are a class of editors that usually include only simple text editing features. Some include syntax highlighting for languages, but do not usually include code completion. Their extensibility is usually minimal.

GNU nano
--------

`GNU nano`_ is an improved clone of the :wikipedia:`Pico <Pico_(text_editor)>` text editor. Editing takes place entirely within the terminal in its text user interface. Its features are very basic, with many of the controls outlined at the bottom of its screen.

.. _GNU nano: http://www.nano-editor.org/overview.php

GNU nano is best suited for small edits, for example, editing your :file:`.bashrc` or other configuration files. It is also useful over an SSH session because it operates full within the terminal.

gedit, KWrite, and Leafpad
--------------------------

gedit_ (GNOME_), KWrite_ (KDE_), and Leafpad_ (Xfce_ and LXDE_) are the default text editors for their respective desktop environments. All have a similar feature set, including syntax highlighting and other expected features of a text editor. They are useful for simple editing tasks, but we don't recommend using any of them as a full-time code editor.

.. _gedit: https://wiki.gnome.org/Apps/Gedit
.. _KWrite: https://www.kde.org/applications/utilities/kwrite/
.. _Leafpad: http://tarot.freeshell.org/leafpad/

Others
------

Other basic text editors not available on EOS, listed here for completeness:

- Microsoft Windows' :wikipedia:`Notepad <Notepad_%28software%29>` and :wikipedia:`WordPad`
- Mac OS X's :wikipedia:`TextEdit`

Advanced Text Editors
=====================

Advanced text editors are a class of editor which excel in editing quickly and efficiently. They usually allow extensive user customization and configuration, and have packages to augment their base features.

Vim and Emacs are two classic editors known to programmers everywhere. Both have a reputation for steep learning curves and massive extensibility. However, advanced users of each of these editors also have a reputation for being extremely productive.

Advanced text editors are recommended for those who have the time to learn how to be efficient with an editor. Effective use requires dedication of time *specifically to learning the editor*.

Vim
---

.. Extracted from 'runtime/vimlogo.pdf' in the Vim source tree.
.. image:: /images/editors/vim.png
    :align: left
    :alt: Vim logo
    :target: Vim_

Vim_ (Vi IMmproved) is an editor inspired by the classic :wikipedia:`vi` editor. One of the most popular editors of all time, Vim is included with many operating systems and available for many others. Vim is unique as compared to other popular editors in that it features a modal interface in which different keys execute different actions. Vim is customizable through `Vim script`_ as well as other languages. The first version of Vim was released in 1991, while the first version of vi was released in 1976.

As mentioned, Vim is available for many platforms including Windows, Mac OS X, and GNU/Linux.

|clearfix|

.. _Vim: http://www.vim.org/
.. _Vim script: http://en.wikipedia.org/wiki/Vim_script

GNU Emacs
---------

.. Adapted from 'etc/images/icons/hicolor/128x128/apps/emacs.png' in the Emacs source tree.
.. image:: /images/editors/emacs.png
    :align: left
    :alt: Emacs logo
    :target: `GNU Emacs`_

`GNU Emacs`_ (Editor MACroS) is an extensible and programmable editor. It is one of the oldest and most popular editors of all time. Emacs features almost infinite customizability of almost all of its features. GNU Emacs was initially released in 1985, with an initial version of Emacs released in 1976.

|clearfix|

Before using Emacs, check out GNU's `guided tour of Emacs features`_. You can also check out EmacsMovies_ (basic) and `Emacs Rocks!`_ (advanced) for screencasts showcasing what the editor can do. After starting Emacs, press :kbd:`C-h t` (that's Emacs parlance for :kbd:`Control-h`, then :kbd:`t`) for the in-application Emacs tutorial. Another great guide is `Jessica Hamrick's Absolute Beginner's Guide to Emacs`_.

Like most GNU software, Emacs has a very detailed and complete manual that is `available online <https://gnu.org/software/emacs/manual/html_node/emacs/index.html>`_, as well within Emacs by entering :kbd:`C-h r` (that's :kbd:`Control-h`, then :kbd:`r`). No mention of Emacs would be complete without mentioning the gigantic resource that is EmacsWiki_.

Emacs is not difficult to use out-of-the-box, but requires customization and commitment to use effectively. We recommend using vanilla Emacs for a bit, then moving on to customization when you are comfortable. A great way to get started is to use a so-called *starter kit*, a collection of packages that include useful Emacs packages and turn on useful Emacs functionality disabled by default. Xah Lee maintains a `list of Emacs starter kits`_. Although all of these are good, we recommend `Emacs Prelude`_ because it is full-featured and always up-to-date.

Emacs 24 includes a package manager called ELPA_ (Emacs Lisp Package Archive). Its use is highly recommended. Two additional package archives that any Emacs user needs to know about are Marmalade_ and MELPA_.

Emacs is available for many platforms including Windows, Mac OS X, and GNU/Linux.

.. _GNU Emacs: https://gnu.org/software/emacs/
.. _guided tour of Emacs features: http://www.gnu.org/software/emacs/tour/
.. _EmacsMovies: http://emacsmovies.org/blog/where_to_begin/
.. _Emacs Rocks!: http://emacsrocks.com/
.. _Jessica Hamrick's Absolute Beginner's Guide to Emacs: http://www.jesshamrick.com/2012/09/10/absolute-beginners-guide-to-emacs/
.. _EmacsWiki: http://www.emacswiki.org/
.. _list of Emacs starter kits: http://ergoemacs.org/misc/list_of_emacs_starter_kits.html
.. _Emacs Prelude: https://github.com/bbatsov/prelude
.. _ELPA: http://www.emacswiki.org/emacs/ELPA
.. _Marmalade: https://marmalade-repo.org/
.. _MELPA: http://melpa.org/

Kate
----

.. Adapted from the "Kate's Mascot" blog post: http://kate-editor.org/2014/10/12/kates-mascot-kate-the-woodpecker/
.. image:: /images/editors/kate.png
    :align: left
    :alt: Kate mascot
    :target: Kate_

Kate_ (KDE Advanced Text Editor) is KDE's entry into the field of advanced text editors. Kate's `list of features <http://kate-editor.org/about-kate/>`_ is comparable to other editors of its class.

Although Kate is primarily used on GNU/Linux through KDE_, it is also available for Windows and Mac OS X.

|clearfix|

.. _Kate: http://kate-editor.org/

Others
------

The following are other advanced text editors not available on EOS. You can use these on your personal machine, and you may be able to install them on EOS manually.

Atom
~~~~

.. Adapted from 'resources/atom.png' in the Atom source tree.
.. image:: /images/editors/atom.png
    :align: left
    :alt: Atom logo
    :target: Atom_

Atom_ is an open-source, customizable text editor produced by GitHub_. As an editor, it seems to be in the spirit of Vim or Emacs, but using modern design principles and technologies. Atom comes with many useful features out-of-the box, including a fuzzy-finder, multiple cursors, and a package manager. Atom is based on the `Atom Shell`_, which is in turn based on `node.js`_ and Chromium_.

Atom is available on Windows, Mac OS X, GNU/Linux, and FreeBSD.

|clearfix|

.. _Atom: https://atom.io/
.. _GitHub: https://github.com/
.. _Atom Shell: https://github.com/atom/atom-shell
.. _node.js: http://nodejs.org/
.. _Chromium: http://www.chromium.org/

Sublime Text
~~~~~~~~~~~~

.. image:: /images/editors/sublime-text.png
    :align: left
    :alt: Sublime Text logo
    :target: `Sublime Text`_

`Sublime Text`_ is a free, proprietary, shareware advanced text editor. It features easy navigation within files, multiple selections, split panes, and a package manager, among other features. Sublime Text is very customizable and features a Python API.

Sublime Text is available for Windows, Mac OS X, and GNU/Linux.

|clearfix|

.. _Sublime Text: http://www.sublimetext.com/

Notepad++
~~~~~~~~~

.. image:: /images/editors/notepad-plus-plus.png
    :align: left
    :alt: Notepad++ logo
    :target: `Notepad++`_

`Notepad++`_ is a simple open-source editor for Windows. It supports split editing, syntax highlighting, and many other features come to be expected by an editor of this class.

|clearfix|

.. _Notepad++: http://notepad-plus-plus.org/

TextMate
~~~~~~~~

.. image:: /images/editors/textmate.png
    :align: left
    :alt: TextMate logo
    :target: TextMate_

TextMate_ is a popular advanced text editor for Mac OS X. Originally a proprietary product, TextMate is now free and open-source software. TextMate has been called the "culmination of Emacs and OS X" and features a slick but minimal interface, file browser, auto-pairing, simple completion, and many more features. TextMate has been particularly popular in the `Ruby on Rails`_ community.

|clearfix|

.. _TextMate: http://macromates.com/
.. _Ruby on Rails: http://rubyonrails.org/

Integrated Development Environments
===================================

Integrated development environments (IDEs) are the most complex class of text editors. Although editing is usually still at the forefront, the IDE's text editor is only a *component* of the larger program. Like advanced text editors, IDEs typically feature syntax highlighting, multiple panes, and many other editing features. Unlike advanced text editors, IDEs often feature deep integration with certain environments, such as semantic code completion, support for refactoring, graphical user interface (GUI) composers, and ability invoke test harnesses or debuggers directly from the editing interface. IDEs also have a focus on projects as opposed to individual files.

IDEs often focus on a specific language or environment. As such, for people who work in multiple environments, the choice is often between use of a single advanced text editor for all environments or use of an individual IDE for each environment.

BlueJ
-----

.. From http://blueroom.bluej.org/
.. image:: /images/editors/bluej.png
    :align: left
    :alt: BlueJ logo
    :target: BlueJ_

BlueJ_ is a beginner's IDE for Java. Its interface offers the ability to selectively instantiate classes and run methods with different parameters, making it excellent for learning. BlueJ also features an object inspector which allows examination of objects as they progress through a software instance's life cycle.

BlueJ is available for Windows, Mac OS X, and GNU/Linux.

|clearfix|

.. _BlueJ: http://www.bluej.org/

Eclipse
-------

.. Old logo from http://help.eclipse.org/juno/index.jsp?topic=%2Forg.eclipse.platform.doc.user%2FwhatsNew%2Fplatform_whatsnew.html
.. New logo cropped from http://www.eclipse.org/artwork/
.. image:: /images/editors/eclipse.png
    :align: left
    :alt: Eclipse logo
    :target: Eclipse_

Eclipse_ is an extensible, feature-complete, free and open-source IDE. Although Eclipse is written in and was initially written for Java, it also supports many other languages and environments. By default, Eclipse on EOS supports Java, PHP, Python, C, C++, and Android.

|clearfix|

Popular language/environment plugins for Eclipse include:

- `Eclipse JDT`_ (Java Development Tools)
- `Eclipse CDT`_ (C/C++ Development Tooling)
- `Eclipse PDT`_ (PHP Development Tools)
- PyDev_ (Python)
- NodeClipse_ (JavaScript and Node.JS)
- ADT_ (Android Development Tools)
- `Aptana Studio`_ (HTML5, CSS3, JavaScript, Ruby, Rails, PHP, Python)

Eclipse is available for Windows, Mac OS X, and GNU/Linux.

.. _Eclipse: https://www.eclipse.org/home/index.php
.. _Eclipse JDT: http://www.eclipse.org/jdt/
.. _Eclipse CDT: http://www.eclipse.org/cdt/
.. _Eclipse PDT: http://www.eclipse.org/pdt/
.. _PyDev: http://pydev.org/
.. _NodeClipse: http://www.nodeclipse.org/
.. _ADT: http://developer.android.com/tools/sdk/eclipse-adt.html
.. _Aptana Studio: http://www.aptana.com/index.html

IntelliJ IDEA
-------------

.. Cropped from the SVG at https://www.jetbrains.com/company/press/materials.html#idea
.. image:: /images/editors/intellij.png
    :align: left
    :alt: IntelliJ IDEA logo
    :target: `IntelliJ IDEA`_

`IntelliJ IDEA`_ (colloquially known as "IntelliJ") is a professional IDE for Java and other languages developed by developer tool company JetBrains_. IntelliJ's primary advantage over other IDEs and editors is deep integration with many specific languages and technologies. IntelliJ is available in two versions: Community and Ultimate. The Community edition is free and open-source software, while the Ultimate edition includes more features for a price. For details on specific features, consult `IntelliJ's advertised feature list`_ or :wikipedia:`Wikipedia's list of IntelliJ features <IntelliJ_IDEA#Features>`.

|clearfix|

IntelliJ is available for Windows, Mac OS X, and GNU/Linux. On EOS, IntelliJ may be started from the command line with::

    idea.sh

.. _IntelliJ IDEA: https://www.jetbrains.com/idea/
.. _JetBrains: https://www.jetbrains.com/
.. _IntelliJ's advertised feature list: https://www.jetbrains.com/idea/features/

Visual Studio
-------------

.. From http://flakshack.deviantart.com/art/Visual-Studio-2012-icon-342054061
.. image:: /images/editors/visual-studio.png
    :align: left
    :alt: Visual Studio logo
    :target: `Visual Studio`_

`Visual Studio`_ is an IDE for Windows developed and maintained by Microsoft_. It is primarily aimed at development of applications and libraries for Microsoft platforms, including Windows_, `Windows Phone`_, `Microsoft Silverlight`_, and IIS_. Visual Studio's supported languages include C, C++, C#, F#, and Visual Basic. Visual Studio also supports Python through PyTools_ and web development with HTML, CSS, JavaScript, and ASP.NET_. The IDE has almost all modern features including IntelliSense code completion, refactoring support, and integrated debugger, graphical interface and web design tools, and a database editor. ReSharper_ by JetBrains_ is a Visual Studio add-on considered necessary by many .NET developers.

Visual Studio is the recommended IDE when developing exclusively for Microsoft platforms.

|clearfix|

.. _Visual Studio: http://www.visualstudio.com/
.. _Microsoft: http://www.microsoft.com/
.. _Windows: http://windows.microsoft.com/
.. _Windows Phone: http://www.windowsphone.com/
.. _Microsoft Silverlight: http://www.microsoft.com/silverlight/
.. _IIS: http://www.iis.net/
.. _PyTools: http://pytools.codeplex.com/
.. _ASP.NET: http://www.asp.net/
.. _ReSharper: https://www.jetbrains.com/resharper/

Xcode
-----

.. From https://itunes.apple.com/us/app/xcode/id497799835?mt=12
.. Had to remove the built-in color profile to get it to export correctly in Gimp after resizing; see https://bugs.archlinux.org/task/35363
.. image:: /images/editors/xcode.png
    :align: left
    :alt: Xcode logo
    :target: Xcode_

Xcode_ is an IDE for Mac OS X developed and maintained by Apple_. It is primarily aimed at development of Mac OS X and iOS Cocoa_ applications written in Objective-C and/or Swift_. Xcode includes :wikipedia:`Interface Builder <Interface_Builder>` for composition of user interfaces, the `Apple LLVM Compiler`_ based on Clang_ and LLVM_, a graphical debugger based on LLDB_, and Instruments_, a tracing and profiling tool based on :wikipedia:`DTrace`. It also features excellent code completion, also implemented using Clang_. For more information, see the `full list of Xcode features`_.

In addition to Objective-C and Swift, Xcode supports development in C, C++, Python, Ruby, and AppleScript. [#xcode-langs]_

If you are developing native Mac OS X or iOS applications, Xcode is the recommended IDE.

|clearfix|

.. _Xcode: https://developer.apple.com/xcode/
.. _Apple: http://www.apple.com/
.. _Cocoa: https://developer.apple.com/technologies/mac/cocoa.html
.. _Swift: https://developer.apple.com/swift/
.. _Apple LLVM Compiler: https://developer.apple.com/Library/mac/documentation/CompilerTools/Conceptual/LLVMCompilerOverview/index.html
.. _Clang: http://clang.llvm.org/
.. _LLVM: http://llvm.org/
.. _LLDB: http://lldb.llvm.org/
.. _Instruments: https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Introduction/Introduction.html
.. _full list of Xcode features: https://developer.apple.com/xcode/features/

.. _qt-creator:

Qt Creator
----------

.. Extracted and rendered from 'src/tools/icons/applicationicons.svg' in the Qt Creator source tree
.. image:: /images/editors/qt-creator.png
    :align: left
    :alt: Qt Creator logo
    :target: `Qt Creator`_

`Qt Creator`_ is an IDE for developing applications using the :ref:`qt-section` cross-platform framework. Qt Creator supports C++ and `QtQuick/QML`_ (JavaScript), two languages used for developing Qt applications. It also includes project navigation tools, code completion, an integrated debugger based on GDB_, and a drag-and-drop interface designer (formerly known as Qt Designer). Additionally, Qt Designer supports integration with various build systems. A full feature list is available on the homepage.

|clearfix|

Qt Creator is the recommended IDE if you are developing cross-platform applications in :ref:`qt-section`. Qt Creator is available on all platforms Qt is available, which includes Windows, Mac OS X, and GNU/Linux.

.. _Qt Creator: http://qt-project.org/wiki/Category:Tools::QtCreator
.. _GDB: http://www.gnu.org/software/gdb/

Geany
-----

.. Rendered from 'geany/icons/scalable/geany.svg' in the Geany source tree
.. image:: /images/editors/geany.png
    :align: left
    :alt: Geany logo
    :target: Geany_

Geany_ is a lightweight IDE based on Scintilla_. It includes syntax highlighting of numerous languages, project support, simple code completion, and code navigation. In addition, Geany includes support for invoking build systems through external tools. Geany is a good choice if you want to use a consistent interface for many different languages and basic IDE features for development.

|clearfix|

Geany is available for Windows, Mac OS X, and GNU/Linux.

.. _Geany: http://geany.org/
.. _Scintilla: http://www.scintilla.org/

Bluefish
--------

.. Rendered from 'bluefish/images/bluefish-icon.svg' in the Bluefish source tree
.. image:: /images/editors/bluefish.png
    :align: left
    :alt: Bluefish logo
    :target: Bluefish_

Bluefish_ is a lightweight IDE primarily aimed at web development. On the web development side, Bluefish supports PHP, ASP.NET, ColdFusion, Java Server Pages (JSP), and Wordpress as well as the standard HTML, CSS, and JavaScript. In addition to that, Bluefish includes support for C, C++, Python, Ruby, and SVG, among others. One of Bluefish's interesting features is integration of external scripts by sending the document text through a pipe to the script. For more information, see the `full list of Bluefish features`_.

Bluefish is available for Windows, Mac OS X, and GNU/Linux.

|clearfix|

.. _Bluefish: http://bluefish.openoffice.nl/
.. _full list of Bluefish features: http://bluefish.openoffice.nl/features.html

For a full list of text editors, please see Wikipedia's :wikipedia:`list of text editors <List_of_text_editors>` and :wikipedia:`comparison of text editors <Comparison_of_text_editors>`.

Others
------

The following are other IDEs not available on EOS. You can use these on your personal machine, and you may be able to install them on EOS manually.

NetBeans
~~~~~~~~

.. Grabbed one of the vectors from here, imported to Inkscape and cropped: https://netbeans.org/community/teams/evangelism/collateral.html#logos
.. image:: /images/editors/netbeans.png
    :align: left
    :alt: NetBeans logo
    :target: NetBeans_

NetBeans_ is a free and open-source IDE for Java and others sponsored by Oracle_. Although Java is the main focus of NetBeans, it also supports PHP, C and C++, and web development. One of the more popular features of NetBeans is its integrated GUI builder for Java/:wikipedia:`Swing <Swing_(Java)>`.

|clearfix|

NetBeans is available for Windows, Mac OS X, and GNU/Linux.

.. _NetBeans: https://netbeans.org/
.. _Oracle: http://www.oracle.com/index.html

EditorConfig
============

.. From http://editorconfig.org/logo.png
.. image:: /images/editors/editorconfig.png
    :align: left
    :alt: EditorConfig logo
    :target: EditorConfig_

If your project is developed by a team or you work with multiple editors, consider using EditorConfig_. EditorConfig plugins for various editors allow developers to maintain a consistent formatting style throughout the projects, supporting such things as tabs vs. spaces, tab width, end of line characters, and character encoding, among others (`full list here <http://editorconfig.org/#supported-properties>`_). Many editors listed in this section are supported.

|clearfix|

*All logos are copyrights of their respective projects.*

.. [#xcode-langs] According to the :wikipedia:`Wikipedia Xcode article <Xcode#Composition>`.
