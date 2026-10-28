from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from colizeum.app.models import Groups


class GroupsCallback(CallbackData, prefix="groups"):
    group: Groups


def build_keyboard_for_groups():
    builder = InlineKeyboardBuilder()
    for group in Groups:
        builder.button(text=group.value, callback_data=GroupsCallback(group=group).pack())

    builder.adjust(2)
    return builder.as_markup()
