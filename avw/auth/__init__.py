from flask import Blueprint

bp = Blueprint('auth', __name__)

from avw.auth import routes
