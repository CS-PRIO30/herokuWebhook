import os
from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


TOKEN = os.environ['TOKEN_TELEGRAM']
PORT = int(os.environ['PORT'])

updater = Updater(TOKEN)

updater.bot.set_webhook("https://webh00k.herokuapp.com/" + TOKEN)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.idle()
