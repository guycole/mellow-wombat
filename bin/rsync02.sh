#!/bin/bash
# generated for: wombat02
# epoch: 1772348236
# ISO8601: 2026-03-01T06:57:16+00:00
#
# must run from gateway
#
DEST_DIR=/var/wombat
SRC_DIR=/var/wombat/fresh
#
#
rsync -av --remove-source-files wombat@c4d:${SRC_DIR} ${DEST_DIR}
rsync -av --remove-source-files wombat@pi4c:${SRC_DIR} ${DEST_DIR}
rsync -av --remove-source-files wombat@pi4o:${SRC_DIR} ${DEST_DIR}
#
#
