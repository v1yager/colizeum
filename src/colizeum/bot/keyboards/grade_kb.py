
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class GradeCallback(CallbackData, prefix="format"):
    grade: int


def build_keyboard_for_grade() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(5, 12):
        builder.button(text=str(i), callback_data=GradeCallback(grade=i).pack())

    builder.adjust(3)
    return builder.as_markup()
