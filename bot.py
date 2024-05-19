import argparse
import asyncio
from aiogram import Bot, Dispatcher

from internal.bot.routers.start import router as start_router
from internal.bot.routers.info import router as info_router
from internal.bot.routers.setgroup import router as set_group_router
from internal.bot.routers.schedule import router as schedule_router


# TODO реализовать получение токена аргументов запуска скрипта (web.py)

async def main():
    parser = argparse.ArgumentParser(
        description="SurSU Schedule bot"
    )

    parser.add_argument("--token", help="Token for bot", required=True)
    args = parser.parse_args()

    bot = Bot(token=args.token)
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
