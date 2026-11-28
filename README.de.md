# Ebenhoeh80/.github

[Deutsch](README.de.md) · [English](README.md)

Gemeinsame Community-Dateien und wiederverwendbare Workflows für meine Home-Assistant-Integrationen
([welock-bluetooth](https://github.com/Ebenhoeh80/welock-bluetooth),
[zte-h186](https://github.com/Ebenhoeh80/zte-h186),
[ha-maxcube](https://github.com/Ebenhoeh80/ha-maxcube), …).

GitHub verwendet diese Dateien als **Standard** für jedes Repository dieses Kontos, das keine eigene
Kopie besitzt: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `FUNDING.yml` und die
Vorlagen in `ISSUE_TEMPLATE/`. Ein Repository kann jede dieser Dateien weiterhin überschreiben.

## Wiederverwendbarer Workflow: Release-Zip

`.github/workflows/release-zip.yml` erstellt das HACS-Release-Zip, prüft, ob der Tag zur Version in
`manifest.json` passt, und erstellt bzw. aktualisiert das GitHub-Release mit dem passenden Abschnitt aus
`CHANGELOG.md` und dem angehängten Zip.

Aufruf aus einem Repository (`.github/workflows/release-zip.yml`):

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
      domain: welock   # Ordner unter custom_components/
```

Das Zip enthält die Integrationsdateien direkt im Wurzelverzeichnis (so erwartet es HACS bei
`zip_release`), und `hacs.json` benötigt `"zip_release": true` und `"filename": "<domain>.zip"`.

Versionen dieses Workflows sind getaggt (`v1`, …); aufrufende Repositories pinnen ein Major-Tag.

## GitHub Sponsors (vorbereitet, nicht aktiv)

[GITHUB-SPONSORS.md](GITHUB-SPONSORS.md) (Englisch und Deutsch) enthält die Profiltexte, die
vorgeschlagenen Stufen und die Schritte für die einmalige Einrichtung. `tools/activate_sponsors.py`
ergänzt den Sponsor-Knopf in der Funding-Datei und in den READMEs der Repositories, sobald GitHub das
Profil freigegeben hat.
