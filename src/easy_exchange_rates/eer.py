import requests
from datetime import datetime
import pandas as pd

class API():    

    def __init__(self):
        self.base_url = 'https://api.exchangerate.host/timeseries?'
        
    def get_exchange_rates(self, base_currency="EUR", start_date="2020-01-01", end_date="2020-01-04",targets=[]):
        date_format = "%Y-%m-%d"
        a = datetime.strptime(start_date, date_format)
        b = datetime.strptime(end_date, date_format)
        delta = b - a
        if delta.days > 366:
            print("Can not retieve more than 366 days of data")
            return False
        query = self.base_url + f'start_date={start_date}&end_date={end_date}&base={base_currency}'
        if targets:
            targets = ','.join(targets)
            query += f'&symbols={targets}'
        response = requests.get(query).json()
        if response["success"]:
            return response["rates"]
        else:
            return response
    
    def to_dataframe(self,ts):
        return pd.DataFrame(ts).T

    def rolling_average(self, df, window=7):
        roll = df.rolling(window).mean()
        roll.columns = [f"roll_{window}_{tag}" for tag in list(roll.columns)]
        return df.merge(roll,right_index=True, left_index=True)

    def rolling_max(self, df, window=7):
        roll = df.rolling(window).max()
        roll.columns = [f"roll_{window}_{tag}" for tag in list(roll.columns)]
        return df.merge(roll,right_index=True, left_index=True)