from sid.db import db
from sid.share.models import Share
from sid.CompanyKeyMetrics.models import Company_key_metrics
from sid.balanceSheet.models import Balance_sheet
from sid.cashFlow.models import Cash_flow
from sqlalchemy.orm import relationship

class Company(db.Model):
    """the model to describe some company"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    industry_id = db.Column(db.Integer, db.ForeignKey('industry.id'), nullable=True)
    ticker = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    description = db.Column(db.Text, nullable=True)
    logo = db.Column(db.String, nullable=True)
    website = db.Column(db.String, nullable=True)
    exchange = db.Column(db.String, nullable=True)
    exchange_short_name = db.Column(db.String, nullable=True)
    shares = db.relationship('Share', backref='shares', lazy=True)
    key_metrics = db.relationship('Company_key_metrics', backref='key_metrics', lazy=True)
    balance_sheet = db.relationship('Balance_sheet', backref='company_balance_sheet', lazy=True)
    cash_flow = db.relationship('Cash_flow', backref='company_cash_flow', lazy=True)

    def __repr__(self):
        return f'Company {self.name}'