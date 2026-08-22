#
# Title: sql_guard.py
# Description: safety checks for LLM-generated SQL before execution
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
#

import re

from db import TABLE_NAME, COLUMNS

FORBIDDEN_KEYWORDS = (
    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "truncate",
    "grant",
    "revoke",
    "create",
    "copy",
    "call",
    "execute",
    "--",
    "/*",
    ";",
)


class UnsafeQueryError(Exception):
    pass


def validate_select(query: str) -> str:
    """
    raise UnsafeQueryError unless query is a single, read-only select
    statement that only touches the wombat_tasking table.
    """
    stripped = query.strip().rstrip(";").strip()
    lowered = stripped.lower()

    if not lowered.startswith("select"):
        raise UnsafeQueryError("only select statements are permitted")

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in lowered:
            raise UnsafeQueryError(f"disallowed keyword detected: {keyword!r}")

    if TABLE_NAME not in lowered:
        raise UnsafeQueryError(f"query must reference the {TABLE_NAME} table")

    other_tables = re.findall(r"\bfrom\s+([a-z0-9_\.]+)|\bjoin\s+([a-z0-9_\.]+)", lowered)
    for match in other_tables:
        table = (match[0] or match[1]).strip()
        if table and table != TABLE_NAME:
            raise UnsafeQueryError(f"query may not reference table {table!r}")

    return stripped


def describe_schema() -> str:
    """human readable schema description used to prompt the LLM"""
    columns = ", ".join(COLUMNS)
    return (
        f"table {TABLE_NAME}({columns}). "
        "rx_task and rx_type are compound free-text values (e.g. "
        "'hyena-v2-dump978', 'rtl-sdr-v4'), so match them with "
        "ILIKE '%term%' rather than '='."
    )

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
