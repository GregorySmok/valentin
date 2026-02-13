from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


def create_valentin_btn():
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(
            text="Написать валентинку", icon_custom_emoji_id="5285184156555306745"
        )
    )
    return builder
