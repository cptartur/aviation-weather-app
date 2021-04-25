from avw import db


class User(db.Model):
    username = db.Column(db.String(64), primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    preferences = db.Column(db.JSON())
    favorite_airports = db.Column(db.JSON())

    def __init__(self, username, email, password):
        return

    def __repr__(self):
        return f"<User {self.username}>"

    @staticmethod
    def hash_password(self) -> str:
        return

    def set_password(self) -> None:
        return

    def validate_password(self, password: str) -> bool:
        return

    def set_email(self, mail: str) -> None:
        return

    def set_nickname(self, nickname: str) -> None:
        return

    def add_airport_to_favorites(self, airport: str) -> None:
        return

    def remove_airport_from_favorites(self, airport: str) -> None:
        return

    def get_favorite_airports(self) -> dict:
        return

    def update_preferences(self, preferences: dict) -> None:
        return

    def get_preferences(self) -> dict:
        return
