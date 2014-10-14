=================================
 Machine/OS/Software Information
=================================

Finding OS versions
===================

The linux standard base (LSB) version, Distributor ID, OS Description, Release version, and codename can be found using the command::

    $ lsb_release -a
    No LSB modules are available.
    Distributor ID: CentOS
    Description:    CentOS release 6.5 (Final)
    Release:        6.5
    Codename:       Final


Finding versions of programs
============================

The typical command to determine the program in your path would be the following::

    <program name> --version

This is a defacto standard, thus may not work for all programs.  Be concious that there is no standard for displaying the version of the program, thus other unnessary information may be provided.  A sample of this is::

    $ python --version
    Python 2.7.5
