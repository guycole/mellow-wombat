#!/bin/bash
#
# Title: hyena-validate.sh
# Description: verify collection files and write stats
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
echo "start validate"
#
docker rm hyena;docker run -v /var/wombat:/mnt/wombat --name hyena hyena:latest
#
#/home/wombat/github/mellow-wombat/bin/hyena-koala-import.sh
#
echo "end validate"
#
