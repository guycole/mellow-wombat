#!/bin/bash
#
# Title:add_schema.sh
# Description:
# Development Environment: OS X 10.15.2/postgres 12.12
# Author: G.S. Cole (guy at shastrax dot com)
#
# psql -U wombat_admin -d wombat
#
export PGDATABASE=wombat
export PGHOST=localhost
export PGPASSWORD=woofwoof
export PGUSER=wombat_admin
#
psql < heeler_daily_score.psql
psql < heeler_load_log.psql
#
