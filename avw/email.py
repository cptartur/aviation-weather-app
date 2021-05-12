from avw.models import User
from flask import current_app, render_template
from flask_mailman import EmailMessage

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
    with current_app.app_context():
        msg.send()