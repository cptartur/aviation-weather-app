from flask.globals import request
from flask.helpers import url_for
from flask_wtf import form
from avw.main.forms import SearchForm
from flask import render_template, redirect
from avw.main import bp
from metar.metar import Metar

m = Metar()

@bp.route('/', methods=('GET', 'POST'))
@bp.route('/index', methods=('GET', 'POST'))
def index():
    search_form = SearchForm()
    if request.method == 'POST' and search_form.validate_on_submit():
        return redirect(url_for('main.airport', code=search_form.airport_name.data))
    return render_template('index.html', form=search_form)

@bp.route('/airport/<code>')
def airport(code):
    return m.get_metar(code)