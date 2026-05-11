#!/bin/bash
#
# Title: generator.sh
# Description: generate hosts, inventory, and rsync files from catalog
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_DIR=$(cd "${SCRIPT_DIR}/.." && pwd)
GENERATOR_DIR="${REPO_DIR}/src/generator"
VENV_ACTIVATE="${GENERATOR_DIR}/venv/bin/activate"
CATALOG_FILE="/var/wombat/admin/catalog.json"
HOSTS_NEW="${GENERATOR_DIR}/hosts.new"
HOSTS_TARGET="/etc/hosts"
INVENTORY_NEW="${GENERATOR_DIR}/inventory.new"
INVENTORY_TARGET="${REPO_DIR}/src/ansible/inventory.yaml"
RSYNC_NEW="${GENERATOR_DIR}/rsync.new"
RSYNC_TARGET="${REPO_DIR}/bin/rsync.sh"

if [[ $(id -u) -ne 0 ]]; then
    echo "Error: must run as root" >&2
    exit 1
fi

if [[ ! -f "$CATALOG_FILE" ]]; then
    echo "Error: catalog file not found: $CATALOG_FILE" >&2
    exit 1
fi

if [[ ! -d "$GENERATOR_DIR" ]]; then
    echo "Error: generator directory not found: $GENERATOR_DIR" >&2
    exit 1
fi

if [[ ! -f "$VENV_ACTIVATE" ]]; then
    echo "Error: virtualenv activate script not found: $VENV_ACTIVATE" >&2
    exit 1
fi

source "$VENV_ACTIVATE"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 is not available from virtualenv: $VENV_ACTIVATE" >&2
    exit 1
fi

pushd "$GENERATOR_DIR" >/dev/null

python3 make_hosts.py "$CATALOG_FILE"
install -m 0644 "$HOSTS_NEW" "$HOSTS_TARGET"
echo "Updated $HOSTS_TARGET"

python3 make_inventory.py "$CATALOG_FILE"
install -m 0644 "$INVENTORY_NEW" "$INVENTORY_TARGET"
echo "Updated $INVENTORY_TARGET"

python3 make_rsync.py "$CATALOG_FILE"
install -m 0755 -o wombat -g wombat "$RSYNC_NEW" "$RSYNC_TARGET"
echo "Updated $RSYNC_TARGET"

popd >/dev/null