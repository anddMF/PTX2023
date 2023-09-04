import requests
import os
import json

ACCU_WEATHER_URL = os.getenv('ACCU_WEATHER_URL')
ACCU_WEATHER_KEY = os.getenv('ACCU_WEATHER_KEY')

metric_suffix = "&metric=true"

def get_daily(city_key):
    final_url = ACCU_WEATHER_URL + "forecasts/v1/daily/5day/" + city_key + "?apikey=" + ACCU_WEATHER_KEY + metric_suffix
    response = requests.get(final_url)
    return response.json()


def get_hourly(city_key):
    final_url = ACCU_WEATHER_URL + "forecasts/v1/hourly/12hour/" + city_key + "?apikey=" + ACCU_WEATHER_KEY + metric_suffix
    response = requests.get(final_url)
    return response.json()


def get_current(city_key):
    final_url = ACCU_WEATHER_URL + "currentconditions/v1/" + city_key + "?apikey=" + ACCU_WEATHER_KEY
    response = requests.get(final_url)
    converted_json = json.loads(response.text)
    converted_json[0]['Temperature'] = converted_json[0]['Temperature']['Metric']['Value']
    return converted_json[0]


def get_city_key(query):
    final_url = ACCU_WEATHER_URL + "locations/v1/cities/autocomplete?apikey=" + ACCU_WEATHER_KEY + "&q=" + query
    response = requests.get(final_url)
    return response.json()