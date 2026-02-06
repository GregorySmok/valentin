from states import States
from aiogram.types import Message
from shared import shared
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from keyboards import create_valentin_btn


def setup(router):
    @router.message(Command(commands=["start"]))
    async def start_handler(message: Message, state: FSMContext):
        await shared.bot.send_message(
            message.from_user.id,
            text="💘 Анонимные признания\n\n"
            "Я опубликую твою валентинку в наш канал\n"
            "Нажми на кнопку, чтобы написать валентинку",
            reply_markup=create_valentin_btn().as_markup(resize_keyboard=True),
        )
