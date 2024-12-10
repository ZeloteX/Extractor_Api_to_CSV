import unittest

from configuration.global_config import GlobalConfig
from main import main


class TestMain(unittest.TestCase):
    # initialization
    args = {
        "action": "Extraction",
        "as_of_date": "2024-12-01",
        "tickers": ["AAPL", "AMZN"],
        "period_in_years": 2
    }

    global_config = GlobalConfig(args['action'],
                                 args['as_of_date'],
                                 args['period_in_years'],
                                 args['tickers'])

    def test_main_when_extraction(self):
        result = main(self.global_config)
        self.assertIsNotNone(result, "Result is None")


if __name__ == '__main__':
    unittest.main()
