#!/bin/bash
#
# Title: admin_copy.sh
# Description: copy admin files from S3 to local directory
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
# 
# admin_copy.sh wombat04
#
set -euo pipefail

if [[ $# -ne 1 ]]; then
    echo "Usage: ./admin-copy.sh <profile>" >&2
    exit 1
fi

if [[ -z "${1// }" ]]; then
    echo "Error: profile must be a non-empty string" >&2
    exit 1
fi

PROFILE="$1"
SOURCE_URI="s3://mellow-wombat.braingang.net/wombat/admin/"
TARGET_DIR="/var/wombat/admin"

if ! command -v aws >/dev/null 2>&1; then
    echo "Error: aws CLI is not installed" >&2
    exit 1
fi

mkdir -p "$TARGET_DIR"

aws s3 sync "$SOURCE_URI" "$TARGET_DIR" --delete --profile "$PROFILE"

echo "Synchronized $SOURCE_URI to $TARGET_DIR using profile $PROFILE"