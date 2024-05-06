from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from internal.db.db import get_group

router = Router()

host = str("your-host")

with open('internal/bot/assets/message/msg_schedule.txt', 'r', encoding="utf-8") as file:
    msg_schedulenice = file.read()

photo_schedulenice = FSInputFile("internal/bot/assets/images/schedule-nice.jpeg")

with open('internal/bot/assets/message/msg_schedule_baduser.txt', 'r', encoding="utf-8") as file:
    msg_schedulebad = file.read()


photo_schedulebad = FSInputFile("internal/bot/assets/images/schedule-bad.jpg")


@router.message(Command("schedule"))
async def cmd_start(message: Message):
    if not get_group(message.from_user.id):
        await message.answer_photo(photo=photo_schedulebad, caption=msg_schedulebad.format(name=message.from_user.full_name))
        return

    user_id = str(message.from_user.id)

    btn = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                              [InlineKeyboardButton(text='Понедельник',
                                                                   web_app=WebAppInfo(url=f"https://{host}/user?user_id={user_id}"))],
                                              [InlineKeyboardButton(text="Вторник",
                                                                   web_app=WebAppInfo(url=f"https://{host}/user?user_id={user_id}"))],
                                              [InlineKeyboardButton(text="Среда",
                                                                   web_app=WebAppInfo(url=f"https://{host}/user?user_id={user_id}"))],
                                              [InlineKeyboardButton(text="Четверг",
                                                                   web_app=WebAppInfo(url=f"https://{host}/user?user_id={user_id}"))],
                                              [InlineKeyboardButton(text="Пятница",
                                                                   web_app=WebAppInfo(url=f"https://{host}/user?user_id={user_id}"))],
                                              [InlineKeyboardButton(text="Суббота",
                                                                   web_app=WebAppInfo(url=f"https://{host}/user?user_id={user_id}"))],
                                      ])

    await message.answer_photo(photo_schedulenice, caption=msg_schedulenice.format(name=message.from_user.full_name), reply_markup=btn)