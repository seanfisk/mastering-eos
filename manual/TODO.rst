======
 TODO
======

* Add link to EOS basics: http://www.cis.gvsu.edu/Facilities/eosLabs/. Mention the caveat of not being up-to-date.
* Write a script which SSH'es into all the machines and checks for requisite software.
* Include technical details in contributing section.

* Raise awareness
    * Add note to ``/etc/motd``
        * ``eos-web-docs`` (use the script in ``scripts/``)
        * ``man eos``
        * ``info eos``
    * Add shortcut to users' desktop?

* Remote
    * SSHFS (Mac and Linux, suggest ExpandDrive for Windows)
    * rsync
    * X forwarding
    * Add this link: http://www.techrepublic.com/blog/it-security/use-putty-as-a-secure-proxy-on-windows/

* Shells / PATH
    * Focus on Bash and just mention other shells at the end
    * Add path manip section
    * Add prompt customization section
    * "Next class" Python module in prompt, e.g., ``<CIS452 in 01:42>``.

* Add section on 'Mining Hardware/Software Information'.
    * Finding versions of programs
    * Finding OS versions
    * Hardware information
    * Web server details (info.php)

* Installing software
    * Manual compilation
    * Linuxbrew
    * Local install scripts
    * Specific environments
        * Python (https://github.com/yyuu/pyenv)
        * Ruby (https://github.com/sstephenson/rbenv)
        * Java (https://github.com/gcuisinier/jenv)

* Expand DB section; add PostgreSQL

* List of GUI libraries

* HPC? (Threading, OpenMP, MPI, C++, Python)

* Later, tryout http://www.mremoteng.org/ and http://terminals.codeplex.com/.

* Change theme to use GVSU colors. Use black, white, the 3 blue shades from the home page, and the official blue (Pantone).

Ira
===

* Be clear about keycard Datacomm vs. EOS/Arch access.

* Sean asks: Are we going to deploy man and info pages? They are commented out right now because they haven't been updated in a while. If we aren't going to keep them updated, we should remove them from the systems.

* Sean asks: Is it OK to use the GVSU favicon?

* Sean asks: Is it possible to install Remmina on EOS?
