import json
import os
from flask import Flask, jsonify, request, _request_ctx_stack
from flask_cors import cross_origin
from jose import jwt
from six.moves.urllib.request import urlopen
from functools import wraps
from dotenv import load_dotenv

from news.model.news import News, NewsSchema

load_dotenv()

domain = os.getenv("AUTH0_DOMAIN")
print(f"test env: {domain}")

mock_news = [
    {'title': 'Titulo teste', 'content': 'conteudo teste'},
    {'title': '2 Titutlo teste', 'content': '2 conteudo teste'}
]
# mock_news = [
#     News('Titulo teste', 'conteudo teste'),
#     News('2 Titutlo teste', '2 conteudo teste')
# ]

auth0_domain = os.getenv("AUTH0_DOMAIN")
api_audience = os.getenv("AUTH0_AUDIENCE")
algorithms = ["RS256"]

app = Flask(__name__)

# Error handler


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)

    if not auth:
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected"
            }, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description": "Authorization header must start with Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description": "Authorization header must be Bearer token"}, 401)

    token = parts[1]
    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        requires_scope (str): The scope required to access the resource
    """
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("score"):
        token_scopes = unverified_claims["scope"].split()
        for token_scope in token_scopes:
            if token_scope == required_scope:
                return True
    return False


def requires_auth(f):
    """Determines if the access token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://" + auth0_domain + "/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }

        if rsa_key:
            try:
                payload = jwt.decode(token, rsa_key, algorithms=algorithms,
                                     audience=api_audience, issuer="https://"+auth0_domain+"/")
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                "description": "incorrect claims, please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                "description": "unable to parse authentication token"}, 401)

            _request_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                         "description": "Unable to find appropriate key"}, 401)
    return decorated


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
    news = schema.dump(mock_news)
    print(news[0]['title'])
    return jsonify(news)


@app.route('/news', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def add_news():
    # mock_news.append(request.get_json())
    objPost = NewsSchema().load(request.get_json())
    mock_news.append(objPost)
    return '', 204
