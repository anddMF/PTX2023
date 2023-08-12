import requests
import os
from api.utils import add_route_param

NEWS_URL = os.getenv('MEDIASTACK_NEWS_URL') + os.getenv('MEDIASTACK_NEWS_KEY')


def get_news_mediastack(countries, categories, sources, sort, keywords):
    final_url = NEWS_URL

    excluded_sources = '-baystreet,-adital,-cinepop,-dgabc,-tutube,-r7,-alagoas24horas,-tnonline'

    if countries != '':
        final_url += '&countries=' + countries

    if categories != '':
        final_url += '&categories=' + categories
    
    final_url += f'&sources={excluded_sources}'
    if sources != '':
        final_url += ',' + sources

    if sort != '':
        final_url += f'&sort={sort}'

    if keywords != '':
        final_url += f'&keywords={keywords}'

    final_url += '&limit=30'

    response = requests.get(final_url)
    return response.json()
