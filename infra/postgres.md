#
createuser -e -l -P -r -s mellow // batabat
createdb mellow_v1
#
psql -U mellow -h localhost -d mellow_v1;
#
alter role mellow set client_encoding to 'utf8';
alter role mellow set default_transaction_isolation to 'read committed';
alter role mellow set timezone to 'UTC';
#
grant all privileges on database mellow_v1 to mellow;
#
https://gist.github.com/axelbdt/74898d80ceee51b69a16b575345e8457
#
