#!/bin/bash
#
# Title: heeler_archive.sh
# Description: archive heeler files to tar
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
#
if [[ $# -eq 0 ]] ; then
    echo "missing crate argument"
    exit 1
fi
#
TODAY=$(date '+%Y-%m-%d')
FILE_NAME="heeler-$1-${TODAY}.tgz"
#
DEST_DIR="archive"
SOURCE_DIR="success"
TO_S3_DIR="to_s3"
WORK_DIR="/var/wombat/heeler"
#
echo "start archive"
#
cd ${WORK_DIR}
mv ${SOURCE_DIR} ${DEST_DIR}
mkdir ${SOURCE_DIR}
tar -cvzf ${FILE_NAME} ${DEST_DIR}
mv ${FILE_NAME} ${TO_S3_DIR}
#
echo "cleanup"
rm -rf ${DEST_DIR}
#
echo "end archive"
#
