import logging
from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os
import time

load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('TOKEN'), parse_mode='HTML')
dp = Dispatcher(bot)
start_time = time.time()

if __name__ == '__main__':
    from handlers.handlers import dp
    executor.start_polling(dp, skip_updates=True)
