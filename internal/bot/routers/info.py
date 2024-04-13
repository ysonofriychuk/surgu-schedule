from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()

with open('internal/bot/message/msg_info.txt', 'r', encoding="utf-8") as file:
    msg_info = file.read()


@router.message(Command("info"))
async def cmd_start(message: Message):
    await message.answer(msg_info)
