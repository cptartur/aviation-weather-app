import pytest
from avw import create_app, db
import avw
from avw.models import User
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

@pytest.fixture(scope='module')
def new_user() -> User:
    user = User('Joe', 'example@example.com', 'VerySecure')
    return user

@pytest.fixture(scope='module')
def client():
    app = create_app(TestConfig)
    
    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
            db.create_all()
            yield client


    
