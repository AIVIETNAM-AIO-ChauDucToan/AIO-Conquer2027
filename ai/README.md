# Structure

- `src/ai/` is the package for model code written from scratch. Training and inference are not implemented yet.
- `pyproject.toml` lists NumPy as the only runtime dependency.

The [backend](../backend/README.md) installs this package from the same checkout. It does not run as a separate service.

# Setup

With [uv](https://docs.astral.sh/uv/) installed, run from `ai/`:

```sh
uv sync
```

This creates a standalone environment for model development. `uv sync` in `backend/` also installs this package into the backend environment.
