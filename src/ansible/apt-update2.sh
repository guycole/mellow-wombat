#
ansible-playbook -vvv -i crate2-inventory.yaml apt-update.yaml  --extra-vars "target_hosts=crate02"
#