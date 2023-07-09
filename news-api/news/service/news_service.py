import requests
import os

NEWS_URL = os.getenv('NEWS_IO_URL')
NEWS_KEY = os.getenv('NEWS_IO_KEY')

url = NEWS_URL + NEWS_KEY


def get_news_io(countries, categories):
    countries = countries.split(',')
    categories = categories.split(',')
    final_url = url
    if countries:
        final_url = final_url + '&country=' + countries[0]
        del countries[0]
        for country in countries:
            final_url = final_url + ',' + country

    if categories:
        final_url = final_url + '&category=' + categories[0]
        del categories[0]
        for category in categories:
            final_url = final_url + ',' + category

    response = requests.get(final_url)
    return response.json()
