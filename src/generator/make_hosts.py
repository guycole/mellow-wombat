#
# Title: make_hosts.py
# Description: Generates hosts file from catalog
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import datetime
import sys
import time
import zoneinfo

import json_helper


class HostGenerator:

    def __init__(self, args):
        self.args = args

        self.epoch_seconds = int(time.time())

        dt_object_utc = datetime.datetime.fromtimestamp(
            self.epoch_seconds, tz=zoneinfo.ZoneInfo("UTC")
        )
        self.iso8601_timestamp = dt_object_utc.isoformat()

    def write_hosts_file(self, catalog: dict[str, any]) -> None:
        # write a fresh hosts file with the catalog data
        crate = self.args[1]
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

            for crate in catalog["crate"]:
                hosts_file.write(f"#\n")
                for sbc in crate["sbc"]:
                    print(f"{sbc['eth0']} {sbc['hostName']}")
                    hosts_file.write(f"{sbc['eth0']}\t{sbc['hostName']}\n")

    def execute(self) -> None:
        jh = json_helper.JsonHelper()
        catalog = jh.json_catalog_reader(self.args[0])
        if len(catalog) > 0:
            self.write_hosts_file(catalog)
        else:
            print("catalog is empty")

print("start")

#
# make a hosts file for a crate
# python make_hosts.py catalog.json crate_name
# argv[1] = json catalog filename
#
# python3 make_hosts.py ../../infra/var/wombat/admin/catalog.json wombat01
#
if __name__ == "__main__":
    if len(sys.argv) == 3:
        ndx = len(sys.argv) - 1
        args = sys.argv[-ndx : len(sys.argv)]
        generator = HostGenerator(args)
        generator.execute()
    else:
        print("need catalog filename")
        exit(1)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
