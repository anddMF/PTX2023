import requests
import os

WEATHER_URL = os.getenv('ACCU_WEATHER_URL')
WEATHER_KEY = os.getenv('ACCU_WEATHER_KEY')

url = WEATHER_URL + WEATHER_KEY

# def get_hourly(city_key):
    # if city_key


# def get_city_key