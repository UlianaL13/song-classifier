import asyncio
from aiogram import Dispatcher
from bot.utils.handlers import router
from bot.create_bot import bot

async def main():
    dp = Dispatcher()
    dp.include_router (router)

    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())
