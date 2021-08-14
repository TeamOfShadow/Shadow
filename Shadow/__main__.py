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

import pyrogram
import asyncio
import os
from importlib import import_module

from aiogram import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from Shadow import TOKEN
from Shadow.config import get_bool_key, get_list_key
from Shadow.modules import ALL_MODULES, LOADED_MODULES, MOD_HELP
from Shadow.services.pyrogram import pbot
from Shadow.utils.logger import log

if get_bool_key("DEBUG_MODE"):
    log.debug("Enabling logging middleware.")

LOAD = get_list_key("LOAD")
DONT_LOAD = get_list_key("DONT_LOAD")


# Import misc stuff

if not get_bool_key("DEBUG_MODE"):
    import_module("Shadow.utils.sentry")


async def before_srv_task(loop):
    for module in [m for m in LOADED_MODULES if hasattr(m, "__before_serving__")]:
        log.debug("Before serving: " + module.__name__)
        loop.create_task(module.__before_serving__(loop))


async def start():
    log.debug("Starting before serving task for all modules...")
    loop.create_task(before_srv_task(loop))
    if not get_bool_key("DEBUG_MODE"):
        log.debug("Waiting 2 seconds...")
        await asyncio.sleep(2)


async def start_webhooks(_):
    os.getenv("WEBHOOK_URL") + f"/{TOKEN}"
    return await start(_)


log.info("Starting loop..")
log.info("Pyrogram: Using polling method")


async def run_bot():
    """Run The Bot"""
    
    if get_bool_key("LOAD_MODULES"):
        if len(LOAD) > 0:
            modules = LOAD
        else:
            modules = ALL_MODULES

        modules = [x for x in modules if x not in DONT_LOAD]

        log.info("Modules to load: %s", str(modules))
        for module_name in modules:
            # Load pm_menu at last
            if module_name == "pm_menu":
                continue
            log.debug(f"Importing <d><n>{module_name}</></>")
            imported_module = import_module("Shadow.modules." + module_name)
            if hasattr(imported_module, "__help__"):
                if hasattr(imported_module, "__mod_name__"):
                    MOD_HELP[imported_module.__mod_name__] = imported_module.__help__
                else:
                    MOD_HELP[imported_module.__name__] = imported_module.__help__
            LOADED_MODULES.append(imported_module)
        log.info("Modules loaded!")
    else:
        log.warning("Not importing modules!")

    log.info("Here We Go")
    await pyrogram.idle()


if __name__ == "__main__":
    pbot.loop.run_until_complete(run_bot())
