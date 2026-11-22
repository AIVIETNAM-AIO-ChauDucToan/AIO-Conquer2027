# Structure

- `src/app/` is the Python package for the Streamlit demo. It currently contains only a placeholder.
- `pyproject.toml` declares Streamlit for the UI and HTTPX for requests to the [FastAPI backend](../backend/README.md).

The demo will call the API. It will not run the model or connect to PostgreSQL directly.

# Setup

With [uv](https://docs.astral.sh/uv/) installed, run from `app/`:

```sh
uv sync
```

There is no Streamlit page to launch yet.
