# Release Checklist

This checklist is the release gate for a tagged GitHub release.

## Versioning
- [ ] Update `pyproject.toml` version (SemVer).
- [ ] Ensure `dpi-lab --version` reports the same version.
- [ ] Ensure `run/manifest.json` includes `workbench_version`.

## Packaging (hard requirement)
- [ ] From a clean environment: `pip install .` succeeds.
- [ ] `dpi-lab --help` and `dpi-lab review --help` succeed.
- [ ] Installed package includes required resources:
  - `dpi_lab/resources/schemas/**`
  - `dpi_lab/resources/templates/**`
  - `dpi_lab/resources/reviews/templates/**`

## Smoke tests (offline)
- [ ] `dpi-lab review --engine local --pdf <small.pdf> --slug smoke --out ./tmp-reviews`
- [ ] `dpi-lab validate ./tmp-reviews/smoke`

## Example outputs
- [ ] `dpi-lab validate reviews/examples-batch/<example>` passes for each example directory (schema level).

## CI gates
- [ ] CI runs `pip install .` (not just `pip install -r requirements.txt`).
- [ ] CI runs an offline smoke review and validation.
- [ ] CI validates example review outputs.

## Release notes
- [ ] Update `CHANGELOG.md`.
- [ ] GitHub Release notes include quickstart commands and determinism caveats.

## Tagging
- [ ] Tag from `main` on the intended commit: `vX.Y.Z`
- [ ] Attach release assets (optional): `...-examples.zip`
