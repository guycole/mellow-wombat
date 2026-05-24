#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

BOOTBOY_SRC="$ROOT_DIR/src/bootboy/bootboy.py"
SERVICE_SRC="$ROOT_DIR/infra/etc/systemd/system/bootboy.service"

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 not found (required by /usr/local/bin/bootboy)" >&2
  echo "Install on Debian/Raspberry Pi OS: sudo apt-get update && sudo apt-get install -y python3" >&2
  exit 2
fi

HOST_SHORT="$(hostname -s 2>/dev/null || hostname 2>/dev/null || echo "")"
HOST_SHORT="${HOST_SHORT%%.*}"
ADMIN_DIR="/var/wombat/admin"
CONFIG_PATH="$ADMIN_DIR/${HOST_SHORT}.json"

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

echo "Ensuring admin dir exists at $ADMIN_DIR" >&2
sudo mkdir -p "$ADMIN_DIR"

if [[ -n "$HOST_SHORT" && ! -f "$CONFIG_PATH" ]]; then
  echo "WARNING: missing $CONFIG_PATH" >&2
  echo "BootBoy will fail until you create it. Minimal example:" >&2
  echo "  sudo tee '$CONFIG_PATH' >/dev/null <<'JSON'" >&2
  echo "  { \"assigned\": \"your-app\" }" >&2
  echo "  JSON" >&2
fi

echo "Reloading systemd and enabling bootboy" >&2
sudo systemctl daemon-reload
sudo systemctl enable --now bootboy.service

echo "Done. Check: systemctl status bootboy.service" >&2
