from aiogram import Router
from . import start_handler
from . import valentine_handler
from . import typing_valentin

user_router = Router()
start_handler.setup(user_router)
valentine_handler.setup(user_router)
typing_valentin.setup(user_router)
