#!/bin/bash
#
# Title:freshdb.sh
# Description: reset database
# Development Environment: macOS 12.7.2, Python 3.9.18, Django 4.2.9
#
# Author: Guy Cole (guy at shastrax.com dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
rm db.sqlite3
rm heeler/migrations/000*
rm hyena/migrations/000*
rm manatee/migrations/000*
rm wombat/migrations/000*
#
source ../venv/bin/activate
python manage.py migrate
python manage.py makemigrations
#