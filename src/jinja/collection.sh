#!/bin/bash
# generated for: wombat02
# epoch: 1771727223
# ISO8601: 2026-02-22T02:27:03+00:00
#
# must run from gateway
#
DEST_DIR=/var/wombat
SRC_DIR=/var/wombat/fresh
#
rsync -av --remove-source-files wombat@c4c:${SRC_DIR} ${DEST_DIR}
rsync -av --remove-source-files wombat@c4d:${SRC_DIR} ${DEST_DIR}
rsync -av --remove-source-files wombat@pi4c:${SRC_DIR} ${DEST_DIR}
rsync -av --remove-source-files wombat@pi4d:${SRC_DIR} ${DEST_DIR}
#
