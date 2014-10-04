Command Line (SCP)
==================

Files can be transferred on the command line using a utility called SCP. Because SCP uses SSH for authentication, if you have set up |ssh-keys|, you will not have to type any passwords. SCP stands for *Secure Copy* and works very similar to the ``cp`` command, except that it can also transfer files across the network. Make sure you are familiar with the operation of ``cp`` before using SCP.

Each file can be prefixed with a machine name, which tells SCP where it is or should be located. Files with no prefix are assumed to be on the local machine. Paths on the remote machine start at your home directory, so there is typically no need to include :file:`/home/smithj` in the path. Here are some examples of use of SCP::

    # Typical upload
    scp classes/cis162/hw1.txt eos01.cis.gvsu.edu:classes/cis162
    # Typical download
    scp eos01.cis.gvsu.edu:classes/cis162/hw2.txt classes/cis162
    # Upload a directory
    scp -r projects eos01.cis.gvsu.edu:classes/cis163
    # Include username as well
    scp smithj@eos01.cis.gvsu.edu:classes/cis162/hw3.txt classes/cis162
    # Hostname aliases make this easier
    scp eos01:classes/cis162/hw4.txt classes/cis162
