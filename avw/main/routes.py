from flask.globals import request
from flask.helpers import url_for
from flask_wtf import form
from avw.search import search_airport
from avw.main.forms import SearchForm
from avw.main import bp
from flask import render_template, redirect
from metar.metar import Metar

m = Metar()

@bp.route('/', methods=('GET', 'POST'))
@bp.route('/index', methods=('GET', 'POST'))
def index():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        return redirect(url_for('main.search', code=search_form.airport_name.data))
    return render_template('index.html', form=search_form)


@bp.route('/search/<code>', methods=['GET'])
def search(code):
    results = search_airport(code)
    if results is not None:
        return render_template('search.html',
                               title=f'Search results for {code}',
                               results=results)
    return redirect(url_for('main.index'))


@bp.route('/airport/<code>')
def airport(code):
    return m.get_metar(code)
