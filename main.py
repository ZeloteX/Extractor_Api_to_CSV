import sys
import json
from datetime import datetime

from extractor.yahoo_finance_extractor import YahooFinanceExtractor
from configuration.global_config import GlobalConfig


def main(global_config: GlobalConfig):
    if global_config.action == 'Extraction':
        extractor = YahooFinanceExtractor(tickers=global_config.tickers,
                                          start_date=global_config.start_date,
                                          end_date=global_config.end_date)

        res = extractor.extract_data()
        return f"Done: {datetime.now}"
    raise ValueError(f"Action: {global_config.action} unrecognized")


if __name__ == '__main__':
    """Arguments:
    *action         : str       = "Extraction"
    *as_of_date     : Datetime  
    *tickers        : list      #list of financial instrument to get
    *period_in_years: int
    """
    if sys.argv[1]:
        file_name = sys.argv[1]
    else:
        file_name = 'input.json'

    with open(file_name, 'r') as input_data:
        args = json.load(input_data)

    global_config = GlobalConfig(args['action'],
                                 args['as_of_date'],
                                 args['period_in_years'],
                                 args['tickers'])
    main(global_config)
