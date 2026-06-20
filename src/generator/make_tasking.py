import json
import random
import sys

import json_helper

class TaskingGenerator:
    
    def __init__(self, filename: str) -> None:
        self.catalog_filename = filename

    def assign_task(self, task_options: list[str], task_assigned: str, task_list: list[str]) -> str:
        print(task_options)
        print(task_assigned)

        if len(task_options) == 0:
            print("no tasks declared")
            return "bogus"
        elif len(task_options) == 1:
            return task_options[0]

        # falling through means pick task not yet assigned
        for task in task_options:
            if task in task_list:
                continue
            else:
                return task
            
        # all tasks already assigned, pick random
        return task_options[random.randint(0, len(task_options)-1)]

    def generate_tasking(self, catalog: dict[str, any]) -> list[dict[str, any]]:
        results = []

        crates = catalog.get("crate")
        for crate in crates:
            task_list = []
          
            for sbc in crate["sbc"]:
                if sbc["role"] == "collector":
                    tasks = sbc["tasks"]
                    task = sbc["receiver"]["task"]
                    assigned = self.assign_task(tasks, task, task_list)
                    if assigned not in task_list:
                        task_list.append(assigned)

                    results.append({
                        "assigned": assigned,
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
