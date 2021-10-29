import telegram
import telegram.ext
import requests
import re

class client:
    def __init__(self, token):
        self.updater = telegram.ext.Updater(token)
        self.whitelist = None
    def command(self, func):
        def fwwh(func, whitelist, update, context):
            if whitelist == None or update.message.from_user.id in whitelist:
                func(update, context)
        func = lambda update,context:fwwh(func,self.whitelist,update,context)
        self.updater.dispatcher.add_handler(
            telegram.ext.CommandHandler(func.__name__,func))
    def message(self, func):
        def fwwh(func, whitelist, update, context):
            if whitelist == None or update.message.from_user.id in whitelist:
                func(update, context)
        func = lambda update,context:fwwh(func,self.whitelist,update,context)
        self.updater.dispatcher.add_handler(
            telegram.ext.MessageHandler(telegram.ext.Filters.text,func))
    def start(self):
        self.updater.start_polling()
        self.updater.idle()
