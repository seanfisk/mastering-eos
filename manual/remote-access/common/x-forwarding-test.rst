From your remote shell, try running a graphical program::

    gedit

You may want to send the program to the background to regain use of the shell::

    gedit &

X11 is a heavyweight protocol, and X11 sessions function best on high bandwidth, low latency connections. Remote applications running through X forwarding will typically be much less responsive than if they were running on an EOS machine. If you experience performance problems (and you probably will, depending on the applications that you use), consider using VNC. X forwarding is good for one-off applications, like viewing images or PDFs, but typically not good for editing text, web browsing, or running full desktop sessions. Always keep this in mind when using this technology.
