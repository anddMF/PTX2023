import requests
import os
from api.utils import add_route_param

NEWS_URL = os.getenv('MEDIASTACK_NEWS_URL') + os.getenv('MEDIASTACK_NEWS_KEY')


def get_news_mediastack(countries, categories, sources, sort, keywords):
    countries = countries.split(',')
    categories = categories.split(',')
    sources = sources.split(',')
    final_url = NEWS_URL

    if countries:
        final_url = add_route_param(countries, 'countries', final_url)

    if categories:
        final_url = add_route_param(categories, 'categories', final_url)

    if sources:
        final_url = add_route_param(sources, 'sources', final_url)

    if sort != '':
        final_url += f'&sort={sort}'

    if keywords != '':
        final_url += f'&keywords={keywords}'

    final_url += '&limit=30'

    response = requests.get(final_url)
    return response.json()
