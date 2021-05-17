from avw import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from jwt import decode, encode
from time import time
from copy import deepcopy
from flask import current_app


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    preferences = db.Column(db.JSON())
    favorite_airports = db.Column(db.JSON())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.preferences = {}
        self.favorite_airports = []
        self.set_password(password=password)

    def __repr__(self):
        return f"<User {self.username}>"

    @staticmethod
    def hash_password(password) -> str:
        return generate_password_hash(password=password)

    def set_password(self, password) -> None:
        self.password_hash = User.hash_password(password=password)

    def validate_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def set_email(self, mail: str) -> None:
        self.email = mail

    def set_nickname(self, nickname: str) -> None:
        self.username = nickname

    def add_airport_to_favorites(self, airport: str) -> None:
        if airport not in self.favorite_airports:
            fav = deepcopy(self.favorite_airports)
            fav.append(airport)
            self.favorite_airports = fav

    def remove_airport_from_favorites(self, airport: str) -> None:
        if airport in self.favorite_airports:
            fav = deepcopy(self.favorite_airports)
            fav.remove(airport)
            self.favorite_airports = fav

    def get_favorite_airports(self) -> list:
        return self.favorite_airports

    def update_preferences(self, preferences: dict) -> None:
        pref = deepcopy(self.preferences)
        pref.update(preferences)
        self.preferences = pref

    def get_preferences(self) -> dict:
        return self.preferences

    def get_reset_password_token(self, exp=600) -> str:
        token = encode({'user_id': self.id, 'exp': time() + exp},
                       current_app.config.get('SECRET_KEY'), algorithm='HS256')
        return token
    
    @staticmethod
    def verify_reset_password_token(token):
        try:
            token = decode(token, current_app.config.get('SECRET_KEY'), algorithms='HS256')
        except:
            return None
        else:
            return User.query.get(token.get('user_id'))


@login_manager.user_loader
def load_user(id):
    try:
        return User.query.get(int(id))
    except ValueError:
        return None
