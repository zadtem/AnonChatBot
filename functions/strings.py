"""
    Strings

    Sets strings that the bot uses 
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

START_REPLY = "ሰላም በጌታ የተወደድክ/ሽ\nእንዴት ነህ/ሽ?"

GOOD_PATH_FLOW_START = "ደህና ነኝ እግዚአብሔር ይመስገን"
GOOD_PATH_FLOW_NEED_TO_TALK = "የሚያወራኝ ሰው እፈልጋለሁ"
GOOD_PATH_FLOW_WANT_TO_READ_THINGS = "ፅሁፎችን ለማንበብ"

BAD_PATH_FLOW_START = "ደህና አይደለሁም"
BAD_PATH_FLOW_FOLLOWUP = "በምን አይነት ችግር ዉስጥ ነኝ ብለህ ታስባለህ?"

PROBLEM_SPIRITUAL_CRISIS = "Spiritual Crisis"
PROBLEM_ADDICTION = "Addiction"
PROBLEM_PSYCOLOGICAL = "Psycological issues"
PROBLEM_PORN_ADDICTION = "Porn Addiction"
PROBLEM_RELATIONSHIP = "Relationship issues"
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

ADMIN_BOT = 352475318

ADMIN_SPIRITUAL_CRISIS = 5645705630
ADMIN_RELATIONSHIP = 5845178511
ADMIN_PSYCOLOGICAL = 5821376602
ADMIN_OTHER = 5714443263
ADMIN_ADDICTION = 5749100370
ADMIN_PORN_ADDICTION = 5540027894

STR_ADMIN_SPIRITUAL_CRISIS = "Spiritual Crisis"
STR_ADMIN_RELATIONSHIP = "Relationship"
STR_ADMIN_PSYCOLOGICAL = "Psycological"
STR_ADMIN_OTHER = "Other"
STR_ADMIN_ADDICTION = "Addiction"
STR_ADMIN_PORN_ADDICTION = "Porn Addiction"

ADMIN_NEED_TO_TALK = 5714443263
STR_ADMIN_NEED_TO_TALK = "Need to talk"

CHANNEL_WANT_TO_READ_THINGS = "@yene_counselling"

ADMINS = {
    ADMIN_SPIRITUAL_CRISIS:  STR_ADMIN_SPIRITUAL_CRISIS,
    ADMIN_RELATIONSHIP: STR_ADMIN_RELATIONSHIP,
    ADMIN_PSYCOLOGICAL: STR_ADMIN_PSYCOLOGICAL,
    ADMIN_OTHER: STR_ADMIN_OTHER,
    ADMIN_ADDICTION: STR_ADMIN_ADDICTION,
    ADMIN_PORN_ADDICTION: STR_ADMIN_PORN_ADDICTION,
    ADMIN_NEED_TO_TALK: STR_ADMIN_NEED_TO_TALK
}
