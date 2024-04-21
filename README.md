# Easy Exchange Rates

[![PyPI package](https://img.shields.io/badge/pip%20install-easy--exchange--rates-brightgreen)](https://pypi.org/project/easy-exchange-rates/) 
[![version number](https://img.shields.io/pypi/v/easy-exchange-rates?color=green&label=version)](https://pypi.org/project/easy-exchange-rates/) 
[![Actions Status](https://github.com/oddaspa/easy-exchange-rates/workflows/Build%20status/badge.svg)](https://github.com/oddaspa/easy-exchange-rates/actions) 
[![License](https://img.shields.io/github/license/oddaspa/easy-exchange-rates)](https://github.com/oddaspa/easy-exchange-rates/blob/main/LICENSE.txt)

A python package for retrieving currency exchange data from https://data.ecb.europa.eu/ to a pandas dataframe.
## Usage
```python
from easy_exchange_rates import API
api = API()
df = api.get_exchange_rates(
  base_currency="EUR", 
  start_date="2024-03-12",
  end_date="2024-04-21",
  targets=["USD","CAD"]
)
print(df.head(5))
>>>
	        CAD	    USD
TIME_PERIOD		
2024-03-12	1.4739	1.0916
2024-03-13	1.4756	1.0939
2024-03-14	1.4725	1.0925
2024-03-15	1.4731	1.0892
2024-03-18	1.4745	1.0892
```


# Testing

```
python3 -m unittest discover -s tests
```
