
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from colizeum.app.models import AwardParticipationFormat


class FormatCallback(CallbackData, prefix="format"):
    participation_format: AwardParticipationFormat


def build_keyboard_for_format() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for format in AwardParticipationFormat:
        builder.button(text=format.value, callback_data=FormatCallback(participation_format=format).pack())

    builder.adjust(2)
    return builder.as_markup()
