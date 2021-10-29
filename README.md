# Simple telegram bot
[Original Docs](https://github.com/python-telegram-bot/python-telegram-bot/wiki/)
## Quick start
```python
import telegram_bot

token = 'TOKEN'
client = telegram_bot.client(token)
client.whitelist = [YOURID]

@client.command()
def help(update, context):
    update.message.reply_text('Commands: /ping')

@client.command('ping')
def ping(update, context):
    update.message.reply_text('Pong!')

@client.message
def handler(update, context):
    update.message.reply_text(update.message.text)

client.start()
```
