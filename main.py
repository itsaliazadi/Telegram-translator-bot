import logging
from languages import Language
from telegram import ReplyKeyboardMarkup
from telegram.ext import (
    Filters,
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
)


TOKEN = "Your token"
UPDATER = Updater(token=TOKEN)
DISPATCHER = UPDATER.dispatcher

USERNAME = ""

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):

    global USERNAME
    user = update.message.from_user
    USERNAME += user["username"]

    welcome_text = """Hi {}!
Hope you're doing great!
In order to translate your first text using this bot,Type /translate."""
