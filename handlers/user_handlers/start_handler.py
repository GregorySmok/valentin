from states import States
from aiogram.types import Message
from shared import shared
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

def setup(router):
    @router.message(Command(commands=["start"]))
    async def start_handler(message: Message, state: FSMContext):
        await shared.bot.send_message(message.from_user.id, text="💘 Анонимные признания\n\n"
        "Я опубликую твою валентинку в наш канал\n"
        "Напиши свою валентинку:")
        await state.set_state(States.typing_message)