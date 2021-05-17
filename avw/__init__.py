from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mailman import Mail
from config import Config
from elasticsearch import Elasticsearch


db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    # if not app.testing:
    #     # continue setup
    #     pass
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    es_url = app.config.get('ELASTICSEARCH_URL')
    if es_url is not None:
        app.elasticsearch = Elasticsearch(es_url)

    from avw.main import bp as main_bp
    app.register_blueprint(main_bp)

    from avw.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from avw.airport import bp as airport_bp
    app.register_blueprint(airport_bp)
    
    return app

from avw import models