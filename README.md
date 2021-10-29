# Simple telegram bot
[Original Docs](https://github.com/python-telegram-bot/python-telegram-bot/wiki/)
## Quick start
```python
import telegram_bot

token = 'TOKEN'
client = telegram_bot.client(token)
client.whitelist = [934172244]

@client.command
def ping(update, context):
    update.message.reply_text('Pong!')

@client.message
def handler(update, context):
    update.message.reply_text(update.message.text)

client.start()
```
