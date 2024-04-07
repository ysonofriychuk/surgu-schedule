from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.bot.message import text

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(text.greet.format(name=message.from_user.full_name))
