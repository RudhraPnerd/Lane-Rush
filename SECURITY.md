# Security Policy

## Supported versions

Lane Rush is a small hobby project, so only the latest version on the `main` branch receives fixes.

| Version | Supported |
|---------|-----------|
| Latest (`main`) | ✅ |
| Older versions | ❌ |

## Reporting a vulnerability

If you find a security issue, please **don't open a public issue**. Report it privately so it can be fixed before it's widely known.

**Preferred:** use GitHub's private reporting. Go to the **Security** tab of this repository and choose **Report a vulnerability**.

**Alternative:** email **your-email@example.com** with the subject line `Lane Rush security report`.

Please include:

- A description of the issue and its potential impact
- Steps to reproduce it
- The affected file or feature, if you know it
- Your operating system and Python and Pygame versions

## What to expect

- **Acknowledgement** within about 7 days
- **An assessment and next steps** as soon as I've looked into it
- **Credit** in the fix or release notes if you'd like it, or anonymity if you prefer

This is a volunteer project, so response times may vary, but every report will be read.

## Scope

Lane Rush is an offline game with no server, accounts, or network features. The things most likely to matter are:

- Reading and writing local files, such as `high_score.txt`
- Loading assets (images, sounds, fonts) from disk
- Vulnerabilities in dependencies, mainly [Pygame](https://www.pygame.org/)

Gameplay bugs, crashes that don't affect security, and issues in Pygame itself should be reported through the normal channels: open a regular issue here, or report the Pygame ones to the Pygame project.

## Staying safe

- Download Lane Rush only from this repository's official page.
- Install dependencies from [PyPI](https://pypi.org/project/pygame/) with `pip install pygame`, and keep Pygame up to date.
- If you share custom assets or modified `.py` files, only run files from sources you trust, since Python files run with full access to your computer.