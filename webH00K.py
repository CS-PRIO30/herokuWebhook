import os
from telegram.ext import Updater


TOKEN = os.environ['TOKEN_TELEGRAM']
PORT = int(os.environ['PORT'])
updater = Updater(TOKEN)
# add handlers

updater.bot.set_webhook("https://webh00k.herokuapp.com/" + TOKEN)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)

def echo(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


dispatcher = updater.dispatcher
dispatcher.addTelegramMessageHandler(echo)

updater.idle()
