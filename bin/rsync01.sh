#!/bin/bash
# generated for: wombat01
# epoch: 1773616624
# ISO8601: 2026-03-15T23:17:04+00:00
#
# must run from gateway
#
DEST_DIR=/var/wombat
SRC_DIR=/var/wombat/fresh
#
rsync -av /var/wombat/admin wombat@c4c:${DEST_DIR}
rsync -av --remove-source-files wombat@c4c:${SRC_DIR} ${DEST_DIR}
rsync -av /var/wombat/admin wombat@pi3c:${DEST_DIR}
rsync -av --remove-source-files wombat@pi3c:${SRC_DIR} ${DEST_DIR}
rsync -av /var/wombat/admin wombat@pi4a:${DEST_DIR}
rsync -av --remove-source-files wombat@pi4a:${SRC_DIR} ${DEST_DIR}
#
