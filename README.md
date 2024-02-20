[![pypi](https://img.shields.io/badge/pypi-tglib-blue)](https://pypi.org/project/tglib/) [![tele](https://img.shields.io/badge/telegram-@unixtux-blue)](https://t.me/geko1)

#

<h3 align="center">Build your telegram bot client</h3>

<h3 align="center">Supported Bot Api version <a href="https://core.telegram.org/bots/api#february-16-2024">7.1</a></h3>

#

* #### Requirements
  * Python >= 3.8
  * [aiohttp](https://github.com/aio-libs/aiohttp)
  * Optional [ujson](https://github.com/ultrajson/ultrajson) & [certifi](https://github.com/certifi/python-certifi)

* #### Installation
```powershell
python -m pip install tglib
```

* #### Update the module
```powershell
python -m pip install -U tglib
```

#

* #### 18 managers for different [updates](https://core.telegram.org/bots/api#update)
  * message_manager
  * edited_message_manager
  * channel_post_manager
  * edited_channel_post_manager
  * message_reaction_manager
  * message_reaction_count_manager
  * inline_query_manager
  * chosen_inline_result_manager
  * callback_query_manager
  * shipping_query_manager
  * pre_checkout_query_manager
  * poll_manager
  * poll_answer_manager
  * my_chat_member_manager
  * chat_member_manager
  * chat_join_request_manager
  * chat_boost_manager
  * removed_chat_boost_manager

#

* #### Available methods

All the **methods** are the same described in the **[offical documentation](https://core.telegram.org/bots/api#available-methods)**, changed from camelCase to snake_case. They are all **asynchronous**, so you must use them in **await** expression.

#

* #### Available Types

All the **types** are the same described in the **[offical documentation](https://core.telegram.org/bots/api#available-types)**.

> Attribute "**from**" of the types, has been changed to "**from_user**" because in python it causes conflict.

> If the attribute "**text**" of the Message is empty, it's **str()** instead of **None**, so you can use for example **text.startswith()** without getting errors.

> All other optional attributes of the objects are **None** if they are not in the **JSON** received as response.

#

* #### Reply Markups
**InlineKeyboardMarkup** and **ReplyKeyboardMarkup** have the method "**add**", so you can create new buttons after the object has been initialized.

```python
markup = ReplyKeyboardMarkup()
markup.add(KeyboardButton('x'), KeyboardButton('y'))

# All the buttons added with this method will be in
# the same row, you can change the row width after the
# object initialization using the property setter 'row_width'.

markup.row_width = 4

# The keyboard will be rearranged with 4 buttons each row.
```

#

* #### Notes

> Webhook has not been implemented yet.

#

* #### Prerequisites
You require a good **Python knowledge**, some skills with the **asyncio module** and a telegram bot API token, you can get it via **[@BotFather](https://t.me/botfather)**.

#

* #### Usage
```python
from tglib import (
    Client,
    NextManager,
    TelegramError
)
# Import all the types.
from tglib.types import *

# Create a bot instance.
bot = Client('<your_token>')

# Add some rules for incoming updates. Managers
# check rules in the same order they were added.

@bot.manage_message(lambda message: message.text == '/start')
async def start_message(message: Message):
    user = message.from_user.first_name
    try:
        await bot.send_message(message.chat.id, f'welcome {user}')
    except (TimeoutError, TelegramError):
        return
        # Two errors can be raised in requests:
        # - TimeoutError if a response
        #   is not returned in 5 minutes.
        # - TelegramError if a response is
        #   returned but got a bad status code.
    else:
        return NextManager()
        # Returning a NextManager instance, you will pass
        # the update to the following manager of same kind.

# You can also add rules with the
# method 'add_rule' of the managers.

def help_checker(message: Message):
    return message.text == '/help'

async def help_function(message: Message):
    await bot.send_message(message.chat.id, 'Do you need help?')

bot.message_manager.add_rule(help_checker, help_function)

# Calling the method 'long_polling',
# the bot starts receiving updates by
# the telegram server and process them.

import asyncio

if __name__ == '__main__':
    asyncio.run(bot.long_polling())
```
