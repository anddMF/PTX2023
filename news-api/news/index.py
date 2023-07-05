from flask import Flask, jsonify, request

app = Flask(__name__)

mock_news = [
    { 'title': 'TESTE', 'content': 'content test'}
]

@app.route('/')
def get():
    return 'working'

@app.route('/news')
def get_news():
    return jsonify(mock_news)

@app.route('/news', methods=['POST'])
def add_news():
    mock_news.append(request.get_json())
    return '', 204