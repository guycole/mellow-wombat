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

schema_v1 = {
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
                    "name": {"type": "string"},
                    "location": {"type": "string"},
                    "multicoupler": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "number"},
                            "antenna": {"type": "string"},
                            "type": {"type": "string"}
                        },
                        "required": ["id", "antenna", "type"],
                        "additionalProperties": False
                    },
                    "sbc": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "eth0": {"type": "string"},
                                "gps": {"type": "string"},
                                "name": {"type": "string"},
                                "role": {"type": "string"},
                                "storage": {"type": "string"},
                                "type": {"type": "string"},
                                "wifi": {"type": "string"},
                                "receiver": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "number"},
                                        "type": {"type": "string"},
                                        "antenna": {"type": "string"}
                                    },
                                    "required": ["id", "type", "antenna"],
                                    "additionalProperties": False
                                }
                            },
                            "required": ["eth0", "name", "role", "storage", "type", "wifi"],
                            "additionalProperties": False
                        }
                    }
                },
                "required": ["name", "location", "sbc"],
                "additionalProperties": False
            }
        }
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

    def json_reader(self, file_name: str) -> dict[str, any]:
        print(f"read {file_name}")

        if os.path.isfile(file_name) is False:
            print(f"missing {file_name}")
            return {}

        results = {}

        try:
            with open(file_name, "r") as in_file:
                results = json.load(in_file)
                validate(instance=results, schema=schema_v1)
        except Exception as error:
            print(error)
            return {}

        return results

    def json_writer(self, file_name:str, payload: dict[str, any]) -> None:
        try:
            with open(file_name, "w") as out_file:
                json.dump(payload, out_file, indent=4)
        except Exception as error:
            print(error)
