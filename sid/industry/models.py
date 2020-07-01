from sid.db import db
from sid.company.models import Company
from sqlalchemy.orm import relationship

class Industry(db.Model):
    """the model to describe some industry"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    description = db.Column(db.Text, nullable=True)
    related_companies = db.relationship('Company', backref='industry_companies',lazy=True)

    def __repr__(self):
        return f'Industry {self.name}'