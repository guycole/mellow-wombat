#
# Title: generator.py
# Description:
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import datetime
import sys
import time
import zoneinfo

import json_helper


class Generator:

    def __init__(self, args):
        self.args = args
        self.epoch_seconds = int(time.time())

        dt_object_utc = datetime.datetime.fromtimestamp(self.epoch_seconds, tz=zoneinfo.ZoneInfo("UTC"))
        self.iso8601_timestamp = dt_object_utc.isoformat()

    def write_collect_file(self, inventory: dict[str, any]) -> None:
        crate_name = self.args[2]
        print(f"collect for: {crate_name}")

        with open("collection.sh", "w") as out_file:
            out_file.write("#!/bin/bash\n")
            out_file.write(f"# generated for: {crate_name}\n")
            out_file.write(f"# epoch: {self.epoch_seconds}\n")
            out_file.write(f"# ISO8601: {self.iso8601_timestamp}\n")
            out_file.write(f"#\n")
            out_file.write(f"# must run from gateway\n")
            out_file.write(f"#\n")
            out_file.write(f"DEST_DIR=/var/wombat\n")
            out_file.write(f"SRC_DIR=/var/wombat/fresh\n")

            for crate in inventory["crate"]:
                out_file.write(f"#\n")
                if crate["name"] == crate_name:
                    for sbc in crate["sbc"]:
                        if sbc["role"] == "collector":
                            out_file.write(f"rsync -av --remove-source-files wombat@{sbc['name']}:${{SRC_DIR}} ${{DEST_DIR}}\n")
            
    def write_hosts_file(self, inventory: dict[str, any]) -> None:
        # write a fresh hosts file with the inventory data
        crate = self.args[2]
        print(f"hosts for: {crate}")

        with open("hosts.new", "w") as hosts_file:
            hosts_file.write(f"#\n")
            hosts_file.write(f"# generated for: {crate}\n")
            hosts_file.write(f"# epoch: {self.epoch_seconds}\n")
            hosts_file.write(f"# ISO8601: {self.iso8601_timestamp}\n")
            hosts_file.write(f"#\n")
            hosts_file.write("127.0.0.1\tlocalhost\n")
            hosts_file.write(f"127.0.1.1\t{crate}\n")
            hosts_file.write(f"#\n")
            hosts_file.write("::1\t\tlocalhost ip6-localhost ip6-loopback\n")
            hosts_file.write("ff02::1\t\tip6-allnodes\n")
            hosts_file.write("ff02::2\t\tip6-allrouters\n")

            for crate in inventory["crate"]:
                hosts_file.write(f"#\n")
                for sbc in crate["sbc"]:
                    print(f"{sbc['eth0']} {sbc['name']}")
                    hosts_file.write(f"{sbc['eth0']}\t{sbc['name']}\n")

    def execute(self) -> None:
        jh = json_helper.JsonHelper()
        inventory = jh.json_reader(self.args[0])

        if len(self.args) > 1:
            task = self.args[1]
            if task == "hosts":
                self.write_hosts_file(inventory)
            elif task == "collect":
                self.write_collect_file(inventory)
            else:
                print("unknown task")

print("start")

#
# python generator.py inventory.json collect wombat02 (4 args)
# python generator.py inventory.json hosts wombat02 
# argv[1] = json inventory filename
# argv[2] = task, i.e. "collect" or "hosts"
#
# make a hosts file
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ndx = len(sys.argv) - 1
        args = sys.argv[-ndx:len(sys.argv)]
        generator = Generator(args)
        generator.execute()
    else:
        print("need filename")
        exit(1)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
