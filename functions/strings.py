"""
    Strings

    Sets strings that the bot uses 
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

START_REPLY = "Hey how may I help you today?"

GOOD_PATH_FLOW_START = "I'm doing good"
GOOD_PATH_FLOW_NEED_TO_TALK = "I seek some guidance"
GOOD_PATH_FLOW_WANT_TO_READ_THINGS = "Access resources"

BAD_PATH_FLOW_START = "talk to someone anonymously"
BAD_PATH_FLOW_FOLLOWUP = "what's concerning you today?"

PROBLEM_SPIRITUAL_CRISIS = "I just want to talk to someone"
PROBLEM_ADDICTION = "I want to ask some questions to know more"
PROBLEM_PSYCOLOGICAL = "I want to report a sexual assault case"
PROBLEM_PORN_ADDICTION = "I want contact info for other SCORA groups"
PROBLEM_RELATIONSHIP = "Feedback"
PROBLEM_OTHER = "Other"

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

ADMIN_SPIRITUAL_CRISIS = 1606843992
ADMIN_RELATIONSHIP = 1606843992
ADMIN_PSYCOLOGICAL = 1606843992
ADMIN_OTHER = 1606843992
ADMIN_ADDICTION = 1606843992
ADMIN_PORN_ADDICTION = 1606843992

STR_ADMIN_SPIRITUAL_CRISIS = ""
STR_ADMIN_RELATIONSHIP = ""
STR_ADMIN_PSYCOLOGICAL = ""
STR_ADMIN_OTHER = ""
STR_ADMIN_ADDICTION = ""
STR_ADMIN_PORN_ADDICTION = ""

ADMIN_NEED_TO_TALK = 1606843992
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
