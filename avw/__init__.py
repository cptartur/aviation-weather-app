from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)

    # if not app.testing:
    #     # continue setup
    #     pass

    # db.init_app(app)

    return app
