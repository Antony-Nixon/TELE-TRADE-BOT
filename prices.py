from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class PricesHandler:
    def __init__(self, demo_prices):
        self.demo_prices = demo_prices

    async def show_prices(self, message):
        price_text = "💰 *Current Prices*\n\n"
        for token, price in self.demo_prices.items():
            price_text += f"{token}: ${price:,.2f}\n"
        
        keyboard = [[InlineKeyboardButton("↩️ Back", callback_data='main_menu')]]
        await message.edit_text(
            price_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )