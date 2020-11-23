from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from sid.user.models import User

class LoginForm(FlaskForm):
    email = StringField('Aдрес электронной почты', validators=[DataRequired(), Email()], render_kw={"class": "login-form-control", "placeholder": 'Впишите адрес e-mail'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "login-form-control", "placeholder": 'Введите пароль'})
    remember_me = BooleanField('Запомнить меня', default = True, render_kw={"class":"login-form-check-input"})
    submit = SubmitField('Войти', render_kw={"class": "login-form-control"})

class RegistrationForm(FlaskForm):
    first_name = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class":"registration-form-control", "placeholder":"Введите свое имя"})
    last_name = StringField('Фамилия пользователя', validators=[DataRequired()], render_kw={"class":"registration-form-control", "placeholder":"Введите свою фамилию"})
    email = StringField('Адрес электронной почты', validators=[DataRequired(), Email()], render_kw={"class":"registration-form-control", "placeholder": "Впишите адрес e-mail"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "registration-form-control", "placeholder": 'Введите пароль'})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "registration-form-control", "placeholder": 'Повторите пароль'})
    submit = SubmitField('Отправить', render_kw={"class": "registration-form-control"})

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован')