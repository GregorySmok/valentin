from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def approving_kb(user_id):
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="Принять",
            callback_data=f"accept_val^{user_id}",
        )
    )
    builder.add(
        types.InlineKeyboardButton(
            text="Отклонить",
            callback_data=f"reject_val^{user_id}",
        )
    )
    return builder
