from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from colizeum.app.models import AwardLevel


class LevelCallback(CallbackData, prefix="level"):
    level: AwardLevel


def build_keyboard_for_level() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for level in AwardLevel:
        builder.button(text=level.value, callback_data=LevelCallback(level=level).pack())

    builder.adjust(2)
    return builder.as_markup()
