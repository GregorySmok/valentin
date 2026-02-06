from aiogram import Router
from . import check_handler
from . import approve_handler
from . import reject_handler

admin_router = Router()
check_handler.setup(admin_router)
approve_handler.setup(admin_router)
reject_handler.setup(admin_router)
