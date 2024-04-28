from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from internal.schedule.schedule import Schedule

router = Router()
schedule = Schedule({})

with open('internal/bot/assets/message/msg_setgroup.txt', 'r', encoding="utf-8") as file:
    msg_sg = file.read()
photo_baduser = FSInputFile("internal/bot/assets/images/setgroup-bad.png")

@router.message(Command("setgroup"))
async def cmd_start(message: Message):
    if len(message.text.split()) != 2:
        await message.answer_photo(photo=photo_baduser, caption=msg_sg.format(name=message.from_user.full_name))

    # else:



