from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (
    CallbackQuery,
    Message,
    ReplyKeyboardRemove,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from prettytable import PrettyTable

from colizeum.app.db import Session
from colizeum.app.models import Groups
from colizeum.app.utils.users import get_users
from colizeum.bot.filters.is_admin import IsAdmin

router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


class GetUsersGroupsCallback(CallbackData, prefix="user_groups"):
    group: Groups


def build_keyboard_for_groups():
    builder = InlineKeyboardBuilder()
    for group in Groups:
        builder.button(text=group.value, callback_data=GetUsersGroupsCallback(group=group).pack())

    builder.adjust(2)
    return builder.as_markup()


@router.message(Command("get_users"))
async def get_users_handler(message: Message) -> None:
    await message.answer("Выберите классы:", reply_markup=build_keyboard_for_groups())


@router.callback_query(GetUsersGroupsCallback.filter())
async def get_users_callback(
    callback: CallbackQuery,
    callback_data: GetUsersGroupsCallback
) -> None:
    async with Session() as session:
        users = await get_users(session, callback_data.group)

    if not users:
        await callback.answer("Рейтинг пуст", show_alert=True)
        return

    table = PrettyTable()
    table.field_names = ["ID", "Имя", "Фамилия", "Класс"]
    for row in users:
        table.add_row([row.id, row.firstname, row.lastname, row.grade])
        table.add_divider()

    # Форматируем как моноширинный HTML-блок
    response = f"<pre>{table}</pre>"
    if isinstance(callback.message, Message):
        await callback.message.edit_text(response)
    else:
        await callback.answer(response, reply_markup=ReplyKeyboardRemove())
