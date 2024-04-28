import json

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from internal.db.db import set_group
from internal.schedule.schedule import Schedule

router = Router()

with open('internal/bot/assets/message/msg_setgroup.txt', 'r', encoding="utf-8") as file:
    msg_sg = file.read()
photo_baduser = FSInputFile("internal/bot/assets/images/setgroup-bad.png")

with open('internal/schedule/schedule.json', "r", encoding='utf-8') as file:
    configuration = json.load(file)

schedule = Schedule(configuration)


@router.message(Command("setgroup"))
async def cmd_start(message: Message):
    if len(message.text.split()) != 2:
        await message.answer_photo(photo=photo_baduser, caption=msg_sg.format(name=message.from_user.full_name))
        return
    if not schedule.group_exist(message.text.split()[-1]):
        await message.answer_photo(photo=photo_baduser, caption=msg_sg.format(name=message.from_user.full_name))
        return
    set_group(message.from_user.id, message.text.split()[-1])
    print(message.from_user.id, message.text.split()[-1])


