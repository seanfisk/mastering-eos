=================
Accessing Winserv
=================

Part of the department infrastructure is a Windows Server installation.  Accounts for this machine are given when needed, for example when taking a course that involves teaching on the Windows platform, or working on a project that requires a Windows based setup.  This server is named "winserv.cis.gvsu." and can be accessed via the Remote Desktop Protocol (RDP).  The following are methods for accessing Winserv from various RDP clients.

Common Settings for Any RDP Client
==================================

Despite the RDP client or platform you use, you will need to remember a few things:

- The machine's IP address may change; use the DNS name instead.
- If outside of the EOS network you will need to use the fully-qualified-domain-name, ``winserv.cis.gvsu.edu``.  While on the EOS network you can simply use ``winserv``.
- You must login to the CIS domain.  For instance, if your username is doej you would login with ``CIS\doej``.
- We self-sign our certificate.  You may want to instruct your client to save this information or you will have to accept a security warning each time you login.

From Windows with MSTSC
=======================

Microsoft provides the :program:`mstsc` program with all versions of Windows.  This program provides an RDP mechanism for connecting to hosts with RDP enabled.  You can find this command by searching for :program:`mstsc` or **Remote Desktop** in the start menu.

From Mac OS X Machine with CoRD
===============================

Newer versions of Microsoft's Remote Desktop Application for Mac OS X no longer work.  Fortunately the open-source rdesktop RDP implementation has been implemented for Mac OS X as a program called CoRD.

From a \*nix Machine with rdesktop
==================================

\*nix systems usually have the rdesktop tool in their repositories.  If not, it can most likely be built from source.  :program:`rdesktop` provides a geometry flag that accepts both screen percentages or resolutions from the command-line to help adjust the client to an appropriate size.  For instance, users can type::

    rdekstop winserv.cis.gvsu.edu -g 90%

to allow the client to take up 90% of their screen.  Alternatively they could type::

    rdekstop winserv.cis.gvsu.edu -g 1024x768

to force a resolution of 1024x768 pixels.
