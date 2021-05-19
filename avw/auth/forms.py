from avw.models import User
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)


class RegisterForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), Length(min=1, max=32)]
    )
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'confirm password',
        validators=(
            DataRequired(),
            EqualTo('password', message='Passwords must be equal'),
        ),
    )

    def validate_username(form, field):
        if len(User.query.filter_by(username=field.data).all()) != 0:
            raise ValidationError('Username already in use')

    def validate_email(form, field):
        if len(User.query.filter_by(email=field.data).all()) != 0:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class ResetPasswordForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])


class SetNewPasswordForm(FlaskForm):
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'confirm password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must be equal')
        ]
    )
