from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def approving_kb(user_id):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="Принять", callback_data=f"accept_val^{user_id}", style="success"
        ),
        types.InlineKeyboardButton(
            text="Отклонить", callback_data=f"reject_val^{user_id}", style="danger"
        ),
    )
    builder.row(
        types.InlineKeyboardButton(
            text="Замутить", callback_data=f"mute_{user_id}", style="primary"
        )
    )
    return builder
