from aiogram import F
from states import States
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from config import config
from shared import shared
from keyboards import mute_kb


def setup(router):
    @router.callback_query(F.data.startswith("mute_"))
    async def mute_handler(callback: CallbackQuery, state: FSMContext):
        await callback.answer()
        await callback.message.delete()
        user_id = int(callback.data.split("_")[1])
        await shared.bot.send_message(
            chat_id=config.GROUP_ID,
            text=f"Замутить ID {user_id} на:",
            reply_markup=mute_kb(user_id).as_markup(),
        )
        await state.set_state(States.muting)
