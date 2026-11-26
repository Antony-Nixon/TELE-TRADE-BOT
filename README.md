# Telegram Crypto Trading Bot (Experimental)

An unfinished Telegram bot prototype for exploring crypto price displays, wallet flows, asset views, and trading controls.

> **Status: experimental and incomplete.**
>
> This project is not production-ready, is not financial advice, and must not be used with real funds without a complete security review, tested risk controls, and independent validation.

## Prototype capabilities

- Telegram command and callback handling
- Demo token prices and demo asset data
- Per-user trading configuration
- Trading enable/disable controls
- Wallet menu and withdrawal-flow placeholders
- Separate modules for prices, assets, trading, wallet, and user input

## Security warning

The original repository contained a hard-coded Telegram bot token. That credential must be revoked and regenerated in Telegram through BotFather. Removing a token from a later commit does not invalidate it if it was ever committed.

The original wallet prototype also included private-key fields. Never collect, log, transmit, or persist private keys in a Telegram bot. Use a properly reviewed custody or signing architecture instead.

This project should remain in demo or paper-trading mode until the following are complete:

- Environment-based secrets management
- No private-key handling in the bot process
- Authentication and authorization design
- Transaction confirmation and replay protection
- Position limits, loss limits, and emergency shutdown
- Auditable exchange integration
- Comprehensive tests with mocked providers
- Dependency and deployment security review

## Configuration

Set the token outside the repository:

```bash
$env:TELEGRAM_BOT_TOKEN="replace-with-a-new-token"
```

On Linux/macOS:

```bash
export TELEGRAM_BOT_TOKEN="replace-with-a-new-token"
```

The application now reads `TELEGRAM_BOT_TOKEN` from the environment. Do not commit `.env`, tokens, wallet keys, exchange credentials, or deployment secrets.

## Project structure

```text
main.py          Telegram application entry point
trading_bot.py   Bot composition and demo state
trading.py       Trading controls and configuration UI
prices.py        Demo price display
assets.py        Demo asset display
wallet.py        Wallet menu prototype
user_data.py     Input and withdrawal-flow placeholders
```

## Safe development direction

1. Make the demo flow run without real exchange or wallet access.
2. Add unit tests around every state transition.
3. Introduce typed domain models for orders, balances, and risk limits.
4. Add a paper-trading provider with deterministic fixtures.
5. Add explicit authorization checks per Telegram user.
6. Add risk controls and an emergency stop before any live integration.
7. Keep live trading disabled by default.

## Roadmap

- Complete missing handlers and state transitions
- Add dependency metadata and reproducible setup
- Add test coverage and linting
- Add dry-run and paper-trading modes
- Replace private-key handling with a safer signing boundary
- Add structured audit logs without secrets
- Document deployment and incident response

## License

No license has been selected yet. Until a license is added, the repository remains source-available but does not grant broad reuse rights.

## Author

Built and maintained by Antony Nixon.
