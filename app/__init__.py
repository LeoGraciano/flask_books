import sys  # noqa: ignore=F401 isort:skip
sys.path.append('.')  # noqa: ignore=F401 isort:skip

import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(ROOT_DIR, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Bootstrap5(app)
    login_manager.init_app(app)

    db.init_app(app)
    with app.app_context():
        db.create_all(bind_key='__all__')

    from . import routes

    routes.app_init(app)

    return app
