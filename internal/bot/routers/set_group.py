from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("set-group"))
async def cmd_start(message: Message):
    # TODO SURGU-010
    pass