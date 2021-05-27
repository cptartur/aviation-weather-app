from avw.errors import bp
from flask import render_template, current_app
from os import environ


@bp.app_errorhandler(404)
def not_found_error(error):
    img = environ.get('ERROR_IMG')
    return render_template('404.html', img=img), 404


@bp.app_errorhandler(500)
def internal_server_error(error):
    img = environ.get('ERROR_IMG')
    return render_template('500.html', img=img), 500


@bp.route('/476', methods=('GET',))
def no_metar_for_this_airport_error():
    img = environ.get('476_IMG')
    return render_template('476.html', img=img), 476
