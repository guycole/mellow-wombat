#
# Title: make_config.py
# Description: generate configuration file for a collector from catalog
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
from __future__ import annotations

import sys
import socket
from typing import Any
from pathlib import Path

import json_helper


CONFIG_PATH = Path("/var/wombat/admin/config.json")


def _usage() -> str:
    return "Usage: python3 make_config.py /path/to/catalog.json"


def _bool_to_yaml(value: bool) -> str:
    return "true" if value else "false"


def _task_family(task_name: str) -> str:
    # e.g. heeler-v1 -> heeler, hyena-adsb-v1 -> hyena
    return task_name.split("-")[0].strip() if task_name else "unknown"


def _gps_enabled(sbc: dict[str, Any]) -> bool:
    gps = sbc.get("gps")
    if gps is None:
        return False
    if not isinstance(gps, str):
        return bool(gps)
    return gps.strip().lower() not in {"", "none", "no", "false"}


def _find_local_collector(catalog: dict[str, Any], hostname: str) -> tuple[dict[str, Any], dict[str, Any]]:
    crates = catalog.get("crate")
    if not isinstance(crates, list):
        raise ValueError("catalog missing 'crate' array")

    matches: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for crate in crates:
        if not isinstance(crate, dict):
            continue
        sbcs = crate.get("sbc")
        if not isinstance(sbcs, list):
            continue
        for sbc in sbcs:
            if not isinstance(sbc, dict):
                continue
            if sbc.get("hostName") != hostname:
                continue
            if sbc.get("role") != "collector":
                raise ValueError(f"hostName={hostname} found but role is not 'collector'")
            matches.append((crate, sbc))

    if not matches:
        raise ValueError(f"no collector found for hostName={hostname}")
    if len(matches) > 1:
        raise ValueError(f"multiple collectors found for hostName={hostname}")

    return matches[0]


def _render_config(crate: dict[str, Any], sbc: dict[str, Any]) -> str:
    geo_loc = crate.get("geoLoc") or {}
    site = geo_loc.get("siteName", "unknown") if isinstance(geo_loc, dict) else "unknown"
    host = sbc.get("hostName", "unknown")

    receiver = sbc.get("receiver") or {}
    receiver_task = receiver.get("task") if isinstance(receiver, dict) else None
    if not isinstance(receiver_task, str) or not receiver_task.strip():
        receiver_task = "unknown"

    fresh_dir = f"/var/wombat/fresh/{_task_family(receiver_task)}"
    gps_enable = _gps_enabled(sbc)

    # Note: this is YAML-like text (even though the filename ends in .json),
    # matching the format used in the prompt.
    return "\n".join(
        [
            "# repository of freshly collected observations",
            f"freshDir: {fresh_dir}",
            "#",
            "# collection host location",
            f"site: {site}",
            "#",
            "# collection host",
            f"host: {host}",
            "#",
            "# true, there is a GPS available",
            f"gpsEnable: {_bool_to_yaml(gps_enable)}",
            "#",
            "# stations which inhibit collection",
            "homePlateStations:",
            "  - 'station1'",
            "  - 'station2'",
            "",
        ]
    )


def generate_config(catalog_filename: str) -> int:
    jh = json_helper.JsonHelper()
    catalog = jh.json_catalog_reader(catalog_filename)
    if not catalog:
        print("catalog is empty or invalid", file=sys.stderr)
        return 2

    hostname = socket.gethostname().split(".")[0]
    try:
        crate, sbc = _find_local_collector(catalog, hostname)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    config_text = _render_config(crate, sbc)
    try:
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        CONFIG_PATH.write_text(config_text)
    except Exception as exc:
        print(f"failed to write {CONFIG_PATH}: {exc}", file=sys.stderr)
        return 2

    print(str(CONFIG_PATH))
    return 0


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(_usage(), file=sys.stderr)
        return 1

    return generate_config(argv[1])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
