# KRYON Hosting Bot — Overall Fixed

## Environment variables

Only these variables are required/configurable through ENV:

- `BOT_TOKEN` — main hosting bot token
- `OWNER_ID` — main owner Telegram ID
- `BHARATPE_MERCHANT_ID` — optional BharatPe merchant ID for automatic verification
- `BHARATPE_TOKEN` — optional BharatPe API token for automatic verification

Additional admins are managed from the Admin Panel and are persisted in the bot database. No `ADMIN_IDS` variable is required.

## Payments

Supports Indian UPI methods (PhonePe, Paytm, Google Pay, FamPay, Navi UPI), Binance Pay, and Indian bank transfer. UPI IDs and bank details are configured from the Admin Panel. UPI QR is generated from the configured UPI ID and selected amount.

BharatPe verification is optional. When configured and Auto-Approve is enabled, submitted UTRs are checked against BharatPe transaction data before automatic approval.

## Credential security

- Child bot ENV values are encrypted at rest in the panel database.
- Child ENV values are never written to per-bot JSON or GitHub `bot_meta.json`.
- GitHub `user_data.json` backups are serialized through the encrypted vault; secret settings are omitted from `settings.json` backups.
- Host secrets are removed from the process OS environment after startup so child subprocesses do not inherit them.
- Child processes are launched through `secure_exec.py` with Linux dumpability/ptrace hardening where supported.
- Child output is redacted for common Telegram tokens, API keys, passwords and database URLs.

This protects credentials at rest and isolates the host environment as far as a single-host subprocess architecture permits. Fully hostile third-party code requires OS/container isolation for a hard security boundary.

## Stability / isolation fixes

- Panel persistence uses the dedicated `kryon_host` MongoDB database by default. Child bots may use their own MongoDB databases (for example `Anon`) without sharing panel collections.
- A Mongo-backed runtime lease prevents multiple panel replicas from polling the same Telegram token at once.
- Bot records are merged against the newest DB snapshot before save, preventing concurrent user deployments from erasing other users' bot records.
- Child RAM is reserved before startup against a host-wide safety budget; if the host cannot safely fit another bot, the panel rejects that start instead of risking an OOM crash.
- Dependency installation is limited to two concurrent installers to reduce pip/npm CPU/RAM spikes during mass deployments.
- Existing per-bot RAM enforcement remains enabled.

