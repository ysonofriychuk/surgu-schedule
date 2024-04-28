import asyncio
from aiogram import Bot, Dispatcher

from internal.bot.routers.start import router as start_router
from internal.bot.routers.info import router as info_router
from internal.bot.routers.setgroup import router as set_group_router


# Запуск бота
async def main():
    bot = Bot(token="7106430476:AAHEhYmcOT0UPAvMZEdWK0HuAk6FYYtW6rk")
    dp = Dispatcher()

    dp.include_routers(
        start_router,
        info_router,
        set_group_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
