==============
 GUI Toolkits
==============

For many programs, you may find that a console or command-line interface is not enough. In this case, consider using a library to build a graphical user interface (GUI). Below are the most common GUI toolkits and bindings to various languages. Though you may find bindings of various quality on the Net, care has been taken to include only official or high-quality maintained bindings in this list. Consider the listed bindings the ones recommended by the authors.

Using a cross-platform toolkit is best when you need to target multiple platforms for your application. All of these toolkits support use of a common code base for multiple operating systems.

Please see :wikipedia:`Wikipedia's list of GUI toolkits <List_of_widget_toolkits>` for a fuller list.

.. note::

    Although you can use all of these toolkits on EOS systems, this information is not specific to EOS.

Choosing a Toolkit
==================

Choosing a cross-platform toolkit can be a challenge. It is an important decision because it typically represents a commitment to a specific toolkit. There are a few different issues to consider before making this decision.

The first consideration is whether the toolkit uses *native widgets*. Toolkits that use native widgets (native toolkits) call platform-specific APIs to render widgets on the screen. Since native APIs are used, these toolkits often produce applications which look closer to other applications on the platform. They also sometimes offer better system integration.

Non-native toolkits draw their own widgets on the screen using graphics APIs. Because native APIs are not used, widgets typically have more consistent behavior between platforms.

A second consideration is the language of development. You will typically want to choose a toolkit that has a binding for your language of choice. However, it is not uncommon for the GUI toolkit to *determine* the language of development.

Third, some of the toolkits mentioned offer more that just GUI abstractions. Of these, Qt offers the most features beyond a GUI library. wxWidgets offers more features as well. GTK+, Tk, Swing, and SWT are purely GUI libraries (although GTK+ is typically used with GLib_, while Swing and SWT are used with the Java standard library).

The final (and possibly most important) consideration is the level of maintenance of the library binding and the library itself. Because GUI libraries and application are typically high in complexity, it is highly suggested that you choose an official or well-maintained binding. Choosing a subpar library typically results in many issues and general frustration.

Qt
===

Qt_ is a high-quality cross-platform application framework which includes a full-featured GUI library. Qt applications run on Windows, Mac OS X, GNU/Linux, Android, and iOS. Qt is free to use for both open-source and commercial applications (though some of its bindings are not). The KDE_ GNU/Linux desktop environment is developed using Qt. Qt does not use native widgets, but uses native style APIs to render its widgets for a look and feel that is usually consistent with the platform.

Bindings
--------

- **C++:** Native (built-in)
- **JavaScript:** `QtQuick/QML`_ (built-in)
- **Python:** PyQt_ (free for open-source, but not commercial)

Also see Wikipedia's list of bindings for :wikipedia:`Qt 4 <List_of_language_bindings_for_Qt_4>` and :wikipedia:`Qt 5 <List_of_language_bindings_for_Qt_5>`.

Tools
-----

Qt has an official IDE, :wikipedia:`Qt Creator <Qt_Creator>`, which includes a code editor and GUI designer.

.. _Qt: http://qt-project.org/
.. _KDE: https://www.kde.org/
.. _QtQuick/QML: http://qt-project.org/doc/qt-5/qmlapplications.html
.. _PyQt: http://www.riverbankcomputing.com/software/pyqt/intro

wxWidgets
=========

wxWidgets_ is a popular cross-platform GUI toolkit. wxWidgets applications run on Windows, Mac OS X, and GNU/Linux. wxWidgets and most of its bindings are free to use for both open-source and commercial applications. wxWidgets is a fully native toolkit, meaning that it uses native APIs for all of its widgets.

.. _wxWidgets: http://wxwidgets.org/

Bindings
--------

- **C++:** Native
- **Python:** wxPython_
- **PHP:** wxPHP_
- **Haskell:** wxHaskell_
- **Perl:** wxPerl_

Also see the :wikipedia:`Wikipedia list of wxWidgets bindings <List_of_language_bindings_for_wxWidgets>`.

.. _wxPython: http://wxpython.org/
.. _wxPHP: http://wxphp.org/
.. _wxHaskell: http://www.haskell.org/haskellwiki/WxHaskell
.. _wxPerl: http://www.wxperl.it/

