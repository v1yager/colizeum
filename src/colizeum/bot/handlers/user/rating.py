from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from prettytable import PrettyTable

from colizeum.app.db import Session
from colizeum.app.utils.rating import get_rating
from colizeum.bot.keyboards.groups_kb import GroupsCallback, build_keyboard_for_groups

router = Router()

@router.message(Command("rating"))
async def command_rating_handler(message: Message):
    await message.answer("Классы:", reply_markup=build_keyboard_for_groups())


@router.callback_query(GroupsCallback.filter())
async def junior_callback_query(callback: CallbackQuery, callback_data: GroupsCallback):
    await callback.answer()

    async with Session() as session:
        rating = await get_rating(session, callback_data.group)

    if not rating:
        await callback.answer("Рейтинг пуст", show_alert=True)
        return

    table = PrettyTable()
    table.field_names = ["Имя", "Фамилия", "Класс", "Баллы"]
    for row in rating:
        table.add_row([row.firstname, row.lastname, row.grade, row.total_points])

    # Форматируем как моноширинный HTML-блок
    response = f"<pre>{table}</pre>"
    if isinstance(callback.message, Message):
        await callback.message.edit_text(response)
    else:
        await callback.answer(response)
