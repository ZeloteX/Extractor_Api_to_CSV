import unittest
import json
from configuration.global_config import GlobalConfig
from extractor.yahoo_finance_extractor import YahooFinanceExtractor


@unittest.skip('only for unittest')
class TestExtraction(unittest.TestCase):
    # initialization
    with open('input.json', 'r') as input_data:
        data = json.load(input_data)
    global_config = GlobalConfig(**data)

    def test_yfinance_extraction_when_extract_data(self):
        extractor = YahooFinanceExtractor(tickers=self.global_config.tickers,
                                          start_date=self.global_config.start_date,
                                          end_date=self.global_config.end_date)
        dtf_res = extractor.extract_data()
        self.assertIsNotNone(dtf_res, "dtf is None")


if __name__ == '__main__':
    unittest.main()
