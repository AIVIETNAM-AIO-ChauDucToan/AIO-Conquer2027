# Structure

- `init.sql` is reserved for the PostgreSQL schema and is currently empty.

The [backend](../backend/README.md) will use asyncpg to write logs to PostgreSQL. Database logging is not wired up yet.

# Setup

There is no schema to apply yet. Once `init.sql` contains a schema, run the following from `db/` against a running PostgreSQL server and an existing database:

```sh
psql -v ON_ERROR_STOP=1 -h localhost -U db_user -d db_name -f init.sql
```

Replace `db_user` and `db_name` with your PostgreSQL role and database name. This folder has no `uv` project or lockfile.
