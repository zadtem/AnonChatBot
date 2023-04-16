"""Start message"""

import telegram
from telegram.constants import PARSEMODE_HTML
from functions.strings import START_REPLY, START_KEYBOARD
from decorators import typing


@typing
def start(update, context):
    """
        Send a message when the command /start is issued.
    """
    # Send welcome message
    print(update.effective_chat.id)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            START_REPLY
        ),
        parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=True, reply_markup=START_KEYBOARD
    )
@typing
def ct(update, context):
    """
        Send a message when the command /ct is issued.
    """
    # Send connected to chat 

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=context.user_data
    )
    
@typing
def id(update, context):
    """
        Send a message when the command /id is issued.
    """
    # Send selfs id

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Your id is : <code>{update.effective_chat.id}</code>" ,
        parse_mode = PARSEMODE_HTML
    )
