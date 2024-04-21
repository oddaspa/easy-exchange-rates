import requests
from datetime import datetime
import pandas as pd
import io

class API():    

    def __init__(self):
        self.base_url = 'https://data-api.ecb.europa.eu/service/data/EXR/'
        
    def get_exchange_rates(self, base_currency="EUR", start_date="2020-01-01", end_date="2020-01-04",targets=[]):
        
        query = f'{self.base_url}D.{"+".join(targets)}.{base_currency}.SP00.A'
        
        response = requests.get(
            query,
            params = {
                'startPeriod': start_date,
                'endPeriod': end_date
            },
            headers = {'Accept': 'text/csv'})

        if response.ok:
            df = pd.read_csv(io.StringIO(response.text))
            df = df.set_index("TIME_PERIOD")
            df = df[["CURRENCY", "OBS_VALUE"]]
            df = df.pivot(columns=["CURRENCY"])
            df.columns = [c[1] for c in df.columns]
            return df
        else:
            return response

    def rolling_average(self, df, window=7):
        roll = df.rolling(window).mean()
        roll.columns = [f"roll_{window}_{tag}" for tag in list(roll.columns)]
        return df.merge(roll,right_index=True, left_index=True)

    def rolling_max(self, df, window=7):
        roll = df.rolling(window).max()
        roll.columns = [f"roll_{window}_{tag}" for tag in list(roll.columns)]
        return df.merge(roll,right_index=True, left_index=True)