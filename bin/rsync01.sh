#!/bin/bash
# generated for: wombat01
# epoch: 1772348485
# ISO8601: 2026-03-01T07:01:25+00:00
#
# must run from gateway
#
DEST_DIR=/var/wombat
SRC_DIR=/var/wombat/fresh
#
rsync -av --remove-source-files wombat@pi3c:${SRC_DIR} ${DEST_DIR}
rsync -av --remove-source-files wombat@c4c:${SRC_DIR} ${DEST_DIR}
#
#
#
