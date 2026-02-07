from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.dispatcher.event.bases import CancelHandler
from database import db
import datetime


class BanMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        # Проверяем, находится ли пользователь в бан-листе
        user_id = event.from_user.id

        # Здесь выполняем запрос к базе данных для проверки
        is_banned, time = await self.check_if_banned(user_id)

        if is_banned:
            # Если пользователь в бан-листе, прерываем обработку
            # Можно также отправить сообщение о том, что пользователь заблокирован
            str_time = datetime.datetime.strftime(time, "%d.%m.%Y %H:%M")
            await event.answer(f"Вы были отстранены модератором до {str_time}.")
            raise CancelHandler()

        # Если пользователь не в бан-листе, продолжаем обработку
        return await handler(event, data)

    async def check_if_banned(self, user_id: str) -> bool:
        result = await db.fetch_one(
            "SELECT * FROM Banlist WHERE user_id = %s", (user_id,)
        )
        if result:
            ban_time = result[1]
            if ban_time > datetime.datetime.now():
                return (True, ban_time)
            else:
                # Если время бана истекло, удаляем запись из бан-листа
                await db.execute("DELETE FROM Banlist WHERE user_id = %s", (user_id,))
        return (False, None)
