from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    login = StringField("Логин (email)")
    password = PasswordField("Пароль")
    confirm_password = PasswordField("Повтор пароля")
    nickname = StringField("Название аккаунта")
    submit = SubmitField("Отправить")


class LoginForm(FlaskForm):
    login = StringField("Логин (email)")
    password = PasswordField("Пароль")
    remember = BooleanField("Запомнить в системе", default=False)
    submit = SubmitField("Войти")


class PasswordRecoveryForm(FlaskForm):
    login = StringField("Логин (email)")
    submit = SubmitField("Войти")
