import os

from aiogram.types import Message

from bot import bot, dp
from data.cmc_data import CmcData
from data.yf_data import YfinanceData


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(f'Hi, {message.from_user.first_name}!'
                         f'\nTo check the cryptocurrency just write it down(i.e. bitcoin, ethereum)')


@dp.message_handler(commands=['data'])
async def data(message: Message):
    if message.text == '/data':
        await message.answer('Load data from Yfinance (eg. AAPL, 2021-01-01, 2022-12-31)')
    else:
        index_comma = [i for i in range(0, len(message.text)) if message.text[i] == ',']
        ticker = message.text[9:index_comma[0]].strip()
        start_date = message.text[index_comma[0] + 1:index_comma[1]].strip()
        end_date = message.text[index_comma[1] + 1:].strip()
        yfinance = YfinanceData(ticker, start_date, end_date)
        file = yfinance.get_data_by_date()

        await bot.send_document(document=open(file, 'rb'), chat_id=message.chat.id)
        os.remove(file)


@dp.message_handler(commands=['price'])
async def cmc_price(message: Message):
    if message.text == '/price':
        await message.answer('Coin price (eg. /p btc, /p eth)')
    else:
        try:
            price_index = message.text[6:].strip().upper()
            cmc_data = CmcData(price_index)
            price = cmc_data.get_price()
            await message.answer(price)
        except IndexError:
            await message.answer('Check if the coin spelling is correct')
