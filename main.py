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

# Starting the conversation with the user
def start(update, context):

    global USERNAME
    user = update.message.from_user
    USERNAME += user["username"]

    welcome_text = """Hi {}!
Hope you're doing great!
In order to translate your first text using this bot,Type /translate."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)


TEXT, LANGUAGE = range(2)
# Asking the user for the text
def start_translation(update, context):

    explanation_text = "What's the text you want to translate?!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=explanation_text)

    return TEXT



