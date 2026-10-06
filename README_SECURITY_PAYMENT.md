# KRYON HOST — Security + Payment Update

## Required host environment
BOT_TOKEN=YOUR_BOT_TOKEN
OWNER_ID=YOUR_OWNER_ID

BHARATPE_MERCHANT_ID=YOUR_MERCHANT_ID
BHARATPE_TOKEN=YOUR_BHARATPE_TOKEN

Extra admins are managed from the Admin Panel, not ADMIN_IDS.

## Payment methods
PhonePe, Paytm, Google Pay, FamPay, Navi UPI, BharatPe — Auto Verification, Binance Pay, and Indian Bank Transfer.

UPI methods support admin-configured UPI IDs and dynamic UPI QR generation. BharatPe uses the configured merchant credentials only for backend UTR/amount verification when Auto-Approve is enabled.

## Security
Child bot ENV values are encrypted at rest and excluded from GitHub metadata backups. Host-only secrets are not inherited by child processes. Logs redact common credential patterns.
