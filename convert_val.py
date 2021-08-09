import datetime as dt
from decimal import Decimal

import requests
from bs4 import BeautifulSoup


def get_rates(cur_from, date, requests):
    # ! конвертируем одну валюту в другую через
    # ! через cbr.ru
    result = requests.get(
        "https://www.cbr.ru/scripts/XML_daily.asp",
        {"date_req": date})
    soup = BeautifulSoup(result.content, 'xml')
    rates = {i.CharCode.string: (
        Decimal(i.Value.string.replace(',', '.')),
        int(i.Nominal.string)
    ) for i in soup('Valute')
    }
    return rates[cur_from][0]


today = dt.date.today().strftime("%d.%m.%Y")
print(today)
money_from = 'USD'  # ! какой валюты
# date_any = '2021-08-09'  # ! на какое число. 07.08.2021
print(get_rates(money_from, today, requests), money_from)
