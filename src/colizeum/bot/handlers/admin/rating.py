from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from prettytable import PrettyTable

from colizeum.app.db import Session
from colizeum.app.models import Groups
from colizeum.app.queries.rating import get_rating
from colizeum.bot.filters.is_admin import IsAdmin

router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())

class RatingGroupsCallback(CallbackData, prefix="rating_groups"):
    group: Groups


def build_keyboard_for_groups():
    builder = InlineKeyboardBuilder()
    for group in Groups:
        builder.button(text=group.value, callback_data=RatingGroupsCallback(group=group).pack())

    builder.adjust(2)
    return builder.as_markup()


@router.message(Command("rating"))
async def command_rating_handler(message: Message):
    await message.answer("Классы:", reply_markup=build_keyboard_for_groups())


@router.callback_query(RatingGroupsCallback.filter())
async def rating_callback_query(callback: CallbackQuery, callback_data: RatingGroupsCallback):
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
        table.add_divider()

    # Форматируем как моноширинный HTML-блок
    response = f"<pre>{table}</pre>"
    if isinstance(callback.message, Message):
        await callback.message.edit_text(response)
    else:
        await callback.answer(response)
