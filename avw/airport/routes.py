from avw.airport import bp
from avw import db
from metar.metar import Metar
from flask_login import current_user
from flask import render_template, abort, url_for, redirect, request

m = Metar()


@bp.route('/airport/<code>', methods=('GET', 'POST'))
def airport(code):
    metar = m.get_metar(code)
    in_favorites = False
    preferences = {}

    if metar['errors'] is not None:
        abort(500)
    if current_user.is_authenticated:
        in_favorites = True if code in current_user.get_favorite_airports() \
            else False
        preferences = current_user.get_preferences()

    vis_unit = request.args.get('vis_unit')
    altim_unit = request.args.get('altim_unit')
    if vis_unit is not None:
        preferences.update({'vis_unit': vis_unit})
    if altim_unit is not None:
        preferences.update({'altim_unit': altim_unit})

    return render_template(
        'airport/airport.html', name=code, metar=metar,
        in_favorites=in_favorites, preferences=preferences)


@bp.route('/airport/add/<code>', methods=['GET'])
def add(code):
    if current_user.is_authenticated:
        current_user.add_airport_to_favorites(code)
        db.session.commit()
        next = request.args.get('next')
        if next is None:
            return redirect(url_for('main.index'))
        return redirect(next)
    return redirect(url_for('main.index'))


@bp.route('/airport/remove/<code>', methods=['GET'])
def remove(code):
    if current_user.is_authenticated:
        current_user.remove_airport_from_favorites(code)
        db.session.commit()
        next = request.args.get('next')
        if next is None:
            return redirect(url_for('main.index'))
        return redirect(next)
    return redirect(url_for('main.index'))
