from sid import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    """ Модель пользователя. """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False) 
    password = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)
    role = db.Column(db.String(10), index=True, nullable=True)
    portfolios = db.relationship('Portfolio', backref='user_portfolios', lazy=True)

    def __repr__(self):
        return f'User {self.first_name} {self.last_name}'
        
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)