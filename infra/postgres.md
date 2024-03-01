postgres 15

sudo su - postgres

createdb wombat_v1

# createdb -e -E UTF8 -l en_US.UTF-8 -T template0 testaroo

mellow_v1=# select version();
                                                         version                                                         
-------------------------------------------------------------------------------------------------------------------------
 PostgreSQL 15.6 (Debian 15.6-0+deb12u1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
(1 row)


createuser -e -l -P -r -s wombat
batbat

alter role wombat set client_encoding to 'utf8';
alter role wombat set default_transaction_isolation to 'read committed';
alter role wombat set timezone to 'UTC';

psql -U wombat -h localhost -d wombat_v1;


create database mellow_v1;
create user mellow_admin with password 'bogus';

alter role mellow_admin set client_encoding to 'utf8';
alter role mellow_admin set default_transaction_isolation to 'read committed';
alter role mellow_admin set timezone to 'UTC';

\connect mellow_v1;
CREATE SCHEMA mellow AUTHORIZATION mellow_admin;

grant all privileges on database mellow_v1 to mellow_admin;

https://gist.github.com/axelbdt/74898d80ceee51b69a16b575345e8457

\dt mellow.*

