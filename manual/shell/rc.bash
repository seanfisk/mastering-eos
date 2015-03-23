# .bashrc
# Run for interactive Bash non-login shell

# Use a custom multiline prompt
PS1='\u@\H:\w (\s-\V:\l) [\t]
$ '

# Aliases and functions
alias ll='ls -l' # long format
alias la='ls -la' # long format, show all including hidden files
alias u='cd ..' # go up a directory
alias path-print='echo "${PATH//:/'$'\n''}"'
cdl() { cd "$1" && ls; } # cd then list
mk() { mkdir -p "$1" && cd "$1"; } # make a directory then cd to it

# Key bindings
## Control-j pipes stdout and stderr of the typed command to less
bind '"\C-j": " |& less\C-m"'
## Alt-j jumps up a directory using the 'u' alias
bind '"\ej": "u\C-m"'
