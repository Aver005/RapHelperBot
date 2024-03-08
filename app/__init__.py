import os
from aiogram import Bot, Dispatcher, Router

API_TOKEN = os.getenv("TOKEN")
bot = Bot(token=API_TOKEN, parse_mode='HTML')

dp = Dispatcher()
router = Router()
dp.include_router(router)

import logging
logging.basicConfig(level=logging.INFO)

from .routes import *
