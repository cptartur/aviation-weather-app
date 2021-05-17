from avw.airport import bp
from avw import db
from metar.metar import Metar
from flask_login import current_user
from flask import render_template, abort, url_for, redirect, request

m = Metar()


@bp.route('/airport/<code>', methods=('GET', 'POST'))
def airport(code):
    metar = m.get_metar(code)
    if metar['errors'] is not None:
        abort(500)
    if current_user.is_authenticated:
        in_favorites = True if code in current_user.get_favorite_airports() \
            else False
    return render_template(
        'airport/airport.html', name=code, metar=metar,
        in_favorites=in_favorites)

