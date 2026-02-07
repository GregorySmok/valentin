from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    typing_message = State()
    muting = State()
