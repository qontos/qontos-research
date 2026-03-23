# QONTOS Release Checklist

When cutting a new release across the public repos, update all install references in this order.

## Pre-release → Tag Cut

1. **`qontos`**: Tag `vX.Y.Z`, push tag, update `README.md` install snippet
2. **`qontos-sim`**: Update `pyproject.toml` dependency to `qontos@vX.Y.Z`, tag `vA.B.C`, push tag, update `README.md`
3. **`qontos-examples`**: Update `requirements.txt` to pinned tags, update `README.md` install snippet
4. **`qontos-benchmarks`**: If dependencies changed, update accordingly

## Tag → PyPI (future)

When packages are published to PyPI:

1. Replace all `git+https://...@vX.Y.Z` with `package>=X.Y.Z` in:
   - `qontos-sim/pyproject.toml`
   - `qontos-examples/requirements.txt`
   - All README install snippets across repos
2. Remove "Pre-release" headers from README install sections
3. Update `.github/workflows/ci.yml` in each repo to install from PyPI

## Consistency Check

After any release, verify all three repos tell the same install story:

| Repo | File | Should Reference |
|------|------|-----------------|
| `qontos` | `README.md` | Current SDK tag |
| `qontos-sim` | `pyproject.toml` | Pinned SDK tag |
| `qontos-sim` | `README.md` | Current sim tag |
| `qontos-examples` | `requirements.txt` | Both pinned tags |
| `qontos-examples` | `README.md` | Both pinned tags |
| `qontos-benchmarks` | `pyproject.toml` | Pinned SDK tag |
| `qontos-benchmarks` | `README.md` | Current bench tag |

## Shared CI Policy Versioning

The doc-consistency checker (`check-repo-docs.sh`) is **vendored** into each public repo under `.github/scripts/`. This means each repo's CI is hermetic — it does not depend on another repo's `main` branch at runtime.

### How shared scripts are managed

| Component | Location | Versioning |
|-----------|----------|------------|
| `check-repo-docs.sh` | Vendored in each repo's `.github/scripts/` | Copied from `.github` org repo on update |
| `check-doc-consistency.sh` | `.github` org repo only (cross-repo) | Runs in `.github` CI only |
| `doc-check.yml` | Each repo's `.github/workflows/` | Uses local vendored script |
| `doc-consistency.yml` | `.github` org repo only | Clones all 5 repos at runtime |

### Updating the shared checker

When the doc-consistency rules change:

1. Update `check-repo-docs.sh` in the `.github` org repo
2. Copy the updated script to each public repo:
   ```bash
   for repo in qontos qontos-sim qontos-examples qontos-benchmarks qontos-research; do
     cp .github/scripts/check-repo-docs.sh "${repo}/.github/scripts/check-repo-docs.sh"
   done
   ```
3. Commit and push each repo
4. The org-level `doc-consistency.yml` will also pick up the new rules automatically

### Why vendored, not fetched

- **Hermetic**: A repo's CI result depends only on that repo's committed content
- **Auditable**: `git log .github/scripts/check-repo-docs.sh` shows when rules changed
- **No surprise breaks**: Updating `.github` doesn't silently break other repos' CI
- **Trade-off**: Requires manual propagation (5 copies), but the update is rare and simple
