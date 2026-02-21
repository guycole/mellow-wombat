#
# Title: driver.py
# Description:
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import sys

import json_helper

class Driver:
    
    def execute(self, file_name:str) -> None:
        jh = json_helper.JsonHelper()
        xx = jh.json_reader(file_name)
        print(xx)


print("start")

#
# argv[1] = csv filename
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        driver = Driver()
        driver.execute("inventory.json")
    else:
        print("need filename")
        exit(1)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
