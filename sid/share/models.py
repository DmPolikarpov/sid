from sid.db import db
from sqlalchemy.orm import relationship

class Share(db.Model):
    """the model to save data of the shares of different companies"""
    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    trading_date = db.Column(db.Date, nullable=False)
    open_price = db.Column(db.Numeric, nullable=False)
    high_price = db.Column(db.Numeric, nullable=False)
    low_price = db.Column(db.Numeric, nullable=False)
    close_price = db.Column(db.Numeric, nullable=False)
    volume = db.Column(db.Numeric, nullable=False)
    dividends = db.Column(db.Numeric, nullable=True)
    stock_split = db.Column(db.Numeric, nullable=True)

    def __repr__(self):
        return f'Share {self.name}'