Tools
-----

wxGlade_ is the GUI designer tool for wxWidgets.

.. _wxGlade: http://wxglade.sourceforge.net/

GTK+
====

`GTK+`_ is a popular and complete cross-platform library for GUI programming. GTK+ applications run on Windows, Mac OS X, and GNU/Linux. GTK+ and most of its bindings are free to use for both open-source and commercial applications. Many popular GNU/Linux desktop environments are written using GTK+, including GNOME_, Xfce_ and Ubuntu's Unity_. GTK+ is a non-native toolkit, and renders its widgets using Cairo_.

.. note::

    Although GTK+ is purely a GUI library, it is typically used with GLib_, which offers many other application features.

.. _GTK+: http://www.gtk.org/
.. _GNOME: http://www.gnome.org/
.. _Xfce: http://xfce.org/
.. _Unity: https://unity.ubuntu.com/
.. _GLib: https://developer.gnome.org/glib/
.. _Cairo: http://cairographics.org/

Bindings
--------

The GTK+ Project maintains `a list of language bindings and their status <http://www.gtk.org/language-bindings.php>`_. The more popular ones include:

- **C:** Native (official)
- **C++:** gtkmm_ (official)
- **Python:** PyGObject_ (official) [note: PyGTK_ not recommended for new programs]
- **JavaScript:** `Gjs and Seed`_
- **C#:** `Gtk#`_ (official, but incomplete)

Also see the :wikipedia:`Wikipedia list of GTK+ bindings <List_of_language_bindings_for_GTK%2B>`.

.. _gtkmm: http://www.gtkmm.org/
.. _PyGObject: http://live.gnome.org/PyGObject
.. _PyGTK: http://www.pygtk.org/
.. _Gjs and Seed: https://wiki.gnome.org/JavaScript
.. _Gtk#: http://www.mono-project.com/docs/gui/gtksharp/

Tools
-----

Glade_ is the official GUI designer tool for GTK+.

.. _Glade: https://glade.gnome.org/

Tk
===

Tk_ is a relatively basic cross-platform GUI toolkit. Tk applications run on Windows, Mac OS X, and GNU/Linux. Tk and most of its bindings are free to use for both open-source and commercial applications. Tk is

Bindings
--------

- **Tcl:** Native
- **C:** Native
- **Python:** :wikipedia:`Tkinter`
- **Perl:** `Perl/Tk`_
- **Ruby:** `Ruby/Tk`_

.. _Tk: http://www.tcl.tk/
.. _Perl/Tk: http://search.cpan.org/~ni-s/Tk-804.027/pod/UserGuide.pod
.. _Ruby/Tk: http://ruby-doc.com/docs/ProgrammingRuby/html/ext_tk.html

Swing
=====

:wikipedia:`Swing <Swing_%28Java%29>` is the most popular GUI toolkit for Java and is part of the Java standard library. As part of Java, Swing applications run for the most part wherever Java runs. Swing is a non-native toolkit, and draws all of its widgets using Java graphics APIs.

SWT
===

SWT_ (Standard Widget Toolkit) is cross-platform GUI toolkit for Java programs and an alternative to Swing. SWT applications run on Windows, Mac OS X, and GNU/Linux. The main difference between Swing and SWT is that SWT is a native toolkit, meaning that its widgets are wrappers around native APIs (using :wikipedia:`JNI <Java_Native_Interface>`) whenever possible.

SWT's notable user and maintainer is the Eclipse_ project, where it is used to create the GUI for the Eclipse IDE.

.. _SWT: http://www.eclipse.org/swt/
.. _Eclipse: http://www.eclipse.org/

Native Toolkits
===============

Native toolkits are libraries which are usually designed for one platform only. Use these when cross-platform portability is not a concern. We recommend considering :wikipedia:`Windows Presentation Foundation <Windows_Presentation_Foundation>` on Windows and Cocoa_ on Mac OS X. On GNU/Linux, depending on the desktop environment used, Qt_ (for KDE) and `GTK+`_ (most others) *are the native toolkits*.

.. _Cocoa: https://developer.apple.com/technologies/mac/cocoa.html
