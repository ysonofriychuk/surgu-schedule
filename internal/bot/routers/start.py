from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()

with open('internal/bot/message/msg_start.txt', 'r', encoding="utf-8") as file:
    msg_info = file.read()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(msg_info.format(name=message.from_user.full_name))
