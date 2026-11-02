
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ConfirmCallback(CallbackData, prefix="confirm"):
    confirm: bool


def build_keyboard_for_confirm() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Сохранить", callback_data=ConfirmCallback(confirm=True).pack())
    builder.button(text="Отмена", callback_data=ConfirmCallback(confirm=False).pack())
    builder.adjust(1)
    return builder.as_markup()
