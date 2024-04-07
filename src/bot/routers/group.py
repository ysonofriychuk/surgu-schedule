import json

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()

with open("C:\Develop\surgu-schedule\schedule.json", "r", encoding='utf-8') as file:
    configuration = json.load(file)


@router.message(Command("group"))
async def cmd_start(message: Message):
    text = message.text
    text = text.split(' ')
    await message.answer(f"{configuration[text[1]]}")