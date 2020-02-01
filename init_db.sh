#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL

CREATE TABLE results (
id serial primary key not null,
uuid uuid not null,
top int,
bottom int,
answer double precision,
created timestamp
);
alter table results alter column created set default current_timestamp;

EOSQL

