#!/bin/bash
#
# Title: varbat.sh
# Description: create varbat directories
# Development Environment: ubuntu 22.04.5 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
set -euo pipefail

cd /var/wombat

SERVICES=(capybara heeler hyena manatee mastodon slug)

mkdir -p admin failure fresh

for svc in "${SERVICES[@]}"; do
  mkdir -p "fresh/${svc}"
  mkdir -p "${svc}/archive" "${svc}/export" "${svc}/koala" "${svc}/success"
done