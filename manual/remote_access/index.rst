==================================
 Accessing EOS Remotely (SSH/VNC)
==================================

If you are not sitting in the EOS or Arch lab, EOS can be accessed from home using a protocol called Secure Shell (SSH). SSH allows you to remotely run commands on any EOS machine.

SSH is a command-line-only technology. However, graphical remote access is available through a protocol called Virtual Network Computing (VNC). VNC allows you access to a graphical desktop as if you were sitting at an EOS machine. Because the VNC protocol has no security of its own, our lab setup requires that you tunnel your VNC traffic through the SSH protocol. Each respective guide describes how to do this, but remember that you will first need to successfully set up SSH before attempting to use VNC.

The hostnames for the EOS machines are organized as follows: :samp:`eos{XX}.cis.gvsu.edu` where :samp:`{XX}` is 01 through 24 and :samp:`arch{XX}.cis.gvsu.edu` where :samp:`{XX}` is 01 through 10. Use these names to connect to a specific EOS machine.

Your SSH and VNC clients of choice depend on your machine's operating system.

.. toctree::
   :maxdepth: 2

   windows
   mac_os_x
   gnu_linux
