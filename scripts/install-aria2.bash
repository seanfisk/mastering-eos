mkdir -p ~/.local/src
cd ~/.local/src
wget 'http://downloads.sourceforge.net/project/'\
'aria2/stable/aria2-1.17.0/aria2-1.17.0.tar.gz'
tar -xf aria2-1.17.0.tar.gz
cd aria2-1.17.0
./configure --prefix ~/.local
make # builds the program
make install # installs program to ~/.local/bin
export PATH=~/.local/bin:$PATH # consider adding to ~/.bash_profile
aria2c 'http://www.irs.gov/pub/irs-pdf/fw4.pdf'
