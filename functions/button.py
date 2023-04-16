from functions.strings import *

from telegram import Update
from telegram.ext import CallbackContext


def button_good_path_flow_start(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ""
    context.user_data['cta'] = ""
    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello, How are you doing today?", reply_markup=GOOD_PATH_KEYBOARD)
    query.answer()


def button_good_path_flow_need_to_talk(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    context.user_data['ct'] = ADMIN_NEED_TO_TALK
    context.user_data['cta'] = STR_ADMIN_NEED_TO_TALK

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the{STR_ADMIN_NEED_TO_TALK} admin")
    query.answer()


def button_good_path_flow_want_to_read_things(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Go to {CHANNEL_WANT_TO_READ_THINGS}")
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
        chat_id=update.effective_chat.id, text=f"Connected to the{STR_ADMIN_SPIRITUAL_CRISIS} admin")
    query.answer()


def button_problem_relationship(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_RELATIONSHIP
    context.user_data['cta'] = STR_ADMIN_RELATIONSHIP

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the{STR_ADMIN_RELATIONSHIP} admin")
    query.answer()


def button_problem_psycological(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_PSYCOLOGICAL
    context.user_data['cta'] = STR_ADMIN_PSYCOLOGICAL

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the{STR_ADMIN_PSYCOLOGICAL} admin")
    query.answer()


def button_problem_other(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_OTHER
    context.user_data['cta'] = STR_ADMIN_OTHER

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the{STR_ADMIN_OTHER} admin")
    query.answer()


def button_problem_addiction(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_ADDICTION
    context.user_data['cta'] = STR_ADMIN_ADDICTION

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the{STR_ADMIN_ADDICTION} admin")
    query.answer()


def button_problem_porn_addiction(update: Update, context: CallbackContext) -> None:
    context.user_data['ct'] = ADMIN_PORN_ADDICTION
    context.user_data['cta'] = STR_ADMIN_PORN_ADDICTION

    query = update.callback_query
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Connected to the{STR_ADMIN_PORN_ADDICTION} admin")
    query.answer()
