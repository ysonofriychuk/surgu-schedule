from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

router = Router()

with open('internal/bot/assets/message/msg_start.txt', 'r', encoding="utf-8") as file:
    msg_info = file.read()

photo_start = FSInputFile("internal/bot/assets/images/hello.jpg")


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer_photo(photo=photo_start, caption=msg_info.format(name=message.from_user.full_name))
