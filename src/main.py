import logging
from translation import Language
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

# User's information
USERNAME = ""

translation_text = ""
translation_lan  = ""

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Starting the conversation with the user
def start(update, context):

    global USERNAME
    user = update.message.from_user
    USERNAME += user["username"]

    welcome_text = """Hi {}!
Hope you're doing great!
In order to translate your first text using this bot,type /translate.""".format(USERNAME)
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)


TEXT, LANGUAGE = range(2)
# Asking the user for the text
def start_translation(update, context):

    explanation_text = "What's the text you want to translate?!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=explanation_text)

    return TEXT


# Saving the text and asking for the language
def save_text(update, context):

    global translation_text
    # Saving the text
    translation_text += update.message.text

    ask_for_lan = "What language do you want to translate it to?"
    supported_languages_giude = """You can also visit https://cloud.google.com/translate/docs/languages to get a list of the 
supported languages and their abbreviated form."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=ask_for_lan)
    context.bot.send_message(chat_id=update.effective_chat.id, text=supported_languages_giude)

    return LANGUAGE


# Sending the user the translation
def translate(update, context):

    global translation_text
    global translation_lan
    # Saving the translation language
    translation_lan = update.message.text.lower()

    # Translating
    translation_object = Language()
    translation_message = translation_object.translate_text(translation_text, translation_lan)
    context.bot.send_message(chat_id=update.effective_chat.id, text=translation_message)

    return ConversationHandler.END


# Cancel function in case the user wanted to break the process
def cancel(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text="We can do it another time!")

    return ConversationHandler.END


# The handlers
start_handler = CommandHandler("start", start)

conv_handler_translate = ConversationHandler(
    entry_points=[CommandHandler("translate", start_translation)],
    states={
        TEXT : [MessageHandler(Filters.text & ~Filters.command, save_text)],
        LANGUAGE : [MessageHandler(Filters.text & ~Filters.command, translate)],
    },
    fallbacks=[CommandHandler("cancel", cancel)]
)

# Adding the handlers to the dispatcher
DISPATCHER.add_handler(start_handler)
DISPATCHER.add_handler(conv_handler_translate)

UPDATER.start_polling()

