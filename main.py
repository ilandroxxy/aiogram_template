import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

import handlers.users as users
from keyboards import default_commands

load_dotenv('.env')

BOT_TOKEN: str = os.environ.get('BOT_TOKEN')
PARSE_MODE: str = 'HTML'
storage: MemoryStorage = MemoryStorage()
bot: Bot = Bot(token=BOT_TOKEN, parse_mode=PARSE_MODE)
dp: Dispatcher = Dispatcher(storage=storage)


async def main():
    logging.basicConfig(
        filename='log.log',
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        level=logging.INFO,
        datefmt='%H:%M:%S %d-%m-%Y')
    dp.include_router(users.handler_commands.router)
    dp.include_router(users.handler_inlines.router)
    await default_commands.set_bot_commands(bot)

    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
