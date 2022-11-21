from .models import User
from flask import render_template
from flask_login import current_user, login_required

from .auth import auth as auth_bp
from .book import book as book_bp
from .account import account as account_bp


def app_init(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(account_bp)

    @app.route('/')
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)
