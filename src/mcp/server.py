#
# Title: server.py
# Description: MCP server exposing wombat_tasking queries, backed by a local llama3.2 model
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#

import logging
import sys

import yaml
from yaml.loader import SafeLoader
from mcp.server.fastmcp import FastMCP

from db import TaskingRepository
from llm import LlamaClient
from sql_guard import UnsafeQueryError, describe_schema, validate_select

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("mcp")

mcp = FastMCP("wombat-tasking")

repository: TaskingRepository = None
llama: LlamaClient = None

SQL_SYSTEM_PROMPT = (
    "You translate questions about receiver tasking into a single PostgreSQL "
    "select statement. Only use {schema}. Prefer ILIKE '%term%' over '=' when "
    "matching free-text columns, so partial mentions still match. Respond with "
    "the SQL statement only, no markdown, no commentary, no trailing semicolon."
)

ANSWER_SYSTEM_PROMPT = (
    "You answer questions about receiver tasking using the supplied query "
    "results. If the results list is empty, say plainly that no matching rows "
    "were found; otherwise summarize the rows. Be concise and only use the "
    "data provided."
)


@mcp.tool()
def list_tasking(active_only: bool = True, crate_name: str = "", host_type: str = "") -> list[dict]:
    """list rows from wombat_tasking, optionally filtered by crate_name and/or host_type"""
    return repository.list_rows(
        active_only=active_only,
        crate_name=crate_name or None,
        host_type=host_type or None,
    )


@mcp.tool()
def ask_tasking(question: str) -> dict:
    """answer a natural language question about wombat_tasking using llama3.2 + postgres"""
    schema = describe_schema()
    sql_prompt = SQL_SYSTEM_PROMPT.format(schema=schema)
    candidate_sql = llama.generate(sql_prompt, question)

    try:
        safe_sql = validate_select(candidate_sql)
    except UnsafeQueryError as error:
        logger.warning(f"rejected llama-generated query: {candidate_sql!r} ({error})")
        return {"error": str(error), "generated_sql": candidate_sql}

    rows = repository.run_select(safe_sql)

    answer = llama.generate(
        ANSWER_SYSTEM_PROMPT,
        f"question: {question}\nquery results: {rows}",
    )

    return {"answer": answer, "sql": safe_sql, "rows": rows}


#
# argv[1] = configuration filename
#
if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) > 1 else "config.yaml"

    with open(file_name, "r") as in_file:
        try:
            configuration = yaml.load(in_file, Loader=SafeLoader)
        except yaml.YAMLError as error:
            print(error)
            sys.exit(1)

    repository = TaskingRepository(configuration["database"])
    llama = LlamaClient(configuration["ollama"])

    mcp.run(transport="stdio")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
