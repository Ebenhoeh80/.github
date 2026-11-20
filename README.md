# Ebenhoeh80/.github

Shared community health files and reusable workflows for my Home Assistant integrations
([welock-bluetooth](https://github.com/Ebenhoeh80/welock-bluetooth),
[zte-h186](https://github.com/Ebenhoeh80/zte-h186),
[ha-maxcube](https://github.com/Ebenhoeh80/ha-maxcube), …).

GitHub uses these files as **defaults** for every repository of this account that does not have its
own copy: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `FUNDING.yml` and the
issue templates in `ISSUE_TEMPLATE/`. A repository can still override any of them.

## Reusable workflow: release zip

`.github/workflows/release-zip.yml` builds the HACS release zip, checks that the tag matches the
version in `manifest.json`, and creates or updates the GitHub release with the matching
`CHANGELOG.md` section and the zip attached.

Use it from a repository (`.github/workflows/release-zip.yml`):

```yaml
name: Release zip
on:
  push:
    tags: ["v*"]
permissions:
  contents: write
jobs:
  release:
    uses: Ebenhoeh80/.github/.github/workflows/release-zip.yml@v1
    with:
      domain: welock   # folder under custom_components/
```

The zip contains the integration files at its root (what HACS expects with `zip_release`), and
`hacs.json` needs `"zip_release": true` and `"filename": "<domain>.zip"`.

Versions of this workflow are tagged (`v1`, …); callers pin a major tag.

## GitHub Sponsors (prepared, not active)

[GITHUB-SPONSORS.md](GITHUB-SPONSORS.md) (English and German) holds the profile texts, the suggested tiers
and the steps for the one-time setup. `tools/activate_sponsors.py` adds the Sponsor button to the funding
file and the READMEs of the repositories once GitHub has approved the profile.
