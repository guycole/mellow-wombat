#
#ansible-playbook -vvv -i inventory.yaml apt-update.yaml --extra-vars "target_hosts=wombat02"
ansible-playbook -i inventory.yaml apt-update.yaml --extra-vars "target_hosts=wombat01"
#
