# Simple telegram bot
[Original Docs](https://github.com/python-telegram-bot/python-telegram-bot/wiki/)
## Quick start
```python
import telegram_bot
import requests
import re

client = telegram_bot.client('token')

@client.command
def bop(update, context):
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = requests.get('https://random.dog/woof.json').json()['url']
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    update.message.reply_photo(photo=url)

client.start()

```
