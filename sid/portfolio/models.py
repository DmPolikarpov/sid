from sid import db
from sid.user.models import User
from datetime import datetime

class Portfolio(db.Model):
    """ Модель отзыва на книгу. """
    id = db.Column(db.Integer, primary_key=True)
    portfolio_name = db.Column(db.String, nullable=False )
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    added = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return f'Portfolio {self.portfolio_name}'