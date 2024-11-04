from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class TradingHandler:
    def __init__(self, trading_status, trading_config):
        self.trading_status = trading_status
        self.trading_config = trading_config

    def get_trading_config(self, user_id: str) -> dict:
        if user_id not in self.trading_config:
            self.trading_config[user_id] = {
                'amount': 0.5,
                'target': 2,
                'stoploss': 1
            }
        return self.trading_config[user_id]

    async def show_trading_panel(self, message, user_id: str):
        config = self.get_trading_config(user_id)
        is_enabled = self.trading_status.get(user_id, False)
        
        keyboard = [
            [InlineKeyboardButton(
                "🔴 Disable Trading" if is_enabled else "🟢 Enable Trading", 
                callback_data='toggle_trading'
            )],
            [InlineKeyboardButton(f"Amount: {config['amount']} SOL", callback_data='set_amount')],
            [
                InlineKeyboardButton(f"Target: {config['target']}%", callback_data='set_target'),
                InlineKeyboardButton(f"Stoploss: {config['stoploss']}%", callback_data='set_stoploss')
            ],
            [InlineKeyboardButton("↩️ Back to Menu", callback_data='main_menu')]
        ]
        
        await message.reply_text(
            "📊 *Trading Panel*\n" +
            f"Status: {'🟢 Active' if is_enabled else '🔴 Inactive'}",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        