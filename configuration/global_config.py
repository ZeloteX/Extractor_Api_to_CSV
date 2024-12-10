from datetime import datetime
import json

from configuration.config import Config


class GlobalConfig:
    action: str
    start_date: datetime
    end_date: datetime
    tickers: list

    def __init__(self,
                 action: str,
                 as_of_date: str,
                 period_in_years: int,
                 tickers: list):

        self.action = action
        period_in_years = period_in_years
        self.end_date = datetime.strptime(as_of_date, Config.DATE_FORMAT)
        self.start_date = self.end_date.replace(year=self.end_date.year - period_in_years)
        self.tickers = [ticker.upper() for ticker in tickers]

