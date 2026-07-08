# bootboy

BootBoy is a one-shot boot-time configurator: it reads a per-host tasking file on each collector and starts the assigned collection application.

See [README.md](README.md) for crate/gateway/collector terminology and the overall architecture. BootBoy implementation lives in [src/bootboy/bootboy.py](src/bootboy/bootboy.py); detailed service notes are in [src/bootboy/README.md](src/bootboy/README.md).

## Configuration cycle

### 1. Publish the fleet catalog (admin workstation)

`catalog.json` is the single source of truth for all crates, hosts, IPs, roles, and assigned tasks. Run:

```bash
bin/catalog.sh
```

This stamps the file with creation timestamps and uploads it to S3
(`s3://mellow-wombat.braingang.net/wombat/admin/catalog.json`).
The canonical local copy is [infra/var/wombat/admin/catalog.json](infra/var/wombat/admin/catalog.json).

### 2. Generate derived files (gateway, run as root)

One-time virtualenv setup (first use only):

```bash
cd src/generator && python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
```

Then generate:

```bash
sudo bin/generator.sh
```

Reads `/var/wombat/admin/catalog.json` and produces:

| Output | Description |
|--------|-------------|
| `/etc/hosts` | Hostname-to-IP entries for all crate hosts |
| `src/ansible/inventory.yaml` | Ansible fleet inventory |
| `bin/rsync.sh` | rsync commands for distributing config to collectors |

Each collector also gets a dedicated per-host tasking file (`{hostname}.json`) derived from the catalog.

### 3. Distribute config to collectors (gateway)

```bash
bin/rsync.sh
```

rsync(1) pushes `catalog.json` and each `{hostname}.json` to `/var/wombat/admin/` on its respective collector.

### 4. Collector boot — BootBoy runs

On the next reboot (or `systemctl start bootboy.service`), the BootBoy systemd one-shot service:

1. Determines the system hostname.
2. Reads `/var/wombat/admin/{hostname}.json`.
3. Invokes the handler for the `assigned` task.
4. Writes `/var/wombat/admin/bootboy.status.json` recording outcome.

## Tasking file (`{hostname}.json`)

The per-host tasking file is generated from `catalog.json` by the generator. The key field is `assigned`, which selects the handler BootBoy invokes:

```json
{
  "assigned": "heeler-v2",
  "crateName": "wombat01",
  "hostName": "pi3c"
}
```

Known `assigned` values and their handler scripts:

| Value | Handler script |
|-------|----------------|
| `heeler-v2` | `/home/wombat/github/mellow-heeler-v2/bin/bootboy.sh` |
| `hyena-v2` | `/home/wombat/github/mellow-hyena-v2/bin/bootboy.sh` |
| `mastodon-v1` | `/home/wombat/github/mellow-mastodon-v1/bin/bootboy.sh` |

## Status JSON (`bootboy.status.json`)

BootBoy always writes `/var/wombat/admin/bootboy.status.json` (falls back to `/tmp/` if that path is not writable).

| Field | Description |
|-------|-------------|
| `ok` | `true` if BootBoy completed successfully |
| `timestampUtc` | ISO 8601 run timestamp |
| `hostname` | Detected hostname |
| `configPath` | Path of the tasking file read |
| `error` | Set on failure |
| `assignedInvoke` | Present when a handler ran; includes `result.script`, `exitCode`, `durationMs` |

## Troubleshooting

**`ok: false` in `bootboy.status.json`**  
Check the `error` field. Common causes: tasking file not yet rsync'd to the collector, or the collector application repo is not installed.

**`assignedInvoke.missing: true`**  
The handler script path does not exist on the collector. Clone the collector application repo and confirm `bin/bootboy.sh` is present at the expected path.

**`systemctl start bootboy.service` fails with "failed to setup mount namespacing"**  
The kernel does not support mount-namespace hardening directives. Install the bundled unit file:

```bash
sudo install -m 0644 infra/etc/systemd/system/bootboy.service /etc/systemd/system/bootboy.service
sudo systemctl daemon-reload
sudo systemctl restart bootboy.service
```

**Useful diagnostic commands:**

```bash
systemctl status bootboy.service
journalctl -u bootboy.service -b --no-pager
cat /var/wombat/admin/bootboy.status.json
```

## Related files

| Path | Description |
|------|-------------|
| [src/bootboy/bootboy.py](src/bootboy/bootboy.py) | BootBoy implementation |
| [src/bootboy/README.md](src/bootboy/README.md) | BootBoy service details and install notes |
| [bin/bootboy-install-systemd.sh](bin/bootboy-install-systemd.sh) | Installs systemd unit on a collector |
| [bin/catalog.sh](bin/catalog.sh) | Publishes `catalog.json` to S3 |
| [bin/generator.sh](bin/generator.sh) | Generates hosts, inventory, and rsync from catalog |
| [src/generator/](src/generator/) | Generator Python scripts |
| [infra/var/wombat/admin/catalog.json](infra/var/wombat/admin/catalog.json) | Example fleet catalog |
