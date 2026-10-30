from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from colizeum.app.models import AwardPlace


class PlaceCallback(CallbackData, prefix="place"):
    place: AwardPlace


def build_keyboard_for_place() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for place in AwardPlace:
        builder.button(text=place.value, callback_data=PlaceCallback(place=place).pack())

    builder.adjust(2)
    return builder.as_markup()
