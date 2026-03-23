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
