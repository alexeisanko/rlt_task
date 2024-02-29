import os
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
import motor.motor_asyncio

import handlers

client = motor.motor_asyncio.AsyncIOMotorClient()
db = client["main_db"]
collection = db["rlt_test_collection"]


async def main():
    bot = Bot(os.environ['TG_TOKEN'])
    dp = Dispatcher()
    dp.include_router(handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
