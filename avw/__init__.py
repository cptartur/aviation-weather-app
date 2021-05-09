from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mailman import Mail
from config import Config


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

    from avw.main import bp as main_bp
    app.register_blueprint(main_bp)

    from avw.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    return app

from avw import models