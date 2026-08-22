#
# Title: db.py
# Description: read-only access layer for the wombat_tasking table
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
#

import logging

import psycopg2
import psycopg2.extras

logger = logging.getLogger("mcp")

TABLE_NAME = "wombat_tasking"

COLUMNS = (
    "id",
    "active_flag",
    "assign_time",
    "crate_name",
    "host_name",
    "host_type",
    "ip_address",
    "rx_antenna",
    "rx_id",
    "rx_task",
    "rx_type",
    "storage",
)


class TaskingRepository:
    """read-only queries against wombat_tasking, backed by a wombat_client connection"""

    def __init__(self, args: dict[str, any]):
        self.host = args["host"]
        self.port = args["port"]
        self.dbname = args["dbname"]
        self.user = args["user"]
        self.password = args["password"]

    def _connect(self):
        connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password,
        )
        connection.set_session(readonly=True, autocommit=True)
        return connection

    def list_rows(
        self,
        active_only: bool = True,
        crate_name: str | None = None,
        host_type: str | None = None,
        limit: int = 200,
    ) -> list[dict]:
        """list wombat_tasking rows with optional filters, all parameterized"""
        clauses = []
        params: list[any] = []

        if active_only:
            clauses.append("active_flag = true")
        if crate_name:
            clauses.append("crate_name = %s")
            params.append(crate_name)
        if host_type:
            clauses.append("host_type = %s")
            params.append(host_type)

        where_sql = f"where {' and '.join(clauses)}" if clauses else ""
        query = f"select * from {TABLE_NAME} {where_sql} order by id limit %s"
        params.append(limit)

        return self._execute(query, tuple(params))

    def run_select(self, query: str, params: tuple = ()) -> list[dict]:
        """execute a pre-validated select statement against wombat_tasking"""
        return self._execute(query, params)

    def _execute(self, query: str, params: tuple) -> list[dict]:
        connection = self._connect()
        try:
            with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                # psycopg2 parses stray '%' as placeholders even with no params, so pass None when empty
                cursor.execute(query, params or None)
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        finally:
            connection.close()

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
