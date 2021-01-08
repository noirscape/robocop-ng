import hashlib
import datetime
from secure import TOKEN

# Basic bot config, insert your token here, update description if you want
prefixes = [".", "!"]
token = TOKEN
bot_description = "Detrius. The moderation bot of the RationalWiki support chat."
server_id = 797031608933810197

# If you forked robocop-ng, put your repo here
source_url = "https://github.com/noirscape/robocop-ng"
rules_url = 797031751666368542

# The bot description to be used in .detrius embed
embed_desc = (
    "Detrius is developd by [noirscape](https://github.com/noirscape). "
    "Detrius is based on [Robocop-NG](https://github.com/reswitched/robocop-ng). "
    "Robocop-NG is developed by [Ave](https://github.com/aveao)"
    " and [tomGER](https://github.com/tumGER), and is a rewrite "
    "of Robocop.\nRobocop is based on Kurisu by 916253 and ihaveamac."
)


# The cogs the bot will load on startup.
initial_cogs = [
    "cogs.common",
    "cogs.admin",
    "cogs.mod",
    "cogs.mod_note",
    "cogs.mod_reacts",
    "cogs.mod_userlog",
    "cogs.mod_timed",
    "cogs.mod_watch",
    "cogs.basic",
    "cogs.logs",
    "cogs.lockdown",
    "cogs.remind",
    "cogs.robocronp",
    "cogs.sar"
]

# The following cogs are also available but aren't loaded by default:
# cogs.imagemanip - Adds a meme command called .cox.
# Requires Pillow to be installed with pip.
# cogs.lists - Allows managing list channels (rules, FAQ) easily through the bot
# PR'd in at: https://github.com/reswitched/robocop-ng/pull/65
# cogs.pin - Lets users pin important messages
# and sends pins above limit to a github gist


# Minimum account age required to join the guild
# If user's account creation is shorter than the time delta given here
# then user will be kicked and informed
min_age = datetime.datetime.fromtimestamp(0)

# The bot will only work in these guilds
guild_whitelist = [server_id]  # ReSwitched discord

# Named roles to be used with .approve and .revoke
# Example: .approve User hacker
named_roles = {
    "basicperms": 797032376055758888
}

# The bot manager and staff roles
# Bot manager can run eval, exit and other destructive commands
# Staff can run administrative commands
bot_manager_role_id = 126747960972279808  # Bot management role in ReSwitched
staff_role_ids = [
    797032320409534465, # SuperOP
    797040379266465802, # OP
    797032547024240670, # Tech
    797032284174942219, # Board Member
    797032237794459658, # Moderator
]

# Various log channels used to log bot and guild's activity
# You can use same channel for multiple log types
# Spylog channel logs suspicious messages or messages by members under watch
# Invites created with .invite will direct to the welcome channel.
log_channel = 797195774462656532  # server-logs
botlog_channel = 797195899176091648  # bot-logs channel
modlog_channel = 797195974325698600  # mod-logs channel
spylog_channel = 548304839294189579  # spam-alert channel
welcome_channel = 797031751666368542  # rules channel

# These channel entries are used to determine which roles will be given
# access when we unmute on them
general_channels = [
    797031608933810200, # general-wiki-talk
    797045965777403915, # wigo
    797046007064952852, # off-topic
    797046032339959838, # wiki-projects
    797046087873462292, # server-matters
    797050407524237352, # votes
]  # Channels everyone can access

# Controls which roles are blocked during lockdown
lockdown_configs = {
    # Used as a default value for channels without a config
    "default": {"channels": general_channels, "roles": [
        server_id # @everyone
    ]},
}

# Mute role is applied to users when they're muted
# As we no longer have mute role on ReSwitched, I set it to 0 here
mute_role = 0  # Mute role in ReSwitched

# Channels that will be cleaned every minute/hour.
# This feature isn't very good rn.
# See https://github.com/reswitched/robocop-ng/issues/23
minutely_clean_channels = []
hourly_clean_channels = []

# Edited and deletes messages in these channels will be logged
spy_channels = general_channels

# All lower case, no spaces, nothing non-alphanumeric
suspect_words = [
]

# List of words that will be ignored if they match one of the
# suspect_words (This is used to remove false positives)
suspect_ignored_words = [
    "excit",
    "s/x",
    "3dsx",
    "psx",
    "txt",
    "s(x",
    "txd",
    "t=x",
    "osx",
    "rtx",
    "shift-x",
    "users/x",
    "tx1",
    "tx2",
    "tcptx",
    "udptx",
    "ctx",
    "jit's",
]

# == Only if you want to use cogs.pin ==
# Used for the pinboard. Leave empty if you don't wish for a gist pinboard.
github_oauth_token = ""

# Channels and roles where users can pin messages
allowed_pin_channels = []
allowed_pin_roles = []

# == Only if you want to use cogs.sar ==
self_assignable_roles = {
    "he": 797032987601534987,
    "she": 797033034506567730,
    "they": 797033050395115590
}
