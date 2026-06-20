#!/bin/bash

set -euo pipefail

target_host=$(hostname -s)

if [[ -z "$target_host" ]]; then
	echo "Error: hostname -s returned an empty value" >&2
	exit 1
fi

ansible "${target_host}" -m ping -i inventory.yaml
