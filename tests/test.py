import sys, unittest
import pandas as pd

sys.path.insert(1, 'src/easy_exchange_rates')
from eer import API


#Constants
BASE_CURRENCY="EUR"
START_DATE="2021-01-01"
END_DATE="2021-08-13"
TARGETS=["USD","CAD"]

class TestGetData(unittest.TestCase):
    def setUp(self):
        self.api = API()

    def test_connection(self):
        """
        Trying to retrieve data from https://exchangerate.host/ 
        """
        time_series = self.api.get_exchange_rates(
            base_currency=BASE_CURRENCY, 
            start_date=START_DATE, 
            end_date=END_DATE, 
            targets=TARGETS
        )
        self.assertIsInstance(time_series, dict)
        dates = list(time_series.keys())
        self.assertEqual(dates[0], START_DATE)
        self.assertEqual(dates[-1], END_DATE)
    

class TestDataToDataFrame(unittest.TestCase):
    def setUp(self):
        self.api = API()

    def test_create_dataframe(self):
        """
        Trying to retrieve data from https://exchangerate.host/ 
        """
        time_series = self.api.get_exchange_rates(
            base_currency=BASE_CURRENCY, 
            start_date=START_DATE, 
            end_date=END_DATE, 
            targets=TARGETS
        )
        self.assertIsInstance(time_series, dict)
        data_frame = self.api.to_dataframe(time_series)
        self.assertIsInstance(data_frame, pd.core.frame.DataFrame)
        

if __name__ == '__main__':
    unittest.main()