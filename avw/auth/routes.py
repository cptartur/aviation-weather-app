from avw.models import User
from avw.auth.forms import RegisterForm
from avw.auth import bp
from avw import db
from flask import flash, redirect, url_for, render_template
from flask_login import current_user


@bp.route("/register", methods=("POST", "GET"))
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
        flash(f"Succesfully registered user {user}")
        return redirect(url_for("auth.login"))
    else:
        print('errorrrr')
    return render_template("auth/register.html", title="Register", form=form)
