from aiogram.types import CallbackQuery
from database import db
from shared import shared
from aiogram import F
from config import config
from keyboards import next_kb

def setup(router):
    @router.callback_query(F.data.startswith("reject_val"))
    async def approve_val(callback: CallbackQuery):
        callback.answer()
        user_id = int(callback.data.split("^")[-1])
        valentine = await db.fetch_one("SELECT text FROM Valentines WHERE user_id = %s", (user_id, ))
        if not valentine:
            callback.message.answer("Этой валентинки уже нет")
            return
        await db.execute("DELETE FROM Valentines WHERE user_id=%s", (user_id))
        await callback.message.delete()
        await shared.bot.send_message(config.GROUP_ID, "Валентинка была аннигилирована", reply_markup=next_kb().as_markup())
        await shared.bot.send_message(user_id, "Ваша валентинка отклонена!")