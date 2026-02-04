from states import States
from aiogram.types import Message
from aiogram.filters.state import StateFilter
from database import db
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from config import config
from shared import shared
from aiogram import F
from aiogram.filters import Command
from keyboards import approving_kb

def setup(router):
    @router.message(Command(commands=["check"]) , F.chat.id == config.GROUP_ID)
    @router.callback_query(F.data.startswith("next"))
    async def check_valentine(message: Message):
        valentine = (await db.fetch_one("SELECT * FROM Valentines"))
        if not valentine:
            await shared.bot.send_message(config.GROUP_ID, "✅ Все валентинки проверены!")
            return
        text = f"Валентинка от @{valentine[-1]}\nID: {valentine[0]}\n\n{valentine[1]}"
        await shared.bot.send_message(config.GROUP_ID, text, reply_markup=approving_kb(valentine[0]).as_markup())
