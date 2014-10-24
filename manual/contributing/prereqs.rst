.. _contributing-prereqs:

================
 Pre-requisites
================

Before running any commands, make sure you change to the repository root directory. For example::

    cd ~/mastering-eos

All following commands will be run from this directory unless otherwise noted.

Install Requirements
====================

Now that you have the source code, the first step in building the manual is to install the Python requirements. For this, we need to install Pip_, the Python package manager, to our `user site`_::

    wget https://bootstrap.pypa.io/get-pip.py -O - | python - --user

For the technical details on what this is doing, please see the `Pip installation docs`_.

Pip should now be installed to :file:`~/.local/bin/pip`. However, we don't want to have to type the full path every time we want to run :file:`pip` or any other executable installed there.. To remedy this, add the following to your :file:`~/.bash_profile`::

    export PATH=~/.local/bin:$PATH

Restart your shell to effect the changes to your :file:`~/.bash_profile` *by logging out and logging back in.* Run the following to ensure that this worked:

.. code-block:: console

    $ pip --version
    pip 1.5.6 from /home/smithj/.local/lib/python2.7/site-packages (python 2.7)

After installing Pip, use Pip to install this project's requirements to your user site::

    pip install --user -r requirements.txt --allow-external pyPEG2 --allow-unverified pyPEG2

The extra options are required for pyPEG2_ to override certain checks recently added by Pip.

The Python requirements for the project have now been met.

.. _Pip: http://pip.readthedocs.org/en/latest/index.html
.. _user site: http://legacy.python.org/dev/peps/pep-0370/
.. _Pip installation docs: http://pip.readthedocs.org/en/latest/installing.html#install-pip
.. _pyPEG2: https://pypi.python.org/pypi/pyPEG2

Configure Your Editor
=====================

EditorConfig
------------

We use EditorConfig_ to maintain consistent formatting between developers. Our EditorConfig preferences are recorded in the :file:`.editorconfig` file in the root of the repository.

If you do not have an editor preference, we suggest that you use gedit_ for the following reasons:

* It is simple and lightweight.
* It has EditorConfig support.
* It is already installed on EOS.

An editor is a very personal choice, so if you do have an editor preference, please use the editor with which you are comfortable. There are `EditorConfig plugins`_ for many different editors. If yours is listed, we suggest you take the time to get your editor's plugin working. If you cannot get it working or there is no EditorConfig support for your editor, please read the :file:`.editorconfig` file for the formatting standards --- they should be relatively easy to follow manually.

If you do choose gedit, we have a script in our repository to assist in installing EditorConfig support on EOS. To install the plugin, run::

    scripts/install-gedit-editorconfig-eos

This installs the gedit EditorConfig plugin, but we still need to enable it. Open gedit with::

    gedit

Then open the gedit preferences by clicking the application's icon (in GNOME):

.. image:: /images/gedit/preferences.png
   :alt: gedit Preferences

Select the :guilabel:`Plugins` tab, then scroll down and check the :guilabel:`EditorConfig` plugin to enable:

.. image:: /images/gedit/plugins.png
   :alt: gedit Plugins Dialog

The checkbox should become checked. If it turns to a red warning sign, please `report an issue`_. EditorConfig is now enabled for gedit!

Git Configuration
-----------------

We want to set up gedit as the editor for Git commit messages. Do this with::

    git config --global core.editor 'gedit --wait'

We use the ``--wait`` flag here because Git expects the editor to block until the commit message has been finished.

gedit also creates backup files of each file that you save. These files end with a tilde (``~``) and get annoying when they clutter the output of ``git status``. Fortunately, we can tell Git to ignore them. Run the following:

.. code-block:: console

    $ cat > ~/.gitignore-global <<EOF
    # gedit backup files
    *~
    EOF
    $ git config --global core.excludesfile '~/.gitignore-global'

Your editor has now been set up for developing |title|!

.. _gedit: https://wiki.gnome.org/Apps/Gedit
.. _EditorConfig: http://editorconfig.org/
.. _EditorConfig plugins: http://editorconfig.org/#download

SSH Setup
=========

Part of building the documentation is building the table of SSH fingerprints containing a fingerprint for each EOS machine. SSH is used to generate this table. Follow the directions in the following sections to correctly set up SSH to allow this.

Shared and Persistent SSH Connections (optional)
------------------------------------------------

In theory, you should never have to fully rebuild the manual. However, in practice, sometimes a full rebuild is necessary. With a full rebuild, you will have to wait while the SSH fingerprints table is rebuilt. Since this can take a long time, we recommend that you set up shared and persistent SSH connections as shown in :ref:`gnu-linux-advanced-openssh`. These are known to dramatically decrease the build time if you have done a full rebuild within the time given to ``ControlPersist``.

Inter-EOS SSH Trust
-------------------

To be able to rebuild the fingerprints table without user intervention, please follow the steps in :ref:`inter-eos-trust` before continuing.
