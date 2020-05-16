from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.update import Update
from src.utils.exceptions import WrongSetupError
import requests
import re
import os

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bark(update: Update, context: CallbackContext):
    url = get_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if (not token):
        raise WrongSetupError("bot token should be set")
    updater = Updater('1298281693:AAGbWqq38q4qIRR36LhS9W7xsBrP2V3t-J8', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bark',bark))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()