from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class AssetsHandler:
    def __init__(self, demo_assets):
        self.demo_assets = demo_assets

    async def show_assets(self, message, user_id: str):
        assets_text = "💼 *Your Assets*\n\n"
        for token, data in self.demo_assets.items():
            assets_text += f"{token}: {data['amount']} (${self.demo_prices[token]:,.2f}) | {data['change']}%\n"
        
        keyboard = [[InlineKeyboardButton("↩️ Back", callback_data='main_menu')]]
        await message.edit_text(
            assets_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )