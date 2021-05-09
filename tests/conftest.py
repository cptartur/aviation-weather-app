import pytest
from avw import create_app, db
from avw.models import User
from config import Config

class TestConfig(Config):
    SECRET_KEY = 'debug_key'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False

@pytest.fixture(scope='function')
def new_user() -> User:
    user = User('Joe', 'example@example.com', 'VerySecure')
    return user

@pytest.fixture(scope='function')
def client():
    app = create_app(TestConfig)
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
