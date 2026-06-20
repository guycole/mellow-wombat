#!/bin/bash
#
# Title: catalog.sh
# Description: write catalog.json to s3
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
# 

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_DIR=$(cd "${SCRIPT_DIR}/.." && pwd)
SOURCE_FILE="${REPO_DIR}/infra/var/wombat/admin/catalog.json"
S3_URI="s3://mellow-wombat.braingang.net/wombat/admin/catalog.json"

if [[ ! -f "$SOURCE_FILE" ]]; then
    echo "Error: source file not found: $SOURCE_FILE" >&2
    exit 1
fi

epoch_utc=$(date -u +%s)
iso_utc=$(python3 -c 'from datetime import datetime, timezone; import sys; print(datetime.fromtimestamp(int(sys.argv[1]), tz=timezone.utc).isoformat())' "$epoch_utc")

temp_file=$(mktemp)
trap 'rm -f "$temp_file"' EXIT

python3 - "$SOURCE_FILE" "$temp_file" "$epoch_utc" "$iso_utc" <<'PY'
import json
import sys

source_path, target_path, epoch_value, iso_value = sys.argv[1:5]

with open(source_path, "r", encoding="utf-8") as handle:
    payload = json.load(handle)

payload["creationEpochTime"] = int(epoch_value)
payload["creationIso8601Time"] = iso_value

with open(target_path, "w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=4)
    handle.write("\n")
PY

aws s3 cp "$temp_file" "$S3_URI" --profile wombat

echo "Uploaded catalog.json to $S3_URI"
echo "creationEpochTime=$epoch_utc"
echo "creationIso8601Time=$iso_utc"