from aiogram import F
from states import States
from aiogram.filters.state import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from config import config
from shared import shared
from database import db
from datetime import datetime, timedelta


def setup(router):
    @router.callback_query(F.data.startswith("muting"), StateFilter(States.muting))
    async def muting(callback: CallbackQuery, state: FSMContext):
        await callback.answer()
        await callback.message.delete()
        time = {
            "day": timedelta(days=1),
            "week": timedelta(weeks=1),
            "month": timedelta(days=31),
            "year": timedelta(days=365),
        }
        data = callback.data.split("_")
        user_id = int(data[2])
        if data[1] == "exit":
            await state.clear()
            return
        period = datetime.now() + time[data[1]]
        str_period = datetime.strftime(period, "%d.%m.%Y %H:%M")
        await db.execute(
            "INSERT INTO Banlist VALUES (%s, %s)",
            (user_id, period),
        )
        await db.execute("DELETE FROM Valentines WHERE user_id=%s", (user_id,))
        await shared.bot.send_message(
            chat_id=user_id,
            text=f"Вы были отстранены модератором до {str_period}.",
        )
        await shared.bot.send_message(
            chat_id=config.GROUP_ID,
            text=f"Пользователь с ID {user_id} был отстранен до {str_period}",
        )
        await state.clear()
