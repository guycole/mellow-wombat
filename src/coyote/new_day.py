#
# Title: new_day.py
# Description: 
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#

import datetime
import json
import logging
import socket
import sys
import time
import uuid
from xmlrpc import client
import zoneinfo

from atproto import Client

#from httpx import post

import yaml
from yaml.loader import SafeLoader

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("coyote")

class Driver:
    def __init__(self, args: dict[str, any]):
        self.account_name = args['accountName']
        self.application_password = args['applicationPassword']

        self.hostname = socket.gethostname()

    def execute(self) -> None:
        logger.info(f"driver initialized on host: {self.hostname}")

        client = Client()
        client.login(self.account_name, self.application_password)

        message = f"new day from host: {self.hostname}"

        post = client.send_post(text=message)
        print(f"post successful! CID: {post.cid}")

#
# argv[1] = configuration filename
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "config.yaml"

    with open(file_name, "r") as in_file:
        try:
            configuration = yaml.load(in_file, Loader=SafeLoader)
            driver = Driver(configuration)
            driver.execute()
        except yaml.YAMLError as error:
            print(error)

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
