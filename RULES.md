# Contribution rules

## Commit messages

Use `type(scope): description`. Omit the scope for repository-wide changes (`type: description`). When a change belongs to one module, use its directory name as the scope: `app`, `backend`, `ai`, `db`, or `notebooks`.

| Type | Use for | Example |
| --- | --- | --- |
| `feat` | New functionality | `feat(backend): add health endpoint` |
| `fix` | Bug fixes | `fix(app): handle API timeouts` |
| `docs` | Documentation changes | `docs: update setup instructions` |
| `refactor` | Code changes that preserve behavior | `refactor(ai): simplify input validation` |
| `test` | Test additions or updates | `test(backend): cover the health endpoint` |
| `chore` | Maintenance, tooling, or dependencies | `chore: update dependency lockfiles` |

Keep each commit focused on one change. Write a short description that starts with a verb, such as `add`, `fix`, or `update`.

## Review and merge

1. Create a branch from `main` and push your commits to that branch. Do not push directly to `main`.
2. Open a pull request targeting `main`. Explain what changed and how you verified it. Run the relevant checks locally and include the updated `uv.lock` for any Python project whose dependencies changed.
3. Address review feedback and wait for at least one approval from another contributor or a repository maintainer. Your own approval does not count. If you make substantial changes after approval, request another review.
4. Merge only after approval and after any required checks pass. Never force-push to `main`.

Do not commit credentials, `.env` files containing secrets, or local virtual environments.
