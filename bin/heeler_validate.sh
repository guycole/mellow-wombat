#!/bin/bash
#
# Title: heeler_validate.sh
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
echo "end validate"
#
