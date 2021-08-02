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

__mod_name__ = "Misc ⚙️"

__help__ = """
An "odds and ends" module for small, simple commands which don't really fit anywhere.

<b>Available commands:</b>

<b>BASIC</b>
- `/github (username)`: Returns info about a GitHub user or organization.
- `/wiki (keywords)`: Get wikipedia articles just using this bot.
- `/imdb`: Search for a movie
- `/cancel`: Disables current state. Can help in cases if @Mr_Shadow_Robot not responing on your message.
- `/id`: get the current group id. If used by replying to a message, gets that user's id.
- `/info`: get information about a user.
- `/paste`: Pase the text/file in nekobin
- `/gps`: Find a location

<b>BOOK DOWNLOAD</b>
- `/book <book name> <Usage>`: Gets Instant Download Link Of Given Book.

<b>FAKE INFO</b>
- `/fakegen`: Generates Fake Information
- `/picgen`: generate a fake pic

<b>ZIPPER</b>
- `/zip`: reply to a telegram file to compress it in .zip format
- `/unzip`: reply to a telegram file to decompress it from the .zip format

<b>WEATHER</b>
- `/weather [city]`: Gives weather forecast
- `/weatherimg [city]`: Gives weather image

<b>PHONE INFO</b>
- `/phone [phone no]`: Gathers number info

<b>CURRENCY</b>
 - `/cash` : currency converter
Example syntax: `/cash 1 USD LKR`

<b>NAME HISTORY</b>
- `/namehistory [REPLY]`: Get the Username and Name history of user.

<b>SEND</b>
- `/send [MESSAGE]`: Send given text by bot.

<b>CC CHECKER</b>
- `/au [cc]`: Stripe Auth given CC
- `/pp [cc]`: Paypal 1$ Guest Charge
- `/ss [cc]`: Speedy Stripe Auth
- `/ch [cc]`: Check If CC is Live
- `/bin [bin]`: Gather's Info About the bin
- `/gen [bin]`: Generates CC with given bin
- `/key [sk]`: Checks if Stripe key is Live

**Note**: Format of cc is ccnum|mm|yy|cvv
**Privacy warning: Don't check any of your personal CC's.**
  
<b>URL TOOLS</b>
- `/short (url)`: Shortify given url.
- `/ip (url)`: Displays information about an IP / domain.
- `/direct (url)`: Generates direct links from the sourceforge.net
"""
