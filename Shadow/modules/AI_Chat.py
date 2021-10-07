# Copyright (C) 2021 Red-Aura & Shadow & HamkerCat

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


import re
import emoji

IBM_WATSON_CRED_URL = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/bd6b59ba-3134-4dd4-aff2-49a79641ea15"
IBM_WATSON_CRED_PASSWORD = "UQ1MtTzZhEsMGK094klnfa-7y_4MCpJY1yhd52MXOo3Y"
url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

import aiohttp
from googletrans import Translator as google_translator
from pyrogram import filters
import requests
from DaisyX import BOT_ID
from Shadow.db.mongo_helpers.aichat import add_chat, get_session, remove_chat
from Shadow.function.inlinehelper import arq
from Shadow.function.pluginhelpers import admins_only, edit_or_reply
from Shadow.services.pyrogram import pbot as shadow
from Shadow.db.mongo_helpers.kuki import kuki_off, kuki_on, is_kuki_on
translator = google_translator()
from pyrogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup, 
  Message, 
  User, 
)

async def lunaQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


async def fetch(url):
    try:
        async with aiohttp.Timeout(10.0):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    try:
                        data = await resp.json()
                    except:
                        data = await resp.text()
            return data
    except:
        print("AI response Timeout")
        return


shadow_chats = []
en_chats = []

# AI Chat (C) 2020-2021 by @DeshadeethThisarana

"""
@daisyx.on_message(
    filters.voice & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded,
    group=2,
)
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        message.continue_propagation()
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    previous_message = message
    required_file_name = message.download()
    if IBM_WATSON_CRED_URL is None or IBM_WATSON_CRED_PASSWORD is None:
        await message.reply(
            "You need to set the required ENV variables for this module. \nModule stopping"
        )
    else:
        headers = {
            "Content-Type": previous_message.voice.mime_type,
        }
        data = open(required_file_name, "rb").read()
        response = requests.post(
            IBM_WATSON_CRED_URL + "/v1/recognize",
            headers=headers,
            data=data,
            auth=("apikey", IBM_WATSON_CRED_PASSWORD),
        )
        r = response.json()
        print(r)
        await client.send_message(message, r)
"""

@shadow.on_callback_query(filters.regex(pattern=r"^kuki$"))
async def _heldp(b, cb):
    chat_id = cb.message.chat.id
    Escobar = remove_chat(int(chat_id))
    if not Escobar:
        pass
    await kuki_on(chat_id)
    await cb.message.edit(
        f"Enabled Kuki AI chatbot on this group\n\n`Kuki is smart, powerful, cute and intelligent. Reply to any of Shadow's messages to enjoy chatbot service`"
    ) 
@shadow.on_callback_query(filters.regex(pattern=r"^acobot$"))
async def acoo(b, cb):
    chat_id = cb.message.chat.id
    await kuki_off(chat_id)
    lol = add_chat(int(chat_id))
    if not lol:
        pass
    await cb.message.edit(
        f"Enabled Aco chatbot on this group. \n\n`Aco based chatbot in Shadow is simple but powerful chatbot powered by acobot.ai. Support large number of languages and clever on problem solving. Reply to any of Shadow's messages to enjoy chatbot service`"
    ) 
    
@shadow.on_message(
    filters.command("chatbot") & ~filters.edited & ~filters.bot & ~filters.private
)
@admins_only
async def hmm(_, message):
    global daisy_chats
    button = [[InlineKeyboardButton(text = 'Acobot', callback_data = "acobot"),InlineKeyboardButton(text = 'Kuki', callback_data = "kuki")]]
    if len(message.command) != 2:
        if await is_kuki_on(message.chat.id):
            actv="Kuki"
        elif get_session(int(message.chat.id)):
            actv="Acobot"
        else:
            actv="No"
            
        await message.reply_text(
            f"{actv} AI Chatbot currently active for users in this group\nClick any button to change chatbot service",reply_markup = InlineKeyboardMarkup(button)
        )
        return
        
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    if status == "ON" or status == "on" or status == "On":
        
        lel = await edit_or_reply(message, "`Processing...`")
        if chat_id in en_chats:
            en_chats.remove(chat_id)
        if await is_kuki_on(message.chat.id):
            return await lel.edit("Kuki Ai chatbot already active on this group")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("Shadow AI Already Activated In This Chat\nClick any button to change chatbot service",reply_markup = InlineKeyboardMarkup(button))
            return
        await lel.edit(
            f"Shadow's Acobot based AI Successfully Added For Users In this chat\nClick any button to change chatbot service",reply_markup = InlineKeyboardMarkup(button)
        )

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if chat_id in en_chats:
            en_chats.remove(chat_id)        
        if not Escobar and  not await is_kuki_on(message.chat.id):
            await lel.edit("Shadow AI Was Not Activated In This Chat")
            return
        await kuki_off(chat_id)
        await lel.edit(
            f"Shadow AI Successfully Deactivated For Users In The Chat {message.chat.id}"
        )

    elif status == "EN" or status == "en" or status == "english":
        if not chat_id in en_chats:
            en_chats.append(chat_id)
            await message.reply_text("English AI chat Enabled!")
            return
        await message.reply_text("AI Chat Is Already Disabled.")
        message.continue_propagation()
    elif status == "kuki" or status == "KUKI":
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            pass
        await kuki_on(chat_id)
        await message.reply_text(
            f"Enabled Kuki AI chatbot on this group"
        )
    elif status == "acobot" or status == "aco":
        await kuki_off(chat_id)
        lol = add_chat(int(message.chat.id))
        if not lol:
            pass
        await message.reply_text(
            f"Enabled Aco chatbot on this group. Visit Acobot.ai for more info"
        )     
    else:
        if await is_kuki_on(message.chat.id):
            actv="Kuki"
        if get_session(int(message.chat.id)):
            actv="Acobot"
        else:
            actv="No"
            
        await message.reply_text(
            f"{actv} AI Chatbot currently active for users in this group\nClick any button to change chatbot service",reply_markup = InlineKeyboardMarkup(button)
        )


