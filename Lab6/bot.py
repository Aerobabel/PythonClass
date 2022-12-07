import telegram.ext


TOKEN = '5881397097:AAFHAqJwXoVqiK2K8guoPd5laSFir46EjT0'



def start(update, context):
    update.message.reply_text(''' /start - to start the bot
    /content- summary of bot use: The bot is used to predict the scores between two football teams with odds''')

def content(update, context):
    update.message.reply_text('leave')

def handle_message(update, context):
    update.message.reply_text(f"you said {update.message.text}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('content', content))

disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()