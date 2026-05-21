# BootBoy

BootBoy is a one-shot boot-time configurator for mellow collectors.

## Demo behavior (current)

At boot, BootBoy:

1. Determines the system hostname.
2. Reads `/var/wombat/admin/{hostname}.json`.
3. Writes `/var/wombat/admin/bootboy.status.json` indicating success/failure.

## Install as a systemd service

From this repo on the target Linux host:

```bash
./bin/bootboy-install-systemd.sh
```

Useful commands:

```bash
systemctl status bootboy.service
journalctl -u bootboy.service -b --no-pager
cat /var/wombat/admin/bootboy.status.json
```

## Local/manual run

```bash
python3 src/bootboy/bootboy.py --admin-dir /var/wombat/admin --status-file /var/wombat/admin/bootboy.status.json
```
