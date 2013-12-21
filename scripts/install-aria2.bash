mkdir -p ~/.local/src # create directory for source code
cd ~/.local/src
wget 'http://downloads.sourceforge.net/project/'\
'aria2/stable/aria2-1.17.0/aria2-1.17.0.tar.gz' # download aria2's source code archive
tar -xf aria2-1.17.0.tar.gz # unarchive source code
cd aria2-1.17.0
./configure --prefix ~/.local # set up build configuration
make # build the program
make install # install program to ~/.local/bin
export PATH=~/.local/bin:$PATH # consider adding to ~/.bash_profile
aria2c 'http://www.irs.gov/pub/irs-pdf/fw4.pdf' # download the W4
