# using the repo https://github.com/fawazahmed0/currency-api from Fawaz Ahmed to get the currencies

import os
import requests
import json
from api.model.currency import Currency


CURRENCY_URL_1 = os.getenv('CURRENCY_URL_1')
CURRENCY_URL_2 = os.getenv('CURRENCY_URL_2')


def get_currency_rate(base, expected, date):
    rate_url_addon = base.lower() + '/' + expected.lower() + '.json'

    final_url = CURRENCY_URL_1 + date + '/currencies/' + rate_url_addon
    response = requests.get(final_url)
    converted_json = json.loads(response.text)
    currency_rate = Currency(converted_json[expected.lower()], converted_json['date'])
    return currency_rate
