from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    # if not app.testing:
    #     # continue setup
    #     pass
    db.init_app(app)

    from avw.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from avw import models