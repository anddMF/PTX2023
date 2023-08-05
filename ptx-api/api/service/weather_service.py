import requests
import os

ACCU_WEATHER_URL = os.getenv('ACCU_WEATHER_URL')
ACCU_WEATHER_KEY = os.getenv('ACCU_WEATHER_KEY')

metric_suffix = "&metric=true"

def get_daily(city_key):
    if city_key == "":
        return None

    final_url = ACCU_WEATHER_URL + "forecasts/v1/daily/5day/" + city_key + "?apikey=" + ACCU_WEATHER_KEY + metric_suffix
    response = requests.get(final_url)
    return response.json()

# def get_city_key