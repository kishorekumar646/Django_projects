import datetime

from register_page.settings import SECRET_KEY, AUTH_ENDPOINT
import jwt

from django.contrib.auth.tokens import PasswordResetTokenGenerator


def token_activation(username, password):
   

    data = {
        'username': username,
        'password': password,
        'exp': datetime.datetime.now()+datetime.timedelta(minutes=3)
    }
    token = jwt.encode(data, SECRET_KEY, algorithm="HS256").decode('utf-8')
    return token

