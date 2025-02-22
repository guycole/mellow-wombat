#!/bin/bash
#
# Title: hyena-cp.sh
# Description: copy files from hyena to wombat
# Development Environment: macOS Monterey 12.6.9
# Author: Guy Cole (guycole at gmail dot com)
#
# http://www.linuxproblem.org/art_9.html
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
echo "start move"
#cd /var/mellow/wombat-raw
cd /mnt/pp1/gsc/wombat
#scp -i ~/.ssh/id_rsa gsc@192.168.1.71:~/github/mellow-hyena/aws_export/* .
scp -i ~/.ssh/id_rsa gsc@rpi3b:/var/mellow/* .
echo "end move"
#
 scp -r -i ~/.ssh/id_rsa gsc@rpi3b:/var/mellow/* .
#
