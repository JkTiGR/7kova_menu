import logging
import random
import string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes


# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your API token from BotFather
API_TOKEN = '7363060925:AAGEHJfI4_ZqeMjnjXMCKXWUS2Y9X6052U0'

# Language selection command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Get user's first name
    user = update.effective_user
    first_name = user.first_name if user.first_name else "Bạn"

    # Send intro image with caption
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open("7kova_logo.jpg", 'rb'),
        caption=f"{first_name}, welcome to 7KOVA!"
    )
    
    # Provide options for language selection
    keyboard = [
        [InlineKeyboardButton("-       HOME      -", url="https://t.me/sevenkova7")],
        [InlineKeyboardButton("-     ДУБЛЯНКИ    -", url="https://t.me/sevenkova_dublenki")],
        [InlineKeyboardButton("-      ЖИЛЕТИ     -", url="https://t.me/+Q6ceh5-SyG05Mjdi")],
        [InlineKeyboardButton("-      КОСТЮМ     -", url="https://t.me/+Fkc5TxrnUPE2YzMy")],
        [InlineKeyboardButton("-      КУРТКИ     -", url="https://t.me/+IMzsArv-APQxNDcy")],
        [InlineKeyboardButton("-      СОРОЧКИ    -", url="https://t.me/+shrAerJsuhdlZDUy")],
        [InlineKeyboardButton("-       ШТАНИ     -", url="https://t.me/+rwStCex6jDs3YTAy")],
        [InlineKeyboardButton("-       ШУБИ      -", url="https://t.me/+Sln8niuQsxZlZTJi")],
        [InlineKeyboardButton("-     СПІДНИЦІ    -", url="https://t.me/sevenkova_youbki")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("MENU", reply_markup=reply_markup)


def main():
    # Create the application and register the handlers
    application = Application.builder().token(API_TOKEN).build()

    # Command /start
    application.add_handler(CommandHandler("start", start))

    # Start polling
    application.run_polling()

if __name__ == "__main__":
    main()
