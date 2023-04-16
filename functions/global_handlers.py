from telegram import Update
from telegram.constants import PARSEMODE_HTML
from telegram.ext import CallbackContext
from pprint import pprint
from functions.strings import *


def global_text_handler(update: Update, context: CallbackContext) -> None:
    if (update.effective_chat.id in ADMINS):
        print("Councellor Reply")
        to_chat = int(update.message.reply_to_message.text.split('Said :')[0])
        context.bot.send_message(
            chat_id=to_chat,
            text=update.message.text +
            f"<i>\n\n from: <b>{ADMINS[update.effective_chat.id]} Admin</b>\n"
            + "</i>",
            parse_mode=PARSEMODE_HTML)
    else:
        print("Councellor Request")
        chat_id = context.user_data.get('ct')
        if chat_id:
            context.bot.send_message(
                chat_id=chat_id,
                text=f"<i><b>{update.effective_chat.id}</b></i> Said : \n\n" +
                update.message.text + "\n\n<i>Reply to this message to respond.</i>",
                parse_mode=PARSEMODE_HTML)
