from dotenv import load_dotenv
load_dotenv()

from api.model.auth_error import AuthError
from api.model.news import News, NewsSchema
from functools import wraps
from six.moves.urllib.request import urlopen
from api.service.auth_service import requires_auth
import api.service.weather_service as weather_svc
from api.service.news_service import get_news_io
from api.model.weather_daily import WeatherDailySchema
from api.model.weather_city import WeatherCitySchema
from jose import jwt
from flask_cors import cross_origin
from flask import Flask, jsonify, request, _request_ctx_stack
import os
import json


mock_news = [
    {'title': 'Titulo teste', 'content': 'conteudo teste'},
    {'title': '2 Titutlo teste', 'content': '2 conteudo teste'}
]

app = Flask(__name__)


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


@app.route('/ping')
@cross_origin(headers=["Content-Type", "Authorization"])
def ping():
    response = 'Ok'
    return jsonify(message=response)


@app.route('/news')
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_news():
    schema = NewsSchema(many=True)
    categories = request.args.get('categories')
    countries = request.args.get('countries')
    res = get_news_io(countries, categories)
    news = schema.dump(res['results'])
    return jsonify(news)


@app.route('/news', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def add_news():
    objPost = NewsSchema().load(request.get_json())
    mock_news.append(objPost)
    return '', 204


@app.route('/weather/daily', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_daily_weather():
    schema = WeatherDailySchema(many=True)
    city_key = request.args.get('citykey')
    if city_key == None or city_key == '':
        return '', 400
    raw_response = weather_svc.get_daily(city_key)
    response = schema.dump(raw_response['DailyForecasts'])
    return jsonify(response)

@app.route('/weather/city', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_city_key():
    schema = WeatherCitySchema(many=True)
    query = request.args.get('q')
    if query == None or query == '':
        return '', 400
    raw_response = weather_svc.get_city_key(query)
    response = schema.dump(raw_response)
    return jsonify(response)