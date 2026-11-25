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

## GitHub Sponsors (active)

[SPONSORS-CONTENT.md](SPONSORS-CONTENT.md) holds the final copy-paste profile texts (English and German),
tiers and goal. [GITHUB-SPONSORS.md](GITHUB-SPONSORS.md) keeps the background and setup principles.
`tools/activate_sponsors.py` adds the Sponsor button and the `FUNDING.yml` entry to the repositories.

## ❤️ Support this project

<div align="center">

**I maintain these shared community files and workflows in my free time and cover the running costs myself.**

Sponsoring is voluntary and does not buy support, features or response times. Every contribution, however small, helps. Thank you! 🙏

<a href="https://github.com/sponsors/Ebenhoeh80">
  <img src="https://img.shields.io/badge/%E2%9D%A4%20Sponsor%20on%20GitHub-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="GitHub Sponsors" height="42">
</a>
<a href="https://www.paypal.com/pool/9p84qTHCFr?sr=wccr">
  <img src="https://img.shields.io/badge/%E2%9D%A4%20Donate%20via%20PayPal-PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="Donate via PayPal" height="42">
</a>
<a href="https://buymeacoffee.com/daneben">
  <img src="https://img.shields.io/badge/%E2%98%95%20Buy%20me%20a%20coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee" height="42">
</a>

</div>

