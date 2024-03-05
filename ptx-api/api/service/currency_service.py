# using the repo https://github.com/fawazahmed0/exchange-api from Fawaz Ahmed to get the currencies

import os
import requests
import json
from api.model.currency import Currency


CURRENCY_URL_1 = os.getenv('CURRENCY_URL_1')
CURRENCY_URL_2 = os.getenv('CURRENCY_URL_2')


def get_currency_rate(base, expected, date):
    rate_url_addon = base.lower() + '.json'

    final_url = CURRENCY_URL_1 + date + '/v1/currencies/' + rate_url_addon
    response = requests.get(final_url)
    converted_json = json.loads(response.text)
    currency_rate = Currency(
        converted_json[base.lower()][expected.lower()], converted_json['date'])
    return currency_rate
