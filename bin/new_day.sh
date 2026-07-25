#!/bin/bash
#
# Title: new_day.sh
# Description: 
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
WORK_DIR=$HOME/github/mellow-wombat/src/coyote
VENV_ACTIVATE="${WORK_DIR}/venv/bin/activate"
#
cd ${WORK_DIR}
source "$VENV_ACTIVATE"
#
python3 new_day.py
#
