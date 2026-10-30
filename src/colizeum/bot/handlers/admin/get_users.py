from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from prettytable import PrettyTable

from colizeum.app.db import Session
from colizeum.app.utils.users import get_users
from colizeum.bot.filters.is_admin import IsAdmin

router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())

@router.message(Command("get_users"))
async def get_users_handler(message: Message) -> None:
    async with Session() as session:
        users = await get_users(session)

    if not users:
        await message.answer("Рейтинг пуст", show_alert=True)
        return

    table = PrettyTable()
    table.field_names = ["ID", "Имя", "Фамилия", "Класс"]
    for row in users:
        table.add_row([row.id, row.firstname, row.lastname, row.grade])

    # Форматируем как моноширинный HTML-блок
    response = f"<pre>{table}</pre>"
    await message.answer(response)
