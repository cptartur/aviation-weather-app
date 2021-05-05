from avw import db


class User(db.Model):
    username = db.Column(db.String(64), primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    preferences = db.Column(db.JSON())
    favorite_airports = db.Column(db.JSON())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = password
        self.preferences = {}
        self.favorite_airports = []

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
            self.favorite_airports.append(airport)

    def remove_airport_from_favorites(self, airport: str) -> None:
        if airport in self.favorite_airports:
            self.favorite_airports.remove(airport)

    def get_favorite_airports(self) -> list:
        return self.favorite_airports

    def update_preferences(self, preferences: dict) -> None:
        self.preferences.update(preferences)

    def get_preferences(self) -> dict:
        return self.preferences
