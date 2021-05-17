from flask.globals import request
from flask.helpers import url_for
from flask_wtf import form
from avw.search import search_airport
from avw.main.forms import SearchForm
from avw.main import bp
from flask import render_template, redirect, session
from flask_login import current_user


@bp.route('/', methods=('GET', 'POST'))
@bp.route('/index', methods=('GET', 'POST'))
def index():
    search_form = SearchForm()
    favorite_apts = None
    if current_user.is_authenticated:
        favorite_apts = current_user.get_favorite_airports()
    if search_form.validate_on_submit():
        return redirect(
            url_for('main.search', code=search_form.airport_name.data))
    return render_template('index.html', form=search_form,
                           recent_apts=session.get('recent_apts'),
                           favorite_apts=favorite_apts)


@bp.route('/search/<code>', methods=['GET'])
def search(code):
    results = search_airport(code)
    if results is not None:
        if 'recent_apts' not in session:
            session['recent_apts'] = [code]
        else:
            if code not in session['recent_apts']:
                if len(session['recent_apts']) >= 5:
                    session['recent_apts'] = session['recent_apts'][0:4]
                session['recent_apts'].insert(0, code)
                session.modified = True
        return render_template('search.html',
                               title=f'Search results for {code}',
                               results=results)
    return redirect(url_for('main.index'))
