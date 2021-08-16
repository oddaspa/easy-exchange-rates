# easy-exchange-rates

[![PyPI package](https://img.shields.io/badge/pip%20install-easy--exchange--rates-brightgreen)](https://pypi.org/project/easy-exchange-rates/) [![version number](https://img.shields.io/pypi/v/easy-exchange-rates?color=green&label=version)](https://pypi.org/project/easy-exchange-rates/releases) [![Actions Status](https://github.com/tomchen/example_pypi_package/workflows/Test/badge.svg)](https://github.com/oddaspa/easy-exchange-rates/actions) [![License](https://img.shields.io/github/license/oddaspa/easy-exchange-rates)](https://github.com/oddaspa/easy-exchange-rates/blob/main/LICENSE.txt)

## Usage
```python
from easy_exchange_rates import API
api = API()
time_series = api.get_exchange_rates(
  base_currency="EUR", 
  start_date="2021-01-01", 
  end_date="2021-08-13", 
  targets=["USD","CAD"]
)
data_frame = api.to_dataframe(time_series)
print(data_frame.head(5))
>>>
                 CAD       USD
2021-01-01  1.549988  1.217582
2021-01-02  1.544791  1.213500
2021-01-03  1.557791  1.223409
2021-01-04  1.566076  1.225061
2021-01-05  1.558553  1.229681
```


# Testing

```
python3 -m unittest discover -s tests
```