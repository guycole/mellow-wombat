import json
import sys

import json_helper

class TaskingGenerator:
    
    def __init__(self, filename: str) -> None:
        self.catalog_filename = filename

    def generate_tasking(self, catalog: dict[str, any]) -> list[dict[str, any]]:
        results = []

        crates = catalog.get("crate")
        for crate in crates:
            for sbc in crate["sbc"]:
                if sbc["role"] == "collector":
                    results.append({
                        "crateName": crate["crateName"],
                        "geoLoc": crate["geoLoc"],
                        "hostName": sbc["hostName"],
                        "receiver": sbc["receiver"],
                        "type": sbc["type"],
                    })

        return results

    def execute(self) -> None:
        jh = json_helper.JsonHelper()
        catalog = jh.json_catalog_reader(self.catalog_filename)
      
        tasks = self.generate_tasking(catalog)
        for task in tasks:
            filename = f"/var/wombat/admin/{task['hostName']}.json"
            with open(filename, "w") as out_file:
                json.dump(task, out_file, indent=2)

#
# make a tasking file for each collector
# python make_hosts.py catalog.json
# argv[1] = json catalog filename
#
# python3 make_tasking.py ../../infra/var/wombat/admin/catalog.json 
# python3 make_tasking.py /var/wombat/admin/catalog.json 
#
if __name__ == "__main__":
    if len(sys.argv) == 2:
        generator = TaskingGenerator(sys.argv[1])
        generator.execute()
    else:
        print("need catalog filename")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
