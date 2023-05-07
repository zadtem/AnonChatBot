from functions.strings import *

from telegram import Update
from telegram.ext import CallbackContext


def button_good_path_flow_start(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ""
    context.user_data['cta'] = ""
    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello, How may I help you today?", reply_markup=GOOD_PATH_KEYBOARD)
    query.answer()


def button_good_path_flow_need_to_talk(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"<a href='https://t.me/Scora_Ecusta_Resources/13'>❤️About SCORA</a>\n<a href='https://t.me/Scora_Ecusta_Resources/14'>❤️SCORA IFMSA OBJECTIVES</a>\n<a href='https://t.me/Scora_Ecusta_Resources/15'>SCORA ETHIOPIA OBJECTIVES</a>\n<a href='https://t.me/Scora_Ecusta_Resources/16'>❤️ABOUT SCORA-ECUSTA</a>\n<a href='https://t.me/Scora_Ecusta_Resources/18'>❤️ABOUT SRHR</a>\n<a href='https://t.me/Scora_Ecusta_Resources/19'>❤️What's sexual health</a>\n<a href='https://t.me/Scora_Ecusta_Resources/20'>❤️What's sexual right</a>\n<a href='https://t.me/Scora_Ecusta_Resources/21'>❤️Information on HIV/AIDS</a>\n<a href='https://t.me/Scora_Ecusta_Resources/22'>❤️Facts about STI</a>\n<a href='https://t.me/Scora_Ecusta_Resources/23'>❤️STI transmission and control</a>\n")
    query.answer()


def button_good_path_flow_want_to_read_things(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Go to {CHANNEL_WANT_TO_READ_THINGS} to get access to more resources")
    query.answer()


def button_bad_path_flow_start(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=BAD_PATH_FLOW_FOLLOWUP, reply_markup=BAD_PATH_KEYBOARD)
    query.answer()


def button_problem_spiritual_crisis(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_SPIRITUAL_CRISIS
    context.user_data['cta'] = STR_ADMIN_SPIRITUAL_CRISIS

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the {STR_ADMIN_SPIRITUAL_CRISIS} admin")
    query.answer()


def button_problem_relationship(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_RELATIONSHIP
    context.user_data['cta'] = STR_ADMIN_RELATIONSHIP

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the {STR_ADMIN_RELATIONSHIP} admin")
    query.answer()


def button_problem_psycological(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_PSYCOLOGICAL
    context.user_data['cta'] = STR_ADMIN_PSYCOLOGICAL

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"We're here for you!❤️ How may we help you?\n1 in 3 (35%) of women have experienced physical and/or sexual violence.\n55-99 % of women of survivors of violence don not disclose or seek any type of services.\nWe would like to take part and make it easier for these women or men to reach out.\nSexual assault refers to unwanted sexual activity (e.g. touching, kissing someone without consent, rape).  Sexual harassment can include comments, behaviour, and unwanted sexual contact.")
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the {STR_ADMIN_PSYCOLOGICAL} admin ")
    query.answer()


def button_problem_other(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_OTHER
    context.user_data['cta'] = STR_ADMIN_OTHER

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the {STR_ADMIN_OTHER} admin")
    query.answer()


def button_problem_addiction(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_ADDICTION
    context.user_data['cta'] = STR_ADMIN_ADDICTION

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the {STR_ADMIN_ADDICTION} admin")
    query.answer()


def button_problem_porn_addiction(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_PORN_ADDICTION
    context.user_data['cta'] = STR_ADMIN_PORN_ADDICTION

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the {STR_ADMIN_PORN_ADDICTION}")
    query.answer()
