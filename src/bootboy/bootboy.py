#!/usr/bin/env python3

import argparse
import json
import os
import socket
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, Optional


@dataclass(frozen=True)
class BootConfig:
    assigned: str
    crate_name: Optional[str]
    host_name: Optional[str]
    raw: Dict[str, Any]


def _tail(s: Optional[str], max_chars: int = 4000) -> str:
    if not s:
        return ""
    return s[-max_chars:]


def _run_bootboy_script(handler_name: str, script_path: str, cfg: BootConfig) -> Dict[str, Any]:
    started = time.monotonic()

    if not os.path.exists(script_path):
        return {
            "handler": handler_name,
            "script": script_path,
            "missing": True,
            "exitCode": None,
            "durationMs": int((time.monotonic() - started) * 1000),
            "error": f"missing script: {script_path}",
            "assigned": cfg.assigned,
            "crateName": cfg.crate_name,
            "hostName": cfg.host_name,
        }

    proc = subprocess.run(
        ["bash", script_path],
        check=False,
        text=True,
        capture_output=True,
    )

    return {
        "handler": handler_name,
        "script": script_path,
        "missing": False,
        "exitCode": proc.returncode,
        "durationMs": int((time.monotonic() - started) * 1000),
        "stdoutTail": _tail(proc.stdout),
        "stderrTail": _tail(proc.stderr),
        "assigned": cfg.assigned,
        "crateName": cfg.crate_name,
        "hostName": cfg.host_name,
    }


def _stub_heeler_v2(cfg: BootConfig) -> Dict[str, Any]:
    return _run_bootboy_script(
        handler_name="heeler-v2",
        script_path="/home/wombat/Documents/github/mellow-heeler-v2/bin/bootboy.sh",
        cfg=cfg,
    )


def _stub_hyena_adsb_v2(cfg: BootConfig) -> Dict[str, Any]:
    return _run_bootboy_script(
        handler_name="hyena-adsb-v2",
        script_path="/home/wombat/Documents/github/mellow-hyena-v2/bin/bootboy.sh",
        cfg=cfg,
    )


def _stub_hyena_uat_v2(cfg: BootConfig) -> Dict[str, Any]:
    return _run_bootboy_script(
        handler_name="hyena-uat-v2",
        script_path="/home/wombat/Documents/github/mellow-hyena-v2/bin/bootboy.sh",
        cfg=cfg,
    )


def _stub_mastodon_v2(cfg: BootConfig) -> Dict[str, Any]:
    return _run_bootboy_script(
        handler_name="mastodon-v2",
        script_path="/home/wombat/Documents/github/mellow-mastodon-v2/bin/bootboy.sh",
        cfg=cfg,
    )


def _stub_manatee_v1(cfg: BootConfig) -> Dict[str, Any]:
    return _run_bootboy_script(
        handler_name="manatee-v1",
        script_path="/home/wombat/Documents/github/mellow-manatee-v1/bin/bootboy.sh",
        cfg=cfg,
    )


def _stub_capybara_v1(cfg: BootConfig) -> Dict[str, Any]:
    return _run_bootboy_script(
        handler_name="capybara-v1",
        script_path="/home/gsc/Documents/github/mellow-capybara-v1/bin/bootboy.sh",
        cfg=cfg,
    )


def _get_assigned_handler(assigned: str) -> Optional[Callable[[BootConfig], Dict[str, Any]]]:
    handlers: Dict[str, Callable[[BootConfig], Dict[str, Any]]] = {
        "heeler-v2": _stub_heeler_v2,
        "hyena-adsb-v2": _stub_hyena_adsb_v2,
        "hyena-uat-v2": _stub_hyena_uat_v2,
        "mastodon-v2": _stub_mastodon_v2,
        "manatee-v1": _stub_manatee_v1,
        "capybara-v1": _stub_capybara_v1,
    }
    return handlers.get(assigned)


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


def _write_status_best_effort(status_file: str, status: Dict[str, Any]) -> Optional[str]:
    """Write status JSON; return path written or None.

    We try the requested path first. If that fails (permissions, read-only FS,
    missing mounts, etc.), we fall back to /tmp so there's still a breadcrumb.
    """
    try:
        _atomic_write_json(status_file, status)
        return status_file
    except Exception as exc:
        print(f"bootboy: failed to write status file {status_file}: {exc}", file=sys.stderr)
        try:
            fallback = os.path.join("/tmp", os.path.basename(status_file) or "bootboy.status.json")
            _atomic_write_json(fallback, status)
            print(f"bootboy: wrote fallback status file {fallback}", file=sys.stderr)
            return fallback
        except Exception as exc2:
            print(f"bootboy: failed to write fallback status file: {exc2}", file=sys.stderr)
            return None


def run(admin_dir: str, status_file: str) -> int:
    status: Dict[str, Any] = {
        "ok": False,
        "timestampUtc": _utc_now_iso(),
        "hostname": None,
        "configPath": None,
    }

    hostname: Optional[str] = None
    config_path: Optional[str] = None
    return_code = 2

    try:
        hostname = _get_short_hostname()
        config_path = os.path.join(admin_dir, f"{hostname}.json")
        status["hostname"] = hostname
        status["configPath"] = config_path

        raw = _read_json(config_path)
        cfg = _parse_boot_config(raw)

        invoke: Dict[str, Any] = {"requested": cfg.assigned, "invoked": False}
        handler = _get_assigned_handler(cfg.assigned)
        if handler is not None:
            invoke["invoked"] = True
            invoke["result"] = handler(cfg)
            exit_code = invoke.get("result", {}).get("exitCode")
            if exit_code not in (None, 0):
                raise RuntimeError(f"assigned handler failed: {cfg.assigned} (exit={exit_code})")
            if exit_code is None and invoke.get("result", {}).get("error"):
                # Missing script is expected when apps haven't been installed yet; record it but don't fail.
                if not invoke.get("result", {}).get("missing", False):
                    raise RuntimeError(f"assigned handler failed: {cfg.assigned} ({invoke['result']['error']})")
        status["assignedInvoke"] = invoke

        status.update(
            {
                "ok": True,
                "assigned": cfg.assigned,
                "crateName": cfg.crate_name,
                "hostName": cfg.host_name,
            }
        )
        return_code = 0
    except Exception as exc:
        status["error"] = str(exc)
        return_code = 2
    finally:
        written_path = _write_status_best_effort(status_file, status)
        if written_path is None:
            # Writing status is a core requirement; if we can't do it, signal a distinct failure.
            return_code = 3

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
