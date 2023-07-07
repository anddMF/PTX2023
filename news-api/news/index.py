from flask import Flask, jsonify, request

from news.model.news import News, NewsSchema

app = Flask(__name__)

mock_news = [
    {'title': 'Titulo teste', 'content': 'conteudo teste'},
    {'title': '2 Titutlo teste', 'content': '2 conteudo teste'}
]
# mock_news = [
#     News('Titulo teste', 'conteudo teste'),
#     News('2 Titutlo teste', '2 conteudo teste')
# ]

@app.route('/')
def get():
    return 'working'

@app.route('/news')
def get_news():
    schema = NewsSchema(many=True)
    news = schema.dump(mock_news)
    print(news[0]['title'])
    return jsonify(news)

@app.route('/news', methods=['POST'])
def add_news():
    # mock_news.append(request.get_json())
    objPost = NewsSchema().load(request.get_json())
    mock_news.append(objPost)
    return '', 204