from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("info"))
async def cmd_start(message: Message):
    await message.answer(
        "Информация:"
        "/start - Запустить бота"
        "/info - Информация о боте"
        "/groupby - Добавить свою группу",
    )
