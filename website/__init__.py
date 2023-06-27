from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Green Bean"

    # Importing auth, views routes to __init__
    from .auth import auth
    from .views import views

    # Registering the auth, views blueprint for the 'app' to utilize
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    return app
