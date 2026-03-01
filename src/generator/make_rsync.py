#
# Title: make_rsync.py
# Description: generate rsync collection script from catalog
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import datetime
import sys
import time
import zoneinfo

import json_helper


class RsyncGenerator:

    def __init__(self, args):
        self.args = args
        self.epoch_seconds = int(time.time())

        dt_object_utc = datetime.datetime.fromtimestamp(self.epoch_seconds, tz=zoneinfo.ZoneInfo("UTC"))
        self.iso8601_timestamp = dt_object_utc.isoformat()

    def write_rsync_file(self, inventory: dict[str, any]) -> None:
        crate_name = self.args[1]
        print(f"rsync for: {crate_name}")

        with open("rsync.new", "w") as out_file:
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

    def execute(self) -> None:
        jh = json_helper.JsonHelper()
        inventory = jh.json_reader(self.args[0])

        self.write_rsync_file(inventory)

print("start")

#
# python make_rsync.py catalog.json wombat02 
# argv[1] = json catalog filename
# argv[2] = target crate name
#
# python3 make_rsync.py ../../infra/var/wombat/admin/catalog.json wombat01
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ndx = len(sys.argv) - 1
        args = sys.argv[-ndx:len(sys.argv)]
        generator = RsyncGenerator(args)
        generator.execute()
    else:
        print("need catalog filename and crate")
        exit(1)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
