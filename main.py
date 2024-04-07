import asyncio
from aiogram import Bot, Dispatcher

from src.bot.routers.start import router as start_router


# Запуск бота
async def main():
    bot = Bot(token="7048218592:AAEmKu0BmAuWt8IEKrLdeavolAVMOOzVO-c")
    dp = Dispatcher()

    dp.include_routers(start_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())