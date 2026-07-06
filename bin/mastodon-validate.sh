#!/bin/bash
#
# Title: mastodon-validate.sh
# Description: verify collection files and write stats
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
echo "start validate"
#
docker rm mastodon;docker run -v /var/wombat:/mnt/wombat --name mastodon mastodon:latest
#
#/home/wombat/github/mellow-wombat/bin/heeler-koala-import.sh
#
echo "end validate"
#
