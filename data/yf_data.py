import yfinance as yf


class YfinanceData:

    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start = start
        self.end = end

    def get_data_by_date(self):
        data_by_date = yf.download(self.ticker, self.start, self.end)
        data_by_date.to_csv('data.csv', header=True, sep=' ')
        return f'data.csv'


# yfinance = YfinanceData('AAPL', '2019-01-01', '2021-12-31')
# print(yfinance.get_data_by_date())
