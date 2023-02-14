import os
import time

from coinmarketcapapi import CoinMarketCapAPI
from dotenv import load_dotenv

from bot import start_time

load_dotenv()


class CmcData:

    def __init__(self, symbol):
        self.symbol = symbol
        self.response_price = None
        self.slug = None
        self.get_cmc_data()

    def get_cmc_data(self):
        cmc = CoinMarketCapAPI(api_key=os.getenv('CMC_api_key'))
        response_price = cmc.cryptocurrency_quotes_latest(symbol=self.symbol)
        self.response_price = response_price.data[self.symbol][0]['quote']['USD']
        self.slug = response_price.data[self.symbol][0]['slug']

    def get_price(self):
        price = round(self.response_price['price'])
        market_cap = round(self.response_price['market_cap'])
        volume_24h = round(self.response_price['volume_24h'])
        percent_change_1h = self.response_price['percent_change_1h']
        percent_change_24h = self.response_price['percent_change_24h']
        percent_change_7d = self.response_price['percent_change_7d']
        chart_link = "<a href='https://coinmarketcap.com/currencies/{}/'>Charts</a>".format(self.slug)

        response = f'\U0001F4B8Price: {price:,}$' \
                   f'\n\U0001f4b0Market Cap: {market_cap:,}$' \
                   f'\n\U0001f4b1Volume 24H: {volume_24h:,}$' \
                   f'\n\U0001f4c8Percent Change 1H: {percent_change_1h:.2f}%' \
                   f'\n\U0001f4c8Percent Change 24H: {percent_change_24h:.2f}%' \
                   f'\n\U0001f4c8Percent Change 7d: {percent_change_7d:.2f}%' \
                   f'\n{"-" * 20}' \
                   f'\n\U0001f4b9{chart_link}|Coinmarketcap' \
                   f'\n\u23f1Time since launch: {round(time.time() - start_time) // 86400} days'
        return response


# coinmarketcap = CmcData('BTC')
# print(coinmarketcap.get_cmc_data())
