#
# Title: driver.py
# Description:
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import datetime
import sys
import time
import zoneinfo

import json_helper


class Driver:

    def execute(self, file_name: str) -> None:
        epoch_seconds = int(time.time())
        print(epoch_seconds)
        dt_object_utc = datetime.datetime.fromtimestamp(epoch_seconds, tz=zoneinfo.ZoneInfo("UTC"))
        iso8601_timestamp = dt_object_utc.isoformat()
        print(iso8601_timestamp)

        jh = json_helper.JsonHelper()
        payload = jh.json_reader(file_name)
        print(payload)
        print(type(payload))
        jh.json_writer("output.json", payload)


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
