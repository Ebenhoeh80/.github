# GitHub Sponsors: preparation / Vorbereitung

**Status:** prepared, **not active**. Nothing in the repositories points to GitHub Sponsors yet.
Everything below is ready to use as soon as the profile has been approved.
*(Deutsch: siehe weiter unten.)*

- [English](#english)
- [Deutsch](#deutsch)

---

## English

### 1. What the maintainer does once (about 30 minutes, manual)

Only the account owner can do this part; it involves identity, bank and tax details.

1. Make sure two-factor authentication is on and the profile is public.
2. Open <https://github.com/sponsors> and choose **Get sponsored** for the personal account
   `Ebenhoeh80`. Germany is a supported region.
3. Fill in the profile with the texts from section 2.
4. **Payouts:** connect a bank account through Stripe Connect (GitHub guides you). GitHub also asks for
   identity details and a tax form (people outside the US usually fill in a W-8BEN).
5. Set up the tiers from section 3 (monthly and one-time), optionally a goal.
6. Submit the profile for review. GitHub usually answers within a few days.

**Tax note (not tax advice):** sponsorship payments are generally income. In Germany that means income
tax, and possibly VAT unless the small-business rule applies. Ask a tax advisor before the first payout.

### 2. Profile text

**Short bio (one line):**

> I build and maintain open-source Home Assistant integrations for smart locks, MAX! heating and modems,
> in my spare time.

**About (profile page):**

> I write and maintain a few Home Assistant integrations that I use at home and share for free:
>
> - **WeLock Smart Lock BLE**: unlock a WeLock smart lock from Home Assistant, with an optional offline mode.
> - **eQ-3 MAX! Cube**: local control of the MAX! heating system, including weekly programmes.
> - **ZTE H186 DSL modem**: modem statistics and diagnostics.
>
> All of it is MIT-licensed and developed in the open, with tests and CI.
>
> **What your support pays for:** my time, electricity, and the development tools and IT equipment I use
> (including test hardware such as Bluetooth adapters and proxies). It is voluntary, and I am grateful for
> every contribution, however small.
>
> **What it does not buy:** support is voluntary and best effort. Sponsoring does not give a claim to
> support, features or response times.

### 3. Suggested tiers

| Tier | Amount | Meaning |
| :--- | :--- | :--- |
| Coffee | 3 € / month | A small thank-you, keeps the lights on. |
| Supporter | 5 € / month | Helps with test hardware and tools. |
| Backer | 10 € / month | Covers a good part of the running costs. |
| Patron | 25 € / month | Same as above; your name or handle appears in the README's thank-you section if your sponsorship is **public**. |
| One-time | 5 / 10 / 25 / 50 / 100 € | A single contribution. |

No tier promises anything contractual (no priority support, no feature guarantees). An optional goal:
*"Bluetooth proxies and test hardware: 100 €"*.

### 4. After GitHub has approved the profile (the assistant does this)

1. In a clone of every repository (`welock-bluetooth`, `zte-h186`, `ha-maxcube`, `.github`) run
   `python tools/activate_sponsors.py <folders>`. It adds `github: Ebenhoeh80` to `FUNDING.yml` and a
   "Sponsor on GitHub" button next to the other support buttons in every README (English, German,
   Spanish, French). Use `--dry-run` first to see what changes.
2. Commit the result in one pull request per repository.
3. Check that the **Sponsor** button appears on the repository pages (it comes from `FUNDING.yml`).
4. Optional thank-you section: a scheduled GitHub Action (for example
   `JamesIves/github-sponsors-readme-action`) can list sponsors in the README between two markers.
   **Only public sponsors are listed; private or anonymous sponsors never are.** Without sponsors the
   section is simply left out.
5. The PayPal pool and Buy Me a Coffee stay as they are (extra ways to give).

### 5. Principles

- Describe costs by project and in general terms ("time, electricity, tools and IT equipment"),
  not as an itemised bill.
- Always "voluntary", never "payment for support or features".
- Never publish names of sponsors without their consent.

---

## Deutsch

### 1. Was der Maintainer einmalig tut (etwa 30 Minuten, von Hand)

Diesen Teil kann nur der Kontoinhaber erledigen, er betrifft Identität, Bank und Steuerangaben.

1. Zwei-Faktor-Authentifizierung einschalten und das Profil öffentlich stellen.
2. <https://github.com/sponsors> öffnen und **Get sponsored** für das persönliche Konto `Ebenhoeh80`
   wählen. Deutschland ist eine unterstützte Region.
3. Das Profil mit den Texten aus Abschnitt 2 ausfüllen.
4. **Auszahlung:** Ein Bankkonto über Stripe Connect verbinden (GitHub führt dich durch die Schritte).
   GitHub fragt außerdem Identitätsangaben und ein Steuerformular ab (Personen außerhalb der USA füllen
   meist ein W-8BEN aus).
5. Die Stufen aus Abschnitt 3 anlegen (monatlich und einmalig), optional ein Ziel.
6. Das Profil zur Prüfung einreichen. GitHub antwortet meist innerhalb weniger Tage.

**Steuerhinweis (keine Steuerberatung):** Sponsoring-Zahlungen sind in der Regel Einkommen. In Deutschland
heißt das Einkommensteuer und eventuell Umsatzsteuer, sofern die Kleinunternehmerregelung nicht greift.
Vor der ersten Auszahlung bitte einen Steuerberater fragen.

### 2. Profiltext

**Kurzbeschreibung (eine Zeile):**

> Ich entwickle und pflege in meiner Freizeit quelloffene Home-Assistant-Integrationen für Smart-Locks,
> MAX!-Heizung und Modems.

**Über mich (Profilseite):**

> Ich schreibe und pflege einige Home-Assistant-Integrationen, die ich zu Hause nutze und kostenlos teile:
>
> - **WeLock Smart Lock BLE**: ein WeLock-Smart-Lock aus Home Assistant entsperren, mit optionalem Offline-Modus.
> - **eQ-3 MAX! Cube**: lokale Steuerung der MAX!-Heizung, auch mit Wochenprogrammen.
> - **ZTE H186 DSL-Modem**: Modem-Statistiken und Diagnose.
>
> Alles steht unter der MIT-Lizenz und wird offen entwickelt, mit Tests und CI.
>
> **Wofür deine Unterstützung gedacht ist:** meine Zeit, Strom sowie die Entwicklungswerkzeuge und die
> IT-Ausstattung, die ich nutze (auch Testgeräte wie Bluetooth-Adapter und -Proxys). Sie ist freiwillig,
> und ich freue mich über jeden Beitrag, egal wie klein.
>
> **Was sie nicht kauft:** Support ist freiwillig und nach bestem Bemühen. Sponsoring begründet keinen
> Anspruch auf Support, Funktionen oder Antwortzeiten.

### 3. Vorgeschlagene Stufen

| Stufe | Betrag | Bedeutung |
| :--- | :--- | :--- |
| Kaffee | 3 € / Monat | Ein kleines Dankeschön, hält das Licht an. |
| Unterstützer | 5 € / Monat | Hilft bei Testgeräten und Werkzeugen. |
| Förderer | 10 € / Monat | Deckt einen guten Teil der laufenden Kosten. |
| Gönner | 25 € / Monat | Wie oben; dein Name oder Benutzername erscheint im Dank-Abschnitt der README, wenn dein Sponsoring **öffentlich** ist. |
| Einmalig | 5 / 10 / 25 / 50 / 100 € | Ein einzelner Beitrag. |

Keine Stufe verspricht etwas Vertragliches (kein Vorrang-Support, keine Funktionszusagen). Ein optionales
Ziel: *„Bluetooth-Proxys und Testgeräte: 100 €“*.

### 4. Nachdem GitHub das Profil freigegeben hat (das erledigt der Assistent)

1. In einem Klon jedes Repositorys (`welock-bluetooth`, `zte-h186`, `ha-maxcube`, `.github`)
   `python tools/activate_sponsors.py <Ordner>` ausführen. Das Skript trägt `github: Ebenhoeh80` in die
   `FUNDING.yml` ein und setzt in jeder README (Englisch, Deutsch, Spanisch, Französisch) einen Knopf
   „Auf GitHub sponsern“ neben die übrigen Unterstützungs-Knöpfe. Mit `--dry-run` vorher ansehen, was sich ändert.
2. Das Ergebnis je Repository in einem Pull Request übernehmen.
3. Prüfen, dass der Knopf **Sponsor** auf den Repository-Seiten erscheint (er kommt aus der `FUNDING.yml`).
4. Optionaler Dank-Abschnitt: Eine geplante GitHub Action (zum Beispiel
   `JamesIves/github-sponsors-readme-action`) kann die Sponsoren in der README zwischen zwei Markern
   auflisten. **Es werden nur öffentliche Sponsoren genannt; private oder anonyme nie.** Ohne Sponsoren
   entfällt der Abschnitt einfach.
5. PayPal-Pool und Buy Me a Coffee bleiben wie sie sind (zusätzliche Wege zu geben).

### 5. Grundsätze

- Kosten projektbezogen und allgemein beschreiben („Zeit, Strom, Werkzeuge und IT-Ausstattung“), nicht als
  einzelne Rechnung.
- Immer „freiwillig“, nie „Bezahlung für Support oder Funktionen“.
- Namen von Sponsoren niemals ohne Zustimmung veröffentlichen.
