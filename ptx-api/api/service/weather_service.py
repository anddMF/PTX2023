# endpoint from https://www.accuweather.com

import requests
import os
import json

ACCU_WEATHER_URL = os.getenv('ACCU_WEATHER_URL')
ACCU_WEATHER_KEY = os.getenv('ACCU_WEATHER_KEY')
UNSPLASH_URL = os.getenv('UNSPLASH_URL')

metric_suffix = "&metric=true"


def get_daily(city_key):
    final_url = ACCU_WEATHER_URL + "forecasts/v1/daily/5day/" + city_key + "?apikey=" + ACCU_WEATHER_KEY + metric_suffix
    response = requests.get(final_url)
    return response.json()


def get_hourly(city_key):
    final_url = ACCU_WEATHER_URL + "forecasts/v1/hourly/12hour/" + city_key + "?apikey=" + ACCU_WEATHER_KEY + metric_suffix
    response = requests.get(final_url)
    converted_json = json.loads(response.text)
    for obj in converted_json:
        obj['Temperature'] = obj['Temperature']['Value']
        obj['WeatherText'] = obj.pop('IconPhrase')

    return converted_json


def get_current(city_key):
    final_url = ACCU_WEATHER_URL + "currentconditions/v1/" + city_key + "?apikey=" + ACCU_WEATHER_KEY
    response = requests.get(final_url)
    converted_json = json.loads(response.text)
    converted_json[0]['Temperature'] = converted_json[0]['Temperature']['Metric']['Value']
    converted_json[0]['DateTime'] = converted_json[0].pop('LocalObservationDateTime')
    converted_json[0]['WeatherIcon'] = int(converted_json[0]['WeatherIcon'])
    converted_json[0]['HasPrecipitation'] = converted_json[0]['HasPrecipitation'] == 'True'

    return converted_json[0]


def get_city_key(query):
    final_url = ACCU_WEATHER_URL + "locations/v1/cities/autocomplete?apikey=" + ACCU_WEATHER_KEY + "&q=" + query
    response = requests.get(final_url)
    return response.json()


def get_city_wallpaper(city_name):
    final_url = UNSPLASH_URL + "query=" + city_name + "&count=1&orientation=landscape"
    response = requests.get(final_url)
    return response.json()
