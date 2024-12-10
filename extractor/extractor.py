from datetime import datetime
import pandas as pd
from abc import abstractmethod

from configuration.config import Config


class Extractor:
    """
    Mother class: extractor
    Extract data
    """
    start_date = None
    end_date = None
    extractor_name: str

    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date

        self.extractor_name = '_'.join([self.__class__.__name__,
                                        end_date.strftime(Config.DATE_FORMAT)])

    def extract_data(self):
        dtf = self._call_api()

        # --- Mocking ---#
        dtf.to_csv(f'tests/mocks/extractions/{self.extractor_name}',
                   sep=';', index=False)

        # --- ------- ---#

        dtf_res = self._post_processing(dtf)

        # --- Mocking ---#
        dtf_res.to_csv(f'tests/mocks/outputs/{self.extractor_name}',
                   sep=';', index=False)

        # --- ------- ---#

        return dtf_res

    @abstractmethod
    def _call_api(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def _post_processing(self, dtf: pd.DataFrame):
        pass
