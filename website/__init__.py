from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Green Bean"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Importing auth, views routes to __init__
    from .auth import auth
    from .views import views

    # Registering the auth, views blueprint for the 'app' to utilize
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    from .models import User, Post, Comment, Like

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # Uses 'sessions' to store the user information to remember it for later
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
