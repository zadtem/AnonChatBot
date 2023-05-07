"""
    Strings

    Sets strings that the bot uses 
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

START_REPLY = "Hello Angel❤️ \n How may I help you today? \n I want\n1. Information on SRHR\n2. To talk to someone anonymously"

GOOD_PATH_FLOW_START = "1"
GOOD_PATH_FLOW_NEED_TO_TALK = "Access resources"
GOOD_PATH_FLOW_WANT_TO_READ_THINGS = "More"

BAD_PATH_FLOW_START = "2"
BAD_PATH_FLOW_FOLLOWUP = "What's concerning you today?\n \nA group of volunteers will reply to your message as soon as possible.\n \nI want to...\na. talk to someone  \nb. ask some questions \nc. report sexual assault\nd. talk with school counselor\ne. Feedback \nf. Other"

PROBLEM_SPIRITUAL_CRISIS = "A"
PROBLEM_ADDICTION = "B"
PROBLEM_PSYCOLOGICAL = "C"
PROBLEM_PORN_ADDICTION = "D"
PROBLEM_RELATIONSHIP = "E"
PROBLEM_OTHER = "F"

# KEYBOARDS

START_KEYBOARD = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(GOOD_PATH_FLOW_START,
                             callback_data=GOOD_PATH_FLOW_START),
        InlineKeyboardButton(BAD_PATH_FLOW_START,
                             callback_data=BAD_PATH_FLOW_START),
    ]
])

GOOD_PATH_KEYBOARD = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(GOOD_PATH_FLOW_NEED_TO_TALK,
                             callback_data=GOOD_PATH_FLOW_NEED_TO_TALK),
        InlineKeyboardButton(GOOD_PATH_FLOW_WANT_TO_READ_THINGS,
                             callback_data=GOOD_PATH_FLOW_WANT_TO_READ_THINGS),
    ]
])

BAD_PATH_KEYBOARD = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(PROBLEM_SPIRITUAL_CRISIS,
                             callback_data=PROBLEM_SPIRITUAL_CRISIS),
        InlineKeyboardButton(PROBLEM_ADDICTION,
                             callback_data=PROBLEM_ADDICTION),
    ],
    [
        InlineKeyboardButton(PROBLEM_PSYCOLOGICAL,
                             callback_data=PROBLEM_PSYCOLOGICAL),
        InlineKeyboardButton(PROBLEM_PORN_ADDICTION,
                             callback_data=PROBLEM_PORN_ADDICTION),
    ],
    [
        InlineKeyboardButton(PROBLEM_RELATIONSHIP,
                             callback_data=PROBLEM_RELATIONSHIP),
        InlineKeyboardButton(PROBLEM_OTHER,
                             callback_data=PROBLEM_OTHER),
    ]
])

# TELEGRAM IDS OF RESPONSIBLE PEEPS

ADMIN_BOT = 1606843992

ADMIN_SPIRITUAL_CRISIS = 1813231809  # a. talk to someone, @ruhamahn
ADMIN_RELATIONSHIP = 412672486      #e. feedback, @ba_zinga
ADMIN_PSYCOLOGICAL = 282048723      #c. sexual assault report, @beth6502
ADMIN_OTHER = 1813231809             #f. other, @ruhamahn
ADMIN_ADDICTION = 879236175         #b. ask some questions to know more, @mek1it
ADMIN_PORN_ADDICTION = 1760843271   #d. school counselor, @kerenino

STR_ADMIN_SPIRITUAL_CRISIS = "talk to someone"
STR_ADMIN_RELATIONSHIP = "feedback"
STR_ADMIN_PSYCOLOGICAL = "sexual assault report"
STR_ADMIN_OTHER = "others"
STR_ADMIN_ADDICTION = "questions"
STR_ADMIN_PORN_ADDICTION = "school counselor"

ADMIN_NEED_TO_TALK = 1813231809  #need some guidance, @ruhamahn
STR_ADMIN_NEED_TO_TALK = ""

CHANNEL_WANT_TO_READ_THINGS = "@SCORA_ECUSTA"

ADMINS = {
    ADMIN_SPIRITUAL_CRISIS:  STR_ADMIN_SPIRITUAL_CRISIS,
    ADMIN_RELATIONSHIP: STR_ADMIN_RELATIONSHIP,
    ADMIN_PSYCOLOGICAL: STR_ADMIN_PSYCOLOGICAL,
    ADMIN_OTHER: STR_ADMIN_OTHER,
    ADMIN_ADDICTION: STR_ADMIN_ADDICTION,
    ADMIN_PORN_ADDICTION: STR_ADMIN_PORN_ADDICTION,
    ADMIN_NEED_TO_TALK: STR_ADMIN_NEED_TO_TALK
}