@shadow.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        if not await is_kuki_on(message.chat.id):
            return
        #print("kuki action")
        if not message.reply_to_message:
            return
        try:
            senderr = message.reply_to_message.from_user.id
        except:
            return
        if senderr != BOT_ID:
            return
        msg = message.text
        chat_id = message.chat.id
        if msg.startswith("/") or msg.startswith("@"):
            message.continue_propagation()
        try:
            Kuki = requests.get(f"https://kuki-api.tk/api/ShadowRobot/DeshadeethThisarana/message={msg}").json()
        except:
            return
        moezilla = f"{Kuki['reply']}"
        pro = moezilla
        try:
            await shadow.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return
        except:
            return
        return
    if not message.reply_to_message:
        return
    try:
        senderr = message.reply_to_message.from_user.id
    except:
        return
    if senderr != BOT_ID:
        return
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        test = msg
        test = test.replace("shadow", "Aco")
        test = test.replace("Shadow", "Aco")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "Shadow")
        response = response.replace("aco", "Shadow")
        response = response.replace("Luna", "Shadow")
        response = response.replace("luna", "Shadow")
        response = response.replace("Aco", "Shadow")
        response = response.replace("I made myself", "Shadow is developed with ❤️ by @TeamOfShadow")
        pro = response
        try:
            await shadow.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return

    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            # print (rm)
        try:
            lan = translator.detect(rm)
            lan = lan.lang
        except:
            return
        test = rm
        if not "en" in lan and not lan == "":
            try:
                test = translator.translate(test, dest="en")
                test = test.text
            except:
                return
        # test = emoji.demojize(test.strip())

        test = test.replace("shadow", "Aco")
        test = test.replace("Shadow", "Aco")
        try:
            response = await lunaQuery(
                test, message.from_user.id if message.from_user else 0
            )
        except:
            return message.continue_propagation()
        response = response.replace("Aco", "Shadow")
        response = response.replace("aco", "Shadow")
        response = response.replace("Luna", "Shadow")
        response = response.replace("luna", "Shadow")        
        pro = response
        if not "en" in lan and not lan == "":
            try:
                pro = translator.translate(pro, dest=lan)
                pro = pro.text
            except:
                return
        try:
            await daisyx.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return


@shadow.on_message(
    filters.text & filters.private & ~filters.edited & filters.reply & ~filters.bot
)
async def inuka(client, message):
    msg = message.text
    try:
      if msg.startswith("/") or msg.startswith("@"):
          message.continue_propagation()
    except:
      return 
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return

    # test = emoji.demojize(test.strip())

    # Kang with the credits >> @InukaASiTH
    
    test = test.replace("shadow", "Aco")
    test = test.replace("Shadow", "Aco")
    try:
        response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    except:
        return message.continue_propagation()
    response = response.replace("Aco", "Shadow")
    response = response.replace("aco", "Shadow")

    pro = response
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, dest=lan)
        pro = pro.text
    try:
        await daisyx.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


@daisyx.on_message(
    filters.regex("Shadow|shadow")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel
    & ~filters.edited
)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return

    # test = emoji.demojize(test.strip())

    test = test.replace("shadow", "Aco")
    test = test.replace("Shadow", "Aco")
    try:
        response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    except:
        return message.continue_propagation()
    response = response.replace("Aco", "Shadow")
    response = response.replace("aco", "Shadow")
    response = response.replace("Luna", "Shadow")
    response = response.replace("luna", "Shadow")
    pro = response
    if not "en" in lan and not lan == "":
        try:
            pro = translator.translate(pro, dest=lan)
            pro = pro.text
        except Exception:
            return
    try:
        await daisyx.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except:
        return



def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


__help__ = """
<b> Chatbot </b>
<i>SHADOW AI 3.0 IS THE ONLY AI SYSTEM WHICH CAN DETECT & REPLY UPTO 200 LANGUAGES<i>

 - `/chatbot`: Select the AI Chat mode (EXCLUSIVE)
 - `/chatbot EN`: Enables English only chatbot
 
 
<b> Assistant </b>
 - `/shadow [question]`: Ask question from Shadow
 - `/shadow [reply to voice note]`: Get voice reply
 """

__mod_name__ = "AI Assistant"
