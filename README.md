# Simple telegram bot
[Original Docs](https://github.com/python-telegram-bot/python-telegram-bot/wiki/)
## Quick start
```python
import telegram_bot

token = 'TOKEN'
myid = YOURID
client = telegram_bot.client(token)
client.whitelist = [myid]
client.bot.send_message(myid, 'Hello!')

@client.command()
def help(update, args):
    cmds = ''
    for i in client.commands:
        cmds += '\n/'
        cmds += i.command
        if i.description != '':
            cmds += ' - '
            cmds += i.description
    update.message.reply_text('Commands:'+cmds)

@client.command('ping', 'Just a description')
def ping(update, args):
    update.message.reply_text('Pong!')

@client.message
def handler(update):
    update.message.reply_text(update.message.text)

client.start()
```
