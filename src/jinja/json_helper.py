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

schema = {
    "type": "object",
    "properties": {
        "creationEpochTime": {"type": "number"},
        "creationIso8601Time": {"type": "string"},
        "project": {"type": "string"},
        "schemaVersion": {"type": "number"},
    },
    "required": [
        "creationEpochTime",
        "creationIso8601Time",
        "project",
        "schemaVersion"
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
                validate(instance=results, schema=schema)
        except Exception as error:
            print(error)
            return {}

        return results
