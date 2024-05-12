import asyncio
from aiogram import Bot, Dispatcher

from internal.bot.routers.start import router as start_router
from internal.bot.routers.info import router as info_router
from internal.bot.routers.setgroup import router as set_group_router
from internal.bot.routers.schedule import router as schedule_router

# Запуск бота
async def main():
    bot = Bot(token="6784641067:AAGEaeTF3GoEN6vOJn1gHMzb-l70gmfLBno")
    dp = Dispatcher()

    dp.include_routers(
        start_router,
        info_router,
        set_group_router,
        schedule_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
