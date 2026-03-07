#!/bin/bash
#
# Title: heeler_archive.sh
# Description: archive heeler files to tar
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
TODAY=$(date '+%Y-%m-%d')
FILE_NAME="heeler-${TODAY}.tgz"
#
SOURCE_DIR="archive"
WORK_DIR="/var/wombat/heeler"
#
echo "start archive"
#
cd ${WORK_DIR}
mv "success" ${SOURCE_DIR}
tar -cvzf ${FILE_NAME} ${SOURCE_DIR}
#
echo "cleanup"
rm -rf ${SOURCE_DIR}
#
echo "end archive"
#
