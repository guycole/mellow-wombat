#
# Title: make_inventory.py
# Description: Generates ansible inventory from catalog
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import datetime
import sys
import time
import zoneinfo

import json_helper


class InventoryGenerator:

    def __init__(self, args):
        self.args = args
        self.epoch_seconds = int(time.time())

        dt_object_utc = datetime.datetime.fromtimestamp(
            self.epoch_seconds, tz=zoneinfo.ZoneInfo("UTC")
        )
        self.iso8601_timestamp = dt_object_utc.isoformat()

    def write_inventory_file(self, catalog: dict[str, any]) -> None:

        with open("inventory.new", "w") as inventory_file:
            inventory_file.write(f"---\n")

            for crate in catalog["crate"]:
                inventory_file.write(f"{crate['crateName']}:\n")

                # only collectors allowed in ansible inventory
                candidates = []
                for sbc in crate["sbc"]:
                    if sbc["role"] == "collector":
                        candidates.append(sbc)
                    else:
                        print(f"skipping {sbc['hostName']} with role {sbc['role']}")

                if len(candidates) > 0:
                    inventory_file.write("  hosts:\n")
                    for candidate in candidates:
                        inventory_file.write(f"    {candidate['hostName']}:\n")
                        inventory_file.write(f"      ansible_host: {candidate['eth0']}\n")

    def execute(self) -> None:
        jh = json_helper.JsonHelper()
        catalog = jh.json_catalog_reader(self.args[0])

        self.write_inventory_file(catalog)


print("start")

#
# make ansible inventory from catalog
# python make_inventory.py catalog.json
# argv[1] = json catalog filename
#
# python3 make_inventory.py ../../infra/var/wombat/admin/catalog.json
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ndx = len(sys.argv) - 1
        args = sys.argv[-ndx : len(sys.argv)]
        generator = InventoryGenerator(args)
        generator.execute()
    else:
        print("need catalog filename")
        exit(1)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
