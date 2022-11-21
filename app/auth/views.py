import sys  # noqa: ignore=F401 isort:skip
sys.path.append('.')  # noqa: ignore=F401 isort:skip

from app import db
from app.forms import LoginForm, RegisterForm
from app.models import User
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import auth


@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        form = dict(
            name=form.name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )

        user = User(**form)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))
    context = {
        'form': form
    }

    return render_template('register.html', **context)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Email not found.', 'warning')

        elif not check_password_hash(user.password, password):
            flash('Invalid password.', 'danger')
        else:
            login_user(user, remember)
            return redirect(url_for('index'))

    context = {
        'form': form
    }

    return render_template('login.html', **context)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
