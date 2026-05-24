# BootBoy

BootBoy is a one-shot boot-time configurator for mellow collectors.

## Demo behavior (current)

At boot, BootBoy:

1. Determines the system hostname.
2. Reads `/var/wombat/admin/{hostname}.json`.
3. Writes `/var/wombat/admin/bootboy.status.json` indicating success/failure.

BootBoy always attempts to write the status JSON even on early failures; if the
configured status path is not writable, it will write a fallback copy under
`/tmp/` and log the fallback path to stderr/journald.

If the config contains an `assigned` value that BootBoy knows about, it will
invoke a matching handler stub and record the outcome under `assignedInvoke` in
the status JSON (currently includes a stub for `heeler-v2`).

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

### Troubleshooting: "failed to setup mount namespacing"

If `systemctl start bootboy.service` fails with an error like:

```
failed to setup mount namespacing
```

your kernel/systemd environment likely doesn't support mount-namespace-based
hardening directives. Use the unit file from this repo (it avoids those
directives), then reload + restart:

```bash
sudo install -m 0644 infra/etc/systemd/system/bootboy.service /etc/systemd/system/bootboy.service
sudo systemctl daemon-reload
sudo systemctl restart bootboy.service
```

## Local/manual run

```bash
python3 src/bootboy/bootboy.py --admin-dir /var/wombat/admin --status-file /var/wombat/admin/bootboy.status.json
```
