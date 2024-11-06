from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from .trading_bot import TradingBot

if __name__ == '__main__':
    bot = TradingBot()
    application = Application.builder().token(bot.token).build()
    
    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(CallbackQueryHandler(bot.button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message))
    
    application.run_polling()