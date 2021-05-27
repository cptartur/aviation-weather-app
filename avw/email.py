from avw.models import User
from flask import current_app, render_template
from flask_mailman import EmailMessage
from threading import Thread


def send_reset_password_email(email: str) -> None:
    user = User.query.filter_by(email=email).first()
    if user is None:
        return
    token = user.get_reset_password_token()
    msg = EmailMessage(
        subject='Reset your password',
        to=[email],
        from_email='noreply@example.com',
        body=render_template('mail/reset_password.html', token=token)
    )
    Thread(target=send_email, args=[
           current_app._get_current_object(), msg]).start()


def send_email(app_object, email: EmailMessage):
    with app_object.app_context():
        email.send()
