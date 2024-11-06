import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from .prices import PricesHandler
from .wallet import WalletHandler
from .trading import TradingHandler
from .assets import AssetsHandler
from .user_data import UserDataHandler

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.ERROR)

class TradingBot:
    def __init__(self):
        self.token = "7693068198:AAGIK1DCmkUs82oFbHimsUiTrA9-WNp06GE"
        self.prices = PricesHandler(self.demo_prices)
        self.wallet = WalletHandler(self.user_wallets)
        self.trading = TradingHandler(self.trading_status, self.trading_config)
        self.assets = AssetsHandler(self.demo_assets)
        self.user_data = UserDataHandler(self.awaiting_input, self.withdraw_data, self.withdraw_state)
        
        self.demo_prices = {
            'SOL': 123.45,
            'JTO': 3.45,
            'PYTH': 1.23
        }
        self.demo_assets = {
            'SOL': {'amount': 0.5, 'change': 25},
            'JTO': {'amount': 100, 'change': 20},
            'PYTH': {'amount': 200, 'change': 18}
        }
        
    # Rest of the code remains the same