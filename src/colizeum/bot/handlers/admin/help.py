from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from colizeum.bot.filters.is_admin import IsAdmin

router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())

@router.message(Command())
async def start_handler(message: Message) -> None:
    if message.from_user:
        await message.answer(f"Привет, <b>{message.from_user.username}</b>!\nСписок команд, которые предоставляет бот:\n\n<i>/rating</i> – показать рейтинговую таблицу\n<i>/new_achievement</i> – добавить достижение\n<i>/get_participants</i> – показать список пользователей")
