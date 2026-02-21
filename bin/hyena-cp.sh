#!/bin/bash
#
# Title: hyena-mv.sh
# Description: copy files from collector to gateway
# Development Environment: ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
DEST_DIR=/var/wombat/hyena/fresh
SRC_DIR=/var/wombat/hyena
#
echo "start move"
#
rsync -av --remove-source-files wombat@odroidc4c:${SRC_DIR} ${DEST_DIR}
rsync -av wombat@odroidc4c:${SRC_DIR} ${DEST_DIR}

#
echo "end move"
#
