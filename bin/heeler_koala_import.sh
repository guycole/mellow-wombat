#!/bin/bash
#
# Title: heeler_koala_import.sh
# Description: import koala files 
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
#
SOURCE_DIR="/var/wombat/heeler/koala"
KOALA_IMPORT="/home/wombat/Documents/github/mellow-koala/bin/import_heeler"
#
for FILE in "$SOURCE_DIR"/*; do
  [ -f "$FILE" ] || continue

  "$KOALA_IMPORT" "$FILE"
  if [ $? -eq 0 ]; then
    rm "$FILE"
  else
    echo "ERROR: import failed for $FILE" >&2
  fi
done
#
