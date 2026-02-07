from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def approving_kb(user_id):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="Принять",
            callback_data=f"accept_val^{user_id}",
        ),
        types.InlineKeyboardButton(
            text="Отклонить",
            callback_data=f"reject_val^{user_id}",
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="Замутить",
            callback_data=f"mute_{user_id}",
        )
    )
    return builder
