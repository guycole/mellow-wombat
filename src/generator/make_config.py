#
# Title: make_config.py
# Description: Generate configuration file for collector
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import datetime
import socket
import sys
import time
import zoneinfo

import json_helper


class ConfigGenerator:

    def __init__(self, catalog_filename: str, tasking_filename: str):
        self.catalog_name = catalog_filename
        self.tasking_name = tasking_filename

        self.host_name = socket.gethostname()
        self.epoch_seconds = int(time.time())

        dt_object_utc = datetime.datetime.fromtimestamp(
            self.epoch_seconds, tz=zoneinfo.ZoneInfo("UTC")
        )
        self.iso8601_timestamp = dt_object_utc.isoformat()

    def get_task(self, sbc: dict[str, any]) -> dict[str, any]:
        result = {}

        if sbc["role"] != "collector":
            return result

        result["name"] = sbc["hostName"]

        if sbc["hostName"].startswith("pi3"):
            result["task"] = "heeler"
            result["version"] = 1
        elif sbc["receiver"]["antenna"] == "multicoupler":
            result["task"] = "assign_me"
            result["version"] = 1
        else:
            result["task"] = "hyena"
            result["version"] = 1

        return result

    def make_tasks(self, catalog: dict[str, any]) -> list[dict[str, any]]:
        crate_list = []

        for crate in catalog["crate"]:
            task_list = {
                "name": crate["crateName"],
                "geoLoc": crate["geoLoc"],
            }

            print(f"crate {crate['crateName']}")
            print(f"geoloc {crate['geoLoc']}")
            for sbc in crate["sbc"]:
                task_entry = self.get_task(sbc)
                if len(task_entry) > 0:
                    if "tasks" in task_list:
                        task_list["tasks"].append(task_entry)
                    else:
                        task_list["tasks"] = [task_entry]
            
            crate_list.append(task_list)

        return crate_list

    def execute(self) -> None:
        jh = json_helper.JsonHelper()
        catalog = jh.json_catalog_reader(self.catalog_name)
        tasking = jh.json_task_reader(self.tasking_name)

#        tasks = self.make_tasks(catalog)
#        jh.json_writer("tasking.new", tasks)

print("start")

#
# invoke from wombat to make configuration file for collectors
#
# python3 make_config.py ../../infra/var/wombat/admin/catalog.json ../../infra/var/wombat/admin/tasking.json
#
if __name__ == "__main__":
    if len(sys.argv) == 3:
        generator = ConfigGenerator(sys.argv[1], sys.argv[2])
#        generator.execute()
    else:
        print("need catalog and tasking filenames")
        exit(1)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
