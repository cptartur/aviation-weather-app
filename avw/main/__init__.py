from flask import Blueprint

bp = Blueprint('main', __name__)

from avw.main import routes