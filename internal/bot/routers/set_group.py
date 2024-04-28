from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from internal.schedule.schedule import Schedule


router = Router()
schedule = Schedule({})

with open('internal/bot/assets/message/msg_set-group.txt', 'r', encoding="utf-8") as file:
    msg_sg = file.read()

@router.message(Command("set-group"))
async def cmd_start(message: Message):
    if len(message.text.split()) != 2:
        await message.answer(msg_sg)
