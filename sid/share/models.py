from sid.db import db
from sqlalchemy.orm import relationship

class Share(db.Model):
    """the model to save data of the shares of different companies"""
    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    lot = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return f'Share {self.name}'