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
