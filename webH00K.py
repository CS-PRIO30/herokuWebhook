import os
from telegram.ext import *

def start(bot, update):
    bot.sendMessage(chat_id = chat_id, text= "ciao a me")

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def call(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.text))

TOKEN = os.environ['TOKEN_TELEGRAM']
PORT = int(os.environ['PORT'])

updater = Updater(TOKEN)

updater.bot.set_webhook("https://webh00k.herokuapp.com/" + TOKEN)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, callback=call))

updater.idle()
