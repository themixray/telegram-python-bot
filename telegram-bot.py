from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

class client:
    def __init__(self, token):
        self.updater = Updater(token)
    def command(self, func):
        self.updater.dispatcher.add_handler(
            CommandHandler(func.__name__,func))
    def start(self):
        self.updater.start_polling()
        self.updater.idle()
client = client('1913346661:AAHFmsw0qT-wES3ENqyLWo_xhzymG7jhXTo')

@client.command
def bop(update, context):
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = requests.get('https://random.dog/woof.json').json()['url']
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    update.message.reply_text(text='123', photo=url)

client.start()
