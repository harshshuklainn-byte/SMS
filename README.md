# Sms-main-DEPLOY-FIXED

Deployment-safe build for Python 3.11 / python-telegram-bot 20.8.

## Required environment variable

`BOT_TOKEN` must be set in the hosting panel. The token is no longer hardcoded in `main.py`.

## Optional environment variables

- `ADMIN_IDS`
- `BOT_USERNAME`
- `ADMIN_SUPPORT`
- `VIP_SUPPORT`
- `POLL_INTERVAL` (default: 60 seconds)
- `DB_CONCURRENCY` (default: 8)
- `TYPE4_CONCURRENCY` (default: 10)
- `BOT_DB_FILE` (default: `bot_database.json`)

## Start command

`python main.py`

The Firebase refresh is deliberately bounded and delayed briefly after startup to avoid a large burst of simultaneous network requests that can cause hosting platforms to kill the process with exit code `-9`.
