import pandas as pd
import yfinance as yf

from extractor.extractor import Extractor


class YahooFinanceExtractor(Extractor):
    tickers = list()

    def __init__(self, tickers: list, **kwargs):
        super(YahooFinanceExtractor, self).__init__(**kwargs)
        self.tickers = tickers

    def _call_api(self) -> pd.DataFrame:
        dtf = pd.DataFrame()

        for ticker in self.tickers:
            data = yf.download(ticker, start=self.start_date, end=self.end_date)
            dtf[ticker] = data['Adj Close']

        dtf.reset_index(inplace=True)
        return dtf

    def _post_processing(self, dtf: pd.DataFrame):

        return dtf
