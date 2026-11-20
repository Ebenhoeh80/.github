# Contributing

Thank you for wanting to improve one of my Home Assistant integrations! This file is the default
for all repositories that do not have their own `CONTRIBUTING.md`.

## Before you start

- For anything bigger than a small fix, **open an issue or a discussion first**, so we agree on
  the direction before you spend time on code.
- Please read the repository's README, and its `RELEASING.md` if you are curious how releases work.

## Development workflow

1. Fork the repository and create a branch from `main`.
2. Make a focused change (one topic per pull request).
3. Run the tests and the linter described in the repository before you push (usually
   `pytest` and `ruff check` / `ruff format --check`).
4. Add or update tests for behaviour you change, and add an entry to `CHANGELOG.md` under
   `[Unreleased]`.
5. If you add or change user-visible text, update every translation file in the repository.
6. Open a pull request and describe **what** changed, **why**, and **how you tested it**
   (including the device or setup you used).

## Quality bar

- Follow the [Home Assistant integration quality scale](https://developers.home-assistant.io/docs/core/integration-quality-scale/).
- Never log or store credentials, tokens or commands that open something.
- Keep dependencies out of `manifest.json` that Home Assistant already provides.

## AI-assisted contributions

AI assistants are fine to use, with these rules:

- **Say so** in the pull request or issue (for example "prepared with an AI assistant"), so
  reviewers know to look closely.
- **You are responsible** for the contribution. Read, understand and test everything you submit;
  do not send unreviewed AI output.
- **Test on real hardware** where the change touches a device. Do not claim a test you did not run.
- **No secrets** in prompts, logs or examples (passwords, tokens, addresses, serial numbers,
  unlock commands).

The maintainer also works with AI tools. Every change is reviewed and tested by a human before it
is released, and pull requests and issues created that way carry a note.

## Releases and versions

Versions follow [Semantic Versioning](https://semver.org/): a breaking change raises the major
version, a new feature the minor version, a fix the patch version.

## Code of conduct

Be kind and respectful. See the [code of conduct](CODE_OF_CONDUCT.md).
