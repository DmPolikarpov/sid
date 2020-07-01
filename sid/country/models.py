from sid.db import db
from sid.industry.models import Industry
from sid.company.models import Company
from sqlalchemy.orm import relationship

class Country(db.Model):
    """the model to describe some country"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    industries = db.relationship('Industry', backref='country_industries',lazy=True)
    companies = db.relationship('Company', backref='contry_companies', lazy=True)

    def __repr__(self):
        return f'Country {self.name}'