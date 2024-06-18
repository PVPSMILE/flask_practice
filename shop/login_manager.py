import flask_login
from registration_page.models import User
from .settings import shop
from authorization_page import show_login

shop.secret_key = 'Задайте секретний ключ'
login_manager = flask_login.LoginManager(shop)

login_manager.login_view = 'show_login'

@login_manager.user_loader

def load_user(id):
    return User.query.get(id)

