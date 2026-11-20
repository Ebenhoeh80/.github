# Security Policy

This policy applies to all of my repositories that do not have their own `SECURITY.md`.

## Supported versions

Only the **latest release** of an integration receives security fixes. Please update first and
check whether the problem still exists.

## Reporting a vulnerability

1. **Do not open a public issue.**
2. Open the repository's **Security** tab and choose **Report a vulnerability**
   (GitHub private vulnerability reporting).
3. Describe what you found, how to reproduce it, which version is affected and what the impact is.

I work on these projects in my free time and answer on a best-effort basis, usually within a few
days. I will work with you on a coordinated disclosure and credit you if you like.

## What is in scope

- The integration code in this repository and its release zip.
- How the integration stores, logs and transmits credentials, tokens and commands.

Out of scope: vulnerabilities in the vendor's cloud service, in the devices' firmware or in Home
Assistant itself. Please report those to the respective vendor or project.

## Notes for integrations that control physical access (door locks)

- Stored unlock commands are sensitive: anyone who can read them from Home Assistant's storage
  and is within Bluetooth range may be able to open the lock. Protect access to your Home
  Assistant configuration and backups accordingly.
- Credentials, tokens and commands must never appear in logs or diagnostics. If you find one
  that does, that is a vulnerability: please report it privately.
