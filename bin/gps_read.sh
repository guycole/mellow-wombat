#!/bin/bash
#
# Title: gps_read.sh
# Description: ask django to read from gpsd, run from cron
#
URL=http://127.0.0.1:8000/wombat/gps
#
curl -v $URL
#
#curl -v -H "Content-Type:application/json" -d '{"preamble": {"pingState": false}' $URL
#curl -v -H "Content-Type:application/json" -d '{"preamble": {"messageType": "PING", "messageVersion": 1, "transactionUuid": "35A0542B-5607-428B-ABA6-ACCC70EE4741"}, "pingState": false}' $URL
#