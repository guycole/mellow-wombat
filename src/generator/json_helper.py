#
# Title: json_helper.py
# Description:
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#

import datetime
import json
import os
import time

from jsonschema import validate

catalog_schema_v1 = {
    "type": "object",
    "properties": {
        "creationEpochTime": {"type": "number"},
        "creationIso8601Time": {"type": "string"},
        "project": {"type": "string"},
        "schemaVersion": {"type": "number"},
        "crate": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "crateName": {"type": "string"},
                    "geoLoc": {
                        "type": "object",
                        "properties": {
                            "siteName": {"type": "string"},
                            "altitude": {"type": "number"},
                            "latitude": {"type": "number"},
                            "longitude": {"type": "number"},
                        },
                        "required": ["siteName", "altitude", "latitude", "longitude"],
                        "additionalProperties": False,
                    },
                    "multicoupler": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "number"},
                            "antenna": {"type": "string"},
                            "type": {"type": "string"},
                        },
                        "required": ["id", "antenna", "type"],
                        "additionalProperties": False,
                    },
                    "sbc": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "eth0": {"type": "string"},
                                "gps": {"type": "string"},
                                "hostName": {"type": "string"},
                                "role": {"type": "string"},
                                "storage": {"type": "string"},
                                "tasks": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                },
                                "type": {"type": "string"},
                                "wifi": {"type": "string"},
                                "receiver": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "number"},
                                        "task": {"type": "string"},
                                        "type": {"type": "string"},
                                        "antenna": {"type": "string"},
                                    },
                                    "required": ["id", "task", "type", "antenna"],
                                    "additionalProperties": False,
                                },
                            },
                            "required": [
                                "eth0",
                                "hostName",
                                "role",
                                "storage",
                                "type",
                                "wifi",
                            ],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["crateName", "geoLoc", "sbc"],
                "additionalProperties": False,
            },
        },
    },
    "required": [
        "creationEpochTime",
        "creationIso8601Time",
        "project",
        "schemaVersion",
    ],
    "additionalProperties": False,
}


class JsonHelper:

    def _validate_task_assignments(self, catalog: dict[str, any]) -> list[str]:
        errors: list[str] = []

        crates = catalog.get("crate")
        if not isinstance(crates, list):
            return ["catalog is missing 'crate' array"]

        for crate in crates:
            if not isinstance(crate, dict):
                continue

            crate_name = crate.get("crateName", "<unknown>")
            sbcs = crate.get("sbc")
            if not isinstance(sbcs, list):
                continue

            tasks_declared: set[str] = set()
            receiver_task_examples: set[str] = set()

            for sbc in sbcs:
                if not isinstance(sbc, dict):
                    continue

                if sbc.get("role") != "collector":
                    continue

                host_name = sbc.get("hostName", "<unknown>")
                sbc_tasks = sbc.get("tasks")
                if not isinstance(sbc_tasks, list):
                    errors.append(
                        f"crate={crate_name} hostName={host_name}: missing tasks list"
                    )
                    sbc_tasks = []
                else:
                    for task in sbc_tasks:
                        if isinstance(task, str):
                            tasks_declared.add(task)
                        else:
                            errors.append(
                                f"crate={crate_name} hostName={host_name}: tasks element is not string"
                            )

                receiver = sbc.get("receiver")
                if not isinstance(receiver, dict):
                    errors.append(
                        f"crate={crate_name} hostName={host_name}: missing receiver stanza"
                    )
                    continue

                receiver_task = receiver.get("task")
                if not isinstance(receiver_task, str) or not receiver_task.strip():
                    errors.append(
                        f"crate={crate_name} hostName={host_name}: receiver.task is missing/empty"
                    )
                    continue

                receiver_task_examples.add(receiver_task)
                if receiver_task not in sbc_tasks:
                    errors.append(
                        f"crate={crate_name} hostName={host_name}: receiver.task '{receiver_task}' not in tasks list"
                    )

            missing_examples = sorted(tasks_declared - receiver_task_examples)
            if missing_examples:
                errors.append(
                    f"crate={crate_name}: missing receiver.task example(s) for: {', '.join(missing_examples)}"
                )

        return errors

    def json_catalog_reader(self, file_name: str) -> dict[str, any]:
        print(f"read {file_name}")

        if os.path.isfile(file_name) is False:
            print(f"missing {file_name}")
            return {}

        results = {}

        try:
            with open(file_name, "r") as in_file:
                results = json.load(in_file)
                validate(instance=results, schema=catalog_schema_v1)

            task_errors = self._validate_task_assignments(results)
            if task_errors:
                for err in task_errors:
                    print(err)
                return {}
        except Exception as error:
            print(error)
            return {}

        return results

    def json_task_reader(self, file_name: str) -> dict[str, any]:
        print(f"read {file_name}")

        if os.path.isfile(file_name) is False:
            print(f"missing {file_name}")
            return {}

        results = {}

        try:
            with open(file_name, "r") as in_file:
                results = json.load(in_file)
        except Exception as error:
            print(error)
            return {}

        return results

    def json_writer(self, file_name: str, payload: dict[str, any]) -> None:
        try:
            with open(file_name, "w") as out_file:
                json.dump(payload, out_file, indent=4)
        except Exception as error:
            print(error)
