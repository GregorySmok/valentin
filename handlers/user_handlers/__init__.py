from aiogram import Router
from . import start_handler
from . import valentine_handler

user_router = Router()
start_handler.setup(user_router)
valentine_handler.setup(user_router)