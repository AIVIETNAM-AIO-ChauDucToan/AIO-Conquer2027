# Structure

- `src/backend/main.py` creates the FastAPI application and registers routers with `app.include_router()`.
- `src/backend/routers/health.py` defines `GET /health` using `APIRouter`.
- `pyproject.toml` configures `backend.main:app` as the FastAPI CLI entry point and declares `fastapi[standard]`, asyncpg, and the editable local [`ai`](../ai/README.md) package.

The layout follows the [FastAPI guide for multi-file apps](https://fastapi.tiangolo.com/tutorial/bigger-applications/). The health endpoint checks that the API is running. Model inference and [PostgreSQL logging](../db/README.md) are not wired up yet.

# Setup

With [uv](https://docs.astral.sh/uv/) installed, run these commands from `backend/`. Keep `ai/` next to `backend/` so uv can install it from `../ai`.

```sh
uv sync
uv run fastapi dev
```

Open [the API docs](http://127.0.0.1:8000/docs) or visit [`/health`](http://127.0.0.1:8000/health) to see `{"status":"ok"}`. No database is needed for this endpoint.
