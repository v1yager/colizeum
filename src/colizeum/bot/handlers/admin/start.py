from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from colizeum.bot.filters.is_admin import IsAdmin

router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())

@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer("Hello, admin!")
