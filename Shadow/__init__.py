# This file is part of Shadow (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
import logging
import spamwatch
from aiohttp import ClientSession

from Shadow.config import get_bool_key, get_int_key, get_list_key, get_str_key
from Shadow.utils.logger import log
from Shadow.versions import SHADOW_VERSION
from Shadow.services.pyrogram import pbot
log.info("----------------------")
log.info("|       Shadow       |")
log.info("----------------------")
log.info("Version: " + SHADOW_VERSION)

if get_bool_key("DEBUG_MODE") is True:
    SHADOW_VERSION += "-debug"
    log.setLevel(logging.DEBUG)
    log.warn(
        "! Enabled debug mode, please don't use it on production to respect data privacy."
    )

TOKEN = get_str_key("TOKEN", required=True)
OWNER_ID = get_int_key("OWNER_ID", required=True)
LOGS_CHANNEL_ID = get_int_key("LOGS_CHANNEL_ID", required=True)
APROOVE_DB = get_str_key("APROOVE_DB", required=True)
OPERATORS = list(get_list_key("OPERATORS"))
OPERATORS.append(OWNER_ID)
OPERATORS.append(918317361)

# SpamWatch
spamwatch_api = get_str_key("SW_API", required=True)
sw = spamwatch.Client(spamwatch_api)

SUPPORT_CHAT = get_str_key("SUPPORT_CHAT", required=True)
log.debug("Getting bot info...")


BOT_USERNAME = get_str_key("BOT_USERNAME", required=True)
BOT_ID = get_str_key("BOT_ID", required=True)
POSTGRESS_URL = get_str_key("DATABASE_URL", required=True)
TEMP_DOWNLOAD_DIRECTORY = "./"

app = pbot

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()

# Sudo Users
# SUDO_USERS = get_str_key("SUDO_USERS", required=True)

# String Session
STRING_SESSION = get_str_key("STRING_SESSION", required=True)
