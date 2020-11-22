from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Aдрес электронной почты', validators=[DataRequired(), Email()], render_kw={"class": "login-form-control", "placeholder": 'Впишите адрес e-mail'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "login-form-control", "placeholder": 'Введите пароль'})
    remember_me = BooleanField('Запомнить меня', default = True, render_kw={"class":"login-form-check-input"})
    submit = SubmitField('Войти', render_kw={"class": "login-form-control"})