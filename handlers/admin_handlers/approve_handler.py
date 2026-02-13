from aiogram.types import CallbackQuery
from database import db
from shared import shared
from aiogram import F
from config import config
from keyboards import next_kb


def setup(router):
    @router.callback_query(F.data.startswith("accept_val"))
    async def approve_val(callback: CallbackQuery):
        callback.answer()
        user_id = int(callback.data.split("^")[-1])
        valentine = await db.fetch_one(
            "SELECT text FROM Valentines WHERE user_id = %s", (user_id,)
        )
        if not valentine:
            callback.message.answer("Этой валентинки уже нет")
            return
        valentine = valentine[0]
        text = f"Новая валентинка<tg-emoji emoji-id='5285184156555306745'>💌</tg-emoji> \n\n{valentine}"
        await shared.bot.send_message(chat_id=config.CHANNEL_ID, text=text)
        await db.execute("DELETE FROM Valentines WHERE user_id=%s", (user_id,))
        await callback.message.delete()
        await shared.bot.send_message(
            config.GROUP_ID,
            "Валентинка выложена в канал",
            reply_markup=next_kb().as_markup(),
        )
        await shared.bot.send_message(user_id, "Ваша валентинка отправлена!")
