#!/bin/bash
#
# Title: heeler-validate.sh
# Description: verify collection files and write stats
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
echo "start validate"
#
docker rm heeler;docker run -v /var/wombat:/mnt/wombat --name heeler heeler:latest
#
/home/wombat/github/mellow-wombat/bin/heeler-koala-import.sh
#
echo "end validate"
#
