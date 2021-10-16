# Copyright (C) 2021 TeamOfShadow

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

from pyrogram import filters

from Shadow.function.pluginhelpers import admins_only
from Shadow.services.pyrogram import pbot


@pbot.on_message(
    filters.command("invitelink") & ~filters.edited & ~filters.bot & ~filters.private
)
@admins_only
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "Add me as admin of yor group first",
        )
        return
    await message.reply_text(f"Invite link generated successfully \n\n {invitelink}")
    

__HELP__ = """
Classic filters are just like marie's filter system. If you still like that kind of filter system

**Admin Only**
 - `/cfilter <word> <message>`: Every time someone says "word", the bot will reply with "message"
You can also include buttons in filters, example send `/savefilter google` in reply to `Click Here To Open Google | [Button.url('Google', 'google.com')]`
 - `/stopcfilter <word>`: Stop that filter.
 - `/stopallcfilters`: Delete all filters in the current chat.

**Admin + Non-Admin**
 - `/cfilters`: List all active filters in the chat
 
 **Please note classic filters can be unstable. We recommend you to use `/addfilter`**
"""


@pbot.on_message(filters.command("cfilterhelp") & ~filters.private & ~filters.edited)
@admins_only
async def filtersghelp(client, message):
    await client.send_message(message.chat.id, text=__HELP__, parse_mode="markdown")
