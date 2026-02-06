from states import States
from aiogram.types import Message
from aiogram.filters.state import StateFilter
from database import db
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from config import config
from shared import shared
from keyboards import create_valentin_btn
import pymysql


def setup(router):
    @router.message(StateFilter(States.typing_message))
    async def valentine_hand(message: Message, state: FSMContext):
        text = message.text
        if len(text) > 4096:
            await message.answer("Слишком большое сообщение, попробуйте другое.")
            return
        user_id = message.from_user.id
        try:
            await db.execute(
                "INSERT INTO Valentines (user_id, text, status, username) values (%s, %s, %s, %s)",
                (user_id, text, "waiting", message.from_user.username),
            )
            await shared.bot.send_message(
                chat_id=config.GROUP_ID,
                text="Новая валентинка отправлена на модерацию. /check",
            )
            await message.answer(
                "Ваша валентинка отправлена на модерацию",
                reply_markup=create_valentin_btn().as_markup(resize_keyboard=True),
            )
        except pymysql.err.IntegrityError:
            await message.answer(
                "Ваша предыдущая валентинка еще на рассмотрении, попробуйте позже.",
                reply_markup=create_valentin_btn().as_markup(resize_keyboard=True),
            )
        except Exception as e:
            await message.answer(
                "Не удалось отправить валентинку, попробуйте позже или обратитесь к администратору."
            )
            print(e)
            raise
        finally:
            await state.set_state(default_state)
