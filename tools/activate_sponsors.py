"""Adds GitHub Sponsors to the funding setup of the repositories. Run it only AFTER GitHub has approved
the Sponsors profile (otherwise the Sponsor button points to a page that does not exist yet).

What it does in each repository folder you pass (all changes are idempotent):
  * `.github/FUNDING.yml`: adds `github: <user>` (other entries stay),
  * every `README*.md`: adds a "Sponsor on GitHub" button next to the existing support buttons.

Usage:
    python tools/activate_sponsors.py --dry-run ../welock-bluetooth ../zte-h186 ../ha-maxcube ../github-defaults
    python tools/activate_sponsors.py ../welock-bluetooth ...        # writes the files
Review the changes with `git diff`, then commit them through a pull request as usual.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

USER = "Ebenhoeh80"
SPONSORS_URL = f"https://github.com/sponsors/{USER}"

LABELS = {
    "en": ("Sponsor on GitHub", "GitHub Sponsors"),
    "de": ("Auf GitHub sponsern", "GitHub Sponsors"),
    "es": ("Patrocinar en GitHub", "GitHub Sponsors"),
    "fr": ("Parrainer sur GitHub", "GitHub Sponsors"),
}


def language_of(path: Path) -> str:
    """README.md is English; README.de.md is German, and so on."""
    match = re.search(r"README\.([a-z]{2})\.md$", path.name)
    return match.group(1) if match else "en"


def sponsor_button(lang: str) -> str:
    """The HTML for the button, in the style of the other support buttons."""
    label, alt = LABELS.get(lang, LABELS["en"])
    badge = label.replace(" ", "%20")
    return (
        f'<a href="{SPONSORS_URL}">\n'
        f'  <img src="https://img.shields.io/badge/%E2%9D%A4%20{badge}-EA4AAA?style=for-the-badge'
        f'&logo=githubsponsors&logoColor=white" alt="{alt}" height="42">\n'
        "</a>\n"
    )


def update_readme(text: str, lang: str) -> str | None:
    """Return the README with the button added, or ``None`` if there is nothing to change."""
    if SPONSORS_URL in text:
        return None
    # The support block ends with the Buy Me a Coffee button (or, failing that, the PayPal one).
    for marker in ("https://buymeacoffee.com/", "https://www.paypal.com/pool/"):
        pattern = re.compile(rf'(<a href="{re.escape(marker)}[^"]*">\n  <img [^\n]*\n</a>\n)')
        matches = list(pattern.finditer(text))
        if matches:
            last = matches[-1]
            return text[: last.end()] + sponsor_button(lang) + text[last.end() :]
    return None


def update_funding(text: str) -> str | None:
    """Return FUNDING.yml with `github: <user>` added, or ``None`` if it is already there."""
    if re.search(r"^github:", text, re.M):
        return None
    return f"github: {USER}\n" + text


def process(folder: Path, dry_run: bool) -> list[str]:
    """Change the files of one repository folder; return what was (or would be) changed."""
    changed: list[str] = []
    # FUNDING.yml lives in `.github/` of a normal repository and in the root of the `.github` repository.
    fundings = [f for f in (folder / ".github" / "FUNDING.yml", folder / "FUNDING.yml") if f.exists()]
    candidates = [(funding, None) for funding in fundings]
    candidates += [(readme, language_of(readme)) for readme in sorted(folder.glob("README*.md"))]
    for path, lang in candidates:
        raw = path.read_text(encoding="utf-8")
        newline = "\r\n" if "\r\n" in raw else "\n"
        text = raw.replace("\r\n", "\n")
        updated = update_funding(text) if lang is None else update_readme(text, lang)
        if updated is None:
            continue
        changed.append(str(path))
        if not dry_run:
            path.write_text(updated.replace("\n", newline), encoding="utf-8", newline="")
    return changed


def main() -> int:
    """Command line entry point."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("folders", nargs="+", type=Path, help="repository folders to change")
    parser.add_argument("--dry-run", action="store_true", help="only list what would change")
    args = parser.parse_args()
    exit_code = 0
    for folder in args.folders:
        if not folder.is_dir():
            print(f"{folder}: not a folder", file=sys.stderr)
            exit_code = 1
            continue
        changed = process(folder, args.dry_run)
        verb = "would change" if args.dry_run else "changed"
        print(f"{folder}: {verb} {len(changed)} file(s)")
        for name in changed:
            print(f"  {name}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
