mkdir -p ~/.local/src                           # Create directory for source code
cd ~/.local/src
wget 'http://downloads.sourceforge.net/project/'\
'aria2/stable/aria2-1.17.0/aria2-1.17.0.tar.gz' # Download aria2 source code
tar -xf aria2-1.17.0.tar.gz                     # Unarchive source code
cd aria2-1.17.0
./configure --prefix ~/.local                   # Set up build configuration
make                                            # Build the program
make install                                    # Install program to ~/.local/bin
export PATH=~/.local/bin:$PATH                  # Consider adding to ~/.bash_profile
aria2c 'http://www.irs.gov/pub/irs-pdf/fw4.pdf' # Download the W4
