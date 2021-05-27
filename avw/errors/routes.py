from avw.errors import bp
from flask import render_template


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@bp.app_errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@bp.route('/476', methods=('GET',))
def no_metar_for_this_airport_error():
    return render_template('476.html'), 476
