from avw import db
from avw.models import User, load_user
from flask import Response, current_app
from jwt import encode
from time import time


def test_load_user(client, new_user: User):
    db.session.add(new_user)
    db.session.commit()

    assert load_user(1) == new_user
    assert load_user('1') == new_user
    assert load_user(2) is None
    assert load_user('2') is None
    assert load_user('fdsafskaj') is None
    assert load_user('') is None
    assert load_user('2\3sd') is None


def test_login_user(client):
    user = User('Susan', 'a@a.com', '12345')
    db.session.add(user)
    db.session.commit()

    rv: Response = client.post(
        '/login', data={'username': 'Susan', 'password': '12345'},
        follow_redirects=True)
    assert rv.status_code == 200

    db.session.delete(user)
    db.session.commit()

def test_password_reset(client):
    user = User('Susan', 'a@a.com', '12345')
    db.session.add(user)
    db.session.commit()

    t = user.get_reset_password_token()
    assert t is not None
    assert type(t) is str

    r_user = User.verify_reset_password_token(t)
    assert r_user == user

    db.session.delete(user)
    db.session.commit()


def test_password_reset_exp_time(client):
    user = User('Susan', 'a@a.com', '12345')
    db.session.add(user)
    db.session.commit()

    t1 = encode({'user_id': user.id, 'exp': time() - 10000},
                current_app.config.get('SECRET_KEY'), algorithm='HS256')
    t2 = user.get_reset_password_token()
    assert User.verify_reset_password_token(t1) is None
    assert User.verify_reset_password_token(t2) is not None
    assert User.verify_reset_password_token(t2) == user
