from flask import Blueprint

bp = Blueprint('airport', __name__)

from avw.airport import routes
