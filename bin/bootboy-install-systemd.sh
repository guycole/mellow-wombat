#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

BOOTBOY_SRC="$ROOT_DIR/src/bootboy/bootboy.py"
SERVICE_SRC="$ROOT_DIR/infra/etc/systemd/system/bootboy.service"

if [[ ! -f "$BOOTBOY_SRC" ]]; then
  echo "ERROR: missing $BOOTBOY_SRC" >&2
  exit 2
fi

if [[ ! -f "$SERVICE_SRC" ]]; then
  echo "ERROR: missing $SERVICE_SRC" >&2
  exit 2
fi

echo "Installing bootboy script to /usr/local/bin/bootboy" >&2
sudo install -m 0755 "$BOOTBOY_SRC" /usr/local/bin/bootboy

echo "Installing systemd unit to /etc/systemd/system/bootboy.service" >&2
sudo install -m 0644 "$SERVICE_SRC" /etc/systemd/system/bootboy.service

echo "Reloading systemd and enabling bootboy" >&2
sudo systemctl daemon-reload
sudo systemctl enable --now bootboy.service

echo "Done. Check: systemctl status bootboy.service" >&2
