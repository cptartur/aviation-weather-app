from flask_login.utils import logout_user
from avw.models import User
from avw.auth.forms import (LoginForm, RegisterForm, ResetPasswordForm,
                            SetNewPasswordForm)
from avw.auth import bp
from avw.email import send_reset_password_email
from avw import db
from flask import flash, redirect, url_for, render_template, request
from flask_login import current_user, login_user


@bp.route('/login', methods=('POST', 'GET'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.validate_password(form.password.data):
            login_user(user)
            flash(f'Succesfully logged in user {user}')
            next = request.args.get('next', 'main.index')
            return redirect(url_for(next))
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html', title='Login', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=('POST', 'GET'))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm(request.form)
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


@bp.route('/request_password_reset', methods=('POST', 'GET'))
def request_password_reset():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm(request.form)
    if form.validate_on_submit():
        send_reset_password_email(form.email.data)
        flash('Password reset email sent')
        return redirect(url_for('auth.login'))
    return render_template('auth/request_password_reset.html',
                           title='Reset Password', form=form)


@bp.route('/reset_password/<token>', methods=('POST', 'GET'))
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user: User = User.verify_reset_password_token(token)
    if user is None:
        flash('Invalid user')
        return redirect(url_for('main.index'))
    form = SetNewPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('New password has been set')
        return redirect(url_for('main.index'))
    return render_template(
        '/auth/reset_password.html', title='Reset password', form=form)
