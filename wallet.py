from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class WalletHandler:
    def __init__(self, user_wallets):
        self.user_wallets = user_wallets

    def has_wallet(self, user_id: str) -> bool:
        return user_id in self.user_wallets

    def set_wallet(self, user_id: str, private_key: str, public_key: str) -> None:
        self.user_wallets[user_id] = {
            'private_key': private_key,
            'public_key': public_key
        }

    async def handle_wallet(self, message, user_id: str):
        if not self.has_wallet(user_id):
            keyboard = [
                [InlineKeyboardButton("➕ Create New Wallet", callback_data='create_wallet')],
                [InlineKeyboardButton("🔑 Use Existing Wallet", callback_data='use_existing')]
            ]
            await message.edit_text(
                "👛 *Wallet Setup*\nChoose an option:",
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='Markdown'
            )
        else:
            keyboard = [
                [InlineKeyboardButton("🔄 Change Wallet", callback_data='change_wallet')],
                [
                    InlineKeyboardButton("📥 Deposit", callback_data='deposit'),
                    InlineKeyboardButton("📤 Withdraw", callback_data='withdraw')
                ],
                [InlineKeyboardButton("↩️ Back", callback_data='main_menu')]
            ]
            await message.edit_text(
                "👛 *Wallet Settings*",
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='Markdown'
            )