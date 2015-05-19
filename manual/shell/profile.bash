# Run for interactive Bash login shells

# Set umask for more privacy. Child processes inherit the umask from
# parent processes, so it is correct to put this in the profile, not
# the rc. See <http://en.wikipedia.org/wiki/Umask#Processes>.
umask u=rwx,g=,o=

# Prepend a path to a variable if the path exists.
# $1: the path variable name
# $2: the path to check and possibly prepend
path_prepend () {
  [[ -d "$2" ]] && eval "$1="'"$2:${!1}"'
}

# Add hierarchy directories to paths. Manually-installed programs
# (~/.local) should override Linuxbrew programs (~/.linuxbrew).
#
# Inspired by
# <https://technotales.wordpress.com/2010/09/19/managing-path-and-manpath/>
for prefix in ~/.linuxbrew ~/.local; do
  path_prepend PATH "$prefix/bin"
  path_prepend MANPATH "$prefix/share/man" # usual manpage install directory
  path_prepend MANPATH "$prefix/man" # older manpage install directory
  path_prepend INFOPATH "$prefix/share/info"
done

# Personal scripts directory
path_prepend PATH ~/bin

# Unset definition of path_prepend
unset -f path_prepend

# Export path variables
export PATH MANPATH INFOPATH

# Set the editor to use when a program needs to edit a file
export EDITOR='gedit --wait'

# Bash doesn't run the .bashrc for login shells -- only .bash_profile.
# However, we want to run everything in the .bashrc as well.
source ~/.bashrc
