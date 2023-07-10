import json
import os
from flask import Flask, jsonify, request, _request_ctx_stack
from flask_cors import cross_origin
from jose import jwt
from news.service.news_service import get_news_io
from news.service.auth_service import requires_auth
from six.moves.urllib.request import urlopen
from functools import wraps
from dotenv import load_dotenv

from news.model.news import News, NewsSchema
from news.model.auth_error import AuthError

load_dotenv()

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
