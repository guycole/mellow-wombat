#
# Title: make_tasking.py
# Description: Generates tasking file from catalog
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import datetime
import socket
import sys
import time
import zoneinfo

import json_helper


class TaskGenerator:

    def __init__(self, filename: str) -> None:
        self.catalog_filename = filename

        self.hostname = socket.gethostname()

        self.epoch_seconds = int(time.time())
        dt_object_utc = datetime.datetime.fromtimestamp(
            self.epoch_seconds, tz=zoneinfo.ZoneInfo("UTC")
        )
        self.iso8601_timestamp = dt_object_utc.isoformat()

    def write_task_file(self, catalog: dict[str, any]) -> None:
        # write a fresh task file with the catalog data

        with open("hosts.new", "w") as hosts_file:
            hosts_file.write(f"#\n")
            hosts_file.write(f"# generated for: {self.hostname}\n")
            hosts_file.write(f"# epoch: {self.epoch_seconds}\n")
            hosts_file.write(f"# ISO8601: {self.iso8601_timestamp}\n")
            hosts_file.write(f"#\n")
            hosts_file.write("127.0.0.1\tlocalhost\n")
            hosts_file.write(f"127.0.1.1\t{self.hostname}\n")
            hosts_file.write(f"#\n")
            hosts_file.write("::1\t\tlocalhost ip6-localhost ip6-loopback\n")
            hosts_file.write("ff02::1\t\tip6-allnodes\n")
            hosts_file.write("ff02::2\t\tip6-allrouters\n")
            hosts_file.write(f"#\n")
            hosts_file.write("10.168.0.11\tentropy\n")
            hosts_file.write("10.168.0.13\tnatash\n")

            for crate in catalog["crate"]:
                hosts_file.write(f"#\n")
                for sbc in crate["sbc"]:
                    print(f"{sbc['eth0']} {sbc['hostName']}")
                    hosts_file.write(f"{sbc['eth0']}\t{sbc['hostName']}\n")

    def generate_tasks(self, catalog: dict[str, any]) -> None:
        results = {}

        for crate in catalog["crate"]:
            for sbc in crate["sbc"]:
                if sbc["hostName"] not in results:
                    results[sbc["hostName"]] = {
                        "ip": sbc["eth0"],
                        "tasks": []
                    }
                for device in sbc["device"]:
                    task = {
                        "type": device["type"],
                        "antenna": device["antenna"]
                    }
                    results[sbc["hostName"]]["tasks"].append(task)

    def execute(self) -> None:
        jh = json_helper.JsonHelper()
        catalog = jh.json_catalog_reader(self.catalog_filename)
        if len(catalog) > 0:
            self.generate_tasks(catalog)
#            self.write_task_file(catalog)
        else:
            print("catalog is empty")

print("start")

#
# make a tasks file for all crates
# python make_tasking.py catalog.json crate_name
# argv[1] = json catalog filename
#
# python3 make_tasking.py ../../infra/var/wombat/admin/catalog.json 
# python3 make_tasking.py /var/wombat/admin/catalog.json 
#
if __name__ == "__main__":
    if len(sys.argv) == 2:
        generator = TaskGenerator(sys.argv[1])
        generator.execute()
    else:
        print("need catalog filename")
        exit(1)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
