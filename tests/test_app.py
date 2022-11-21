import pytest
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask import session
from app.models import User

db = SQLAlchemy()


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

    context = app.app_context()
    context.push()

    db.init_app(app)

    db.create_all()

    yield app.test_client()
    db.session.remove()
    db.drop_all()
    context.pop()


def test_if_page_return_code_200(client):
    response = client.get('/')
    assert response.status_code == 200


def test_if_home_link_register_exist(client):
    response = client.get('/')
    assert 'Cadastrar-se' in response.get_data(as_text=True)


def test_if_home_link_login_exist(client):
    response = client.get('/')
    assert 'Login' in response.get_data(as_text=True)


def test_register_user(client):
    data = {
        'name': 'Test',
        'email': 'test@test.com',
        'password': 'test'
    }

    client.post(
        '/register',
        data=data, follow_redirects=True
    )

    users = User.query.filter_by(email=data['email'])

    assert users


def test_login_user(client):
    data = {
        'name': 'Test',
        'email': 'test@test.com',
        'password': 'test'
    }

    response = client.post(
        '/login',
        data=data, follow_redirects=True
    )

    assert data['email'] in response.get_data(as_text=True)
