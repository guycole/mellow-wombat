#!/bin/bash
#
# Title:drop_schema.sh
# Description: remove schema
# Development Environment: OS X 10.15.2/postgres 12.12
# Author: G.S. Cole (guy at shastrax dot com)
#
export PGDATABASE=wombat
export PGHOST=localhost
export PGPASSWORD=woofwoof
export PGUSER=wombat_admin
#
psql $PGDATABASE -c "drop table wombat_host"
psql $PGDATABASE -c "drop table wombat_tasking"
#
