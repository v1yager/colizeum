from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from colizeum.bot.filters.is_admin import IsNotAdmin

router = Router()
router.message.filter(IsNotAdmin())
router.callback_query.filter(IsNotAdmin())

@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer("В доступе отказано!")
