import telegram
import telegram.ext
import requests
import re

class client:
    def __init__(self, token):
        self.updater = telegram.ext.Updater(token)
        self.whitelist = None
    def command(self, name=None):
        def real_decorator(func):
            nonlocal name
            def fwwh2(update,context):
                if self.whitelist == None or update.message.from_user.id in self.whitelist:
                    func(update, context)
            if name == None:
                name = func.__name__
            self.updater.dispatcher.add_handler(
                telegram.ext.CommandHandler(name,fwwh2))
        return real_decorator
    def message(self, func):
        def fwwh2(update,context):
            if self.whitelist == None or update.message.from_user.id in self.whitelist:
                func(update, context)
        self.updater.dispatcher.add_handler(
            telegram.ext.MessageHandler(telegram.ext.Filters.text,fwwh2))
    def start(self):
        self.updater.start_polling()
        self.updater.idle()
