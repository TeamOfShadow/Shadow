#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

try:
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient
except BaseException:
    print("Telethon Not Found. Installing Now.")
    import os

    os.system("pip3 install telethon")
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient
ok = """
______ _____ ____ ___ __ _ __ ___ ____ _____ ______
|                                                 |
| Copyright (C) 2021 @TeamOfShadow                |
| Copyright (C) 2021 @Mr_Shadow_Robot             |
| Copyright (C) 2020-2021 @DeshadeethThisarana    |
|_____ _____ ____ ___ __ _ __ ___ ____ _____ _____|

Enter your details here.
After filling it check your saved messages
"""
print(ok)

APP_ID = int(input("Enter APP ID here: \n"))
API_HASH = input("Enter API HASH here: \n")

text = "THIS IS YOUR STRING SESSION"
text += "Join @ShadowSupport_Official For More Support."

client = TelegramClient(StringSession(), APP_ID, API_HASH)
with client:
    session_str = client.session.save()
    client.send_message(f"`{session_str}`")
    client.send_message(text)
    print("⬆ Please Check Your Telegram Saved Message For Your String.")
