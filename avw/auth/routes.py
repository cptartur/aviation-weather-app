from flask_login.utils import logout_user
from avw.models import User
from avw.auth.forms import LoginForm, RegisterForm
from avw.auth import bp
from avw import db
from flask import flash, redirect, url_for, render_template, request
from flask_login import current_user, login_user


@bp.route('/login', methods=('POST', 'GET'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.validate_password(form.password.data):
            login_user(user)
            flash(f'Succesfully logged in user {user}')
            next = request.args.get('next', 'main.index')
            return redirect(url_for(next))
        return redirect('auth.login')
    return render_template('auth/login.html', title='Login', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=('POST', 'GET'))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash(f'Succesfully registered user {user}')
        return redirect(url_for('auth.login'))
    else:
        print('errorrrr')
    return render_template('auth/register.html', title='Register', form=form)
