from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def next_kb():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Следующая", callback_data="next_val"))
    return builder
