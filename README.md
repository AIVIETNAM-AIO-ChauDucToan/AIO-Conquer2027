# Structure

AIO-Conquer2027 is a demo project for a model built from scratch with NumPy. The planned flow is Streamlit → FastAPI → NumPy model, with FastAPI writing logs to PostgreSQL.

| Directory | Purpose |
| --- | --- |
| [`app/`](app/README.md) | Streamlit demo and HTTP client |
| [`backend/`](backend/README.md) | FastAPI service and routes |
| [`ai/`](ai/README.md) | NumPy model package |
| [`db/`](db/README.md) | PostgreSQL schema |
| [`notebooks/`](notebooks/README.md) | Experiments and exploration |

# Setup

Install [uv](https://docs.astral.sh/uv/). The Python projects target Python 3.14 and each has its own `uv.lock`. From the repository root:

```sh
uv sync --directory ai
uv sync --directory backend
uv sync --directory app
```

To start the API, run `uv run --directory backend fastapi dev` and open [the API docs](http://127.0.0.1:8000/docs). Only the health endpoint is implemented; PostgreSQL is not required to start the API yet.

# Rules

See [RULES.md](RULES.md) for commit message conventions and the review process. Changes reach `main` through a pull request approved by another contributor or a repository maintainer.

# Acknowledgements

Thanks to AIO-ChauDucToan and to all project authors, contributors, and reviewers for their work on AIO-Conquer2027.

# License

This project is licensed under the GNU Affero General Public License version 3 (AGPLv3). See [LICENSE](LICENSE) for the full text.
