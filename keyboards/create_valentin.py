from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


def create_valentin_btn():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="💘 Написать валентинку"))
    return builder
