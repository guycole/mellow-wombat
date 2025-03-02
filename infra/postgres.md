#
psql -U postgres template1 (or psql -U gsc template1)
#
# (linux) su - postgres
createuser -U postgres -d -e -l -P -r -s wombat_admin
woofwoof
createuser -U postgres -e -l -P wombat_client
batabat
#
# as pg superuser
# create tablespace wombat location '/mnt/pp1/postgres/wombat';
create tablespace wombat location '/mnt/pg_tablespace/wombat';
#
#
createdb wombat -O wombat_admin -D wombat -E UTF8 -T template0 -l C
#
# psql -h localhost -p 5432 -U wombat_admin -d wombat
# psql -h localhost -p 5432 -U wombat_client -d wombat
#
# as wombat_admin
create schema wombat_v1;
grant usage on schema wombat_v1 to wombat_client;

#
# old below
# 
createuser -e -l -P -r -s mellow // batabat
createdb mellow_v1_django;
createdb mellow_v1_test;
#
psql -U mellow -h localhost -d mellow_v1_django;
#
alter role mellow set client_encoding to 'utf8';
alter role mellow set default_transaction_isolation to 'read committed';
alter role mellow set timezone to 'UTC';
#
grant all privileges on database mellow_v1_django to mellow;
grant all privileges on database mellow_v1_test to mellow;
#
https://gist.github.com/axelbdt/74898d80ceee51b69a16b575345e8457
#
