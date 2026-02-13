from states import States
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import F


def setup(router):
    @router.message(F.text == "Написать валентинку")
    async def typing_valentin_handler(message: Message, state: FSMContext):
        await message.answer(
            "<tg-emoji emoji-id='5285184156555306745'>💌</tg-emoji> Введи текст валентинки:"
        )
        await state.set_state(States.typing_message)
