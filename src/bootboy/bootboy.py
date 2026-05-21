#!/usr/bin/env python3

import argparse
import json
import os
import socket
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class BootConfig:
    assigned: str
    crate_name: Optional[str]
    host_name: Optional[str]
    raw: Dict[str, Any]


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _get_short_hostname() -> str:
    # Prefer the kernel hostname; strip any domain suffix.
    host = socket.gethostname().strip()
    if not host:
        raise RuntimeError("hostname is empty")
    return host.split(".", 1)[0]


def _read_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"expected JSON object at {path}")
    return data


def _parse_boot_config(raw: Dict[str, Any]) -> BootConfig:
    assigned = raw.get("assigned")
    if not isinstance(assigned, str) or not assigned.strip():
        raise ValueError("missing/invalid required field: assigned")

    crate_name = raw.get("crateName")
    if crate_name is not None and not isinstance(crate_name, str):
        crate_name = None

    host_name = raw.get("hostName")
    if host_name is not None and not isinstance(host_name, str):
        host_name = None

    return BootConfig(assigned=assigned.strip(), crate_name=crate_name, host_name=host_name, raw=raw)


def _atomic_write_json(path: str, payload: Dict[str, Any]) -> None:
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    tmp_path = f"{path}.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp_path, path)


def run(admin_dir: str, status_file: str) -> int:
    hostname = _get_short_hostname()
    config_path = os.path.join(admin_dir, f"{hostname}.json")

    status: Dict[str, Any] = {
        "ok": False,
        "timestampUtc": _utc_now_iso(),
        "hostname": hostname,
        "configPath": config_path,
    }

    try:
        raw = _read_json(config_path)
        cfg = _parse_boot_config(raw)
        status.update(
            {
                "ok": True,
                "assigned": cfg.assigned,
                "crateName": cfg.crate_name,
                "hostName": cfg.host_name,
                # Placeholder for the next phase (starting the assigned app).
                "assignedAppDir": f"/home/wombat/documents/gitlab/{cfg.assigned}",
            }
        )
        return_code = 0
    except Exception as exc:
        status["error"] = str(exc)
        return_code = 2
    finally:
        try:
            _atomic_write_json(status_file, status)
        except Exception as exc:
            print(f"bootboy: failed to write status file {status_file}: {exc}", file=sys.stderr)
            # If status cannot be written, preserve the original failure signal.
            return_code = return_code or 3

    if return_code != 0:
        print(f"bootboy: failed (see {status_file})", file=sys.stderr)
    return return_code


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Boot-time configuration for mellow collectors")
    parser.add_argument(
        "--admin-dir",
        default="/var/wombat/admin",
        help="Directory containing {hostname}.json (default: /var/wombat/admin)",
    )
    parser.add_argument(
        "--status-file",
        default="/var/wombat/admin/bootboy.status.json",
        help="Path to write status JSON (default: /var/wombat/admin/bootboy.status.json)",
    )
    args = parser.parse_args(argv)
    return run(admin_dir=args.admin_dir, status_file=args.status_file)


if __name__ == "__main__":
    raise SystemExit(main())
 
# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
