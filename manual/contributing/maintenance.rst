===================
 Maintenance Tasks
===================

The |title| project is written and organized to minimize the amount maintenance required to keep it up-to-date. However, like any other project, some maintenance is required. This page attempts to document many of ways in which |title| needs to be maintained.

Automated
=========

The following tasks are automated, and should not have to be closely maintained:

- The number and list of EOS hosts. All ``eos``, ``arch``, and ``dc`` hosts are read from the :file:`/etc/hosts` file on ``eos01``.
- SSH fingerprints. Fingerprints are read from each EOS host detected in the last step.
- The VNC port/geometry mappings. These are read from the :file:`/etc/xinetd.d/vncts` file on ``eos01``.

The automation implies external maintenance of said files. Coordinate with |the-sysadmin| to manage changes. In addition, the automated tasks themselves may need to be updated if for some reason they break.

Documentation
=============

Although everything in the manual having to do with EOS needs to be kept up-to-date, we've identified some pieces that are likely to become out-of-date. These should be checked periodically.

- The quota in the :ref:`quota` section. We have considered automating this.
- Update versions of the example programs (Bash and EditorConfig) in :ref:`manual-install`.
- Ensure the software in :ref:`manual-install` still compiles without issue.
- Ensure that :ref:`linuxbrew-section` is still working as advertised.
- Ensure that :ref:`hardinfo-section` still compiles without issue.
- If the system administrator changes, update the name and email address in the Sphinx configuration file.
- Ensure that we still run each of the :ref:`databases` and that the login mechanisms still work.
- Ensure that the URL for :ref:`oracle-apex` is still accurate.
- Ensure that all advertised :ref:`editors` are still available on EOS. Those that aren't should be placed in their respective section's *Other* subsection.
- Ensure that :ref:`bash` 4 is still the default shell on EOS. At this time of writing, a user's default shell can't be changed. If it can in the future, make a note about this in :ref:`shell-interactive`.
- Ensure that :ref:`sh` still invokes Bash. That would be embarrassing if it isn't and we use it as an example.
- Ensure that all the steps outlined in :ref:`contributing` still work.
- Ensure that the :ref:`list of maintainers <maintainers>` stays up-to-date.

Project Infrastructure
----------------------

Producing great documentation is the main aim of |title|. However, certain project infrastructure is needed to maintain documentation of this complexity. Maintenance of this infrastructure is key to the project's continued success. Here are some areas of the project that need to be kept up-to-date.

Build System
------------

Our build system is Waf_. The Waf build system itself is bundled with the repository in the :file:`waf` file in the project root. We try to keep our version of Waf at the newest version, and it should be checked for updates periodically. Sometimes the updates break part of the build system, which then requires fixing. See the `Waf changelog`_ for a list of changes.

.. _Waf changelog: https://code.google.com/p/waf/source/browse/ChangeLog

Python Requirements
-------------------

Our Python package requirements file, :file:`requirements.txt`, contains a list of Python packages upon which our build depends. All of these requirements need to be periodically checked for updates. Application of the updates may break our build, which then of course needs to be fixed.

Python 3
--------

We would like to transition to Python 3 in the near future. The only thing currently preventing us from doing so is Fabric_. Fabric is an integral part of our build and to remove or replace it would be a significant disadvantage. `Fabric 2.x`_ is already in the works, and it appears that Python 3 compatibility will be added with this release.

When the project runs successfully under Python 3, use of the six_ module may be removed.

.. _Fabric: http://www.fabfile.org/
.. _Fabric 2.x: http://www.fabfile.org/roadmap.html#invoke-fabric-2-x-and-patchwork
.. _six: http://pythonhosted.org/six/
