# pylint: disable=fixme

"""
    Main execution script.
"""

# Standard imports
import os
import logging

from logging import handlers

# 3rd party imports
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters
# local imports

from functions.start import *
from functions.button import *
from functions.global_handlers import *
from functions.constants import *
from functions.strings import *


# Logging configuration

# Make folder called logs if not exists
if not os.path.exists('logs'):
    os.mkdir('logs')
# Timed log handler that rotates the
# log file by each midnight
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
    handlers=[
        handlers.TimedRotatingFileHandler(
            './logs/debug.log', encoding='utf-8', when='midnight'),
        logging.StreamHandler()
    ]
)


def main():
    "Main Execution"
    # start handler
    dpr.add_handler(CommandHandler('start', start))
    dpr.add_handler(CommandHandler('ct', ct))
    dpr.add_handler(CommandHandler('id', id))
    dpr.add_handler(CallbackQueryHandler(
        button_good_path_flow_start, pattern=GOOD_PATH_FLOW_START))
    dpr.add_handler(CallbackQueryHandler(
        button_good_path_flow_need_to_talk, pattern=GOOD_PATH_FLOW_NEED_TO_TALK))
    dpr.add_handler(CallbackQueryHandler(
        button_good_path_flow_want_to_read_things, pattern=GOOD_PATH_FLOW_WANT_TO_READ_THINGS))
    dpr.add_handler(CallbackQueryHandler(
        button_bad_path_flow_start, pattern=BAD_PATH_FLOW_START))

    dpr.add_handler(CallbackQueryHandler(
        button_problem_spiritual_crisis, pattern=PROBLEM_SPIRITUAL_CRISIS))
    dpr.add_handler(CallbackQueryHandler(
        button_problem_relationship, pattern=PROBLEM_RELATIONSHIP))
    dpr.add_handler(CallbackQueryHandler(
        button_problem_psycological, pattern=PROBLEM_PSYCOLOGICAL))
    dpr.add_handler(CallbackQueryHandler(
        button_problem_other, pattern=PROBLEM_OTHER))
    dpr.add_handler(CallbackQueryHandler(
        button_problem_addiction, pattern=PROBLEM_ADDICTION))
    dpr.add_handler(CallbackQueryHandler(
        button_problem_porn_addiction, pattern=PROBLEM_PORN_ADDICTION))

    dpr.add_handler(MessageHandler(Filters.text, global_text_handler))

    updater.start_polling()
    logging.info(f'🟩  Bot is LIVE 🟩')
    updater.idle()


if __name__ == '__main__':
    main()
