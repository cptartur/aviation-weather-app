from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired(), Length(min=1, max=32)]
    )
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "confirm password",
        validators=(
            DataRequired(),
            EqualTo('password', message="Passwords must be equal"),
        ),
    )
