mkdir -p ~/.local/src
cd ~/.local/src
wget 'http://downloads.sourceforge.net/project/'\
'aria2/stable/aria2-1.17.0/aria2-1.17.0.tar.gz'
tar -xf aria2-1.17.0.tar.gz
./configure --prefix ~/.local
make # builds the program
make install # installs program to ~/.local/bin
export PATH=~/.local/bin:$PATH # consider adding to ~/.bashrc
aria2c 'http://cis.gvsu.edu/Facilities/eosLabs/'
