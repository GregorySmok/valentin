from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def mute_kb(user_id):
    """Клавиатура мутов"""
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="День", callback_data=f"muting_day_{user_id}"),
        types.InlineKeyboardButton(
            text="Неделя", callback_data=f"muting_week_{user_id}"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="Месяц", callback_data=f"muting_month_{user_id}"
        ),
        types.InlineKeyboardButton(text="Год", callback_data=f"muting_year_{user_id}"),
    )
    builder.row(
        types.InlineKeyboardButton(text="Отмена", callback_data="muting_exit"),
    )
    return builder
