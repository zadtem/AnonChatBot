"""
    Constants

    Configures key variables and 
    Parses .env to make tokens available to the app 
"""
from logging import warn
from os import getenv

import dotenv

from telegram import Bot
from telegram.ext import Updater, PicklePersistence

# .env parsing
TOKEN = dotenv.get_key('.env', 'TOKEN') or getenv('TOKEN')

if TOKEN:
    # Define bot
    bot = Bot(token=TOKEN)
    # Define updater and dispatcher
    pers = PicklePersistence(filename='persistence')
    updater = Updater(token=TOKEN, persistence=pers, use_context=True)
    dpr = updater.dispatcher
else:
    warn('No TOKEN found in .env file or environment variable')


# Admin list ( Telegram ids )
ADMINS = [1606843992]
