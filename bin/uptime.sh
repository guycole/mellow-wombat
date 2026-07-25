#!/bin/bash
#
# Title: uptime.sh
# Description: write uptime to bluesky
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
WORK_DIR=$HOME/github/mellow-wombat/src/coyote
VENV_ACTIVATE="${WORK_DIR}/venv/bin/activate"
#
cd ${WORK_DIR}
source "$VENV_ACTIVATE"
#
python3 uptime.py
#
