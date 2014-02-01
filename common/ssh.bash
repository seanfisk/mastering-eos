# Generate SSH key
ssh-keygen # Press Enter at each prompt
# Add new SSH key to authorized_keys
< ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
_trust_host() {
	ssh -o StrictHostKeyChecking=no -o ConnectTimeout=2 "$1" exit
}
# Trust all EOS machines
for i in {1..24}; do _trust_host "eos$(printf '%02d' $i)"; done
# Trust all Arch machines
for i in {1..8}; do _trust_host "arch$(printf '%02d' $i)"; done
ssh eos15 # Automatic login
