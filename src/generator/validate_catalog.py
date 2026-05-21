#
# Title: validate_catalog.py
# Description: Validate catalog.json against schema + semantic rules
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
"""Validate a wombat catalog file.

Usage:
    python3 validate_catalog.py /path/to/catalog.json

Returns:
    0 if valid
    1 for usage error
    2 if invalid
"""

from __future__ import annotations

import sys

import json_helper


def _usage() -> str:
    return "Usage: python3 validate_catalog.py /path/to/catalog.json"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(_usage(), file=sys.stderr)
        return 1

    catalog_filename = argv[1]
    jh = json_helper.JsonHelper()
    catalog = jh.json_catalog_reader(catalog_filename)
    if not catalog:
        print("invalid", file=sys.stderr)
        return 2

    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
