import datetime

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from internal.db.db import get_group

router = Router()

host = "sursu-web-app.tw1.su"

with open('internal/bot/assets/message/msg_schedule.txt', 'r', encoding="utf-8") as file:
    msg_schedulenice = file.read()

photo_schedulenice = FSInputFile("internal/bot/assets/images/schedule-nice.jpeg")

with open('internal/bot/assets/message/msg_schedule_baduser.txt', 'r', encoding="utf-8") as file:
    msg_schedulebad = file.read()

photo_schedulebad = FSInputFile("internal/bot/assets/images/schedule-bad.jpg")


def get_date_by_week_day(week_day):
    date = datetime.datetime.now()
    if week_day:
        if date.day <= week_day:
            date += datetime.timedelta(days=week_day)
        else:
            date += datetime.timedelta(days=7 - date.weekday() + week_day)

    return date.strftime("%d-%m-%Y-%H-%M")


@router.message(Command("schedule"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    group_user = get_group(user_id)

    if not group_user:
        await message.answer_photo(
            photo=photo_schedulebad,
            caption=msg_schedulebad.format(name=message.from_user.full_name)
        )
        return

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
           [InlineKeyboardButton(text='Понедельник',
                                 web_app=WebAppInfo(
                                     url=f"https://{host}/schedule?group={group_user}&date={get_date_by_week_day(0)}"))],
           [InlineKeyboardButton(text="Вторник",
                                 web_app=WebAppInfo(
                                     url=f"https://{host}/schedule?group={group_user}&date={get_date_by_week_day(1)}"))],
           [InlineKeyboardButton(text="Среда",
                                 web_app=WebAppInfo(
                                     url=f"https://{host}/schedule?group={group_user}&date={get_date_by_week_day(2)}"))],
           [InlineKeyboardButton(text="Четверг",
                                 web_app=WebAppInfo(
                                     url=f"https://{host}/schedule?group={group_user}&date={get_date_by_week_day(3)}"))],
           [InlineKeyboardButton(text="Пятница",
                                 web_app=WebAppInfo(
                                     url=f"https://{host}/schedule?group={group_user}&date={get_date_by_week_day(4)}"))],
           [InlineKeyboardButton(text="Суббота",
                                 web_app=WebAppInfo(
                                     url=f"https://{host}/schedule?group={group_user}&date={get_date_by_week_day(5)}"))],
        ])

    await message.answer_photo(
        photo_schedulenice,
        caption=msg_schedulenice.format(name=message.from_user.full_name),
        reply_markup=btn
    )
