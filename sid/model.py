from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Country(db.Model):
    """the model to describe some country"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    industries = db.relationship('Industry', backref='country_industries',lazy=True)
    companies = db.relationship('Company', backref='contry_companies', lazy=True)

    def __repr__(self):
        return f'Country {self.name}'

class Industry(db.Model):
    """the model to describe some industry"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    description = db.Column(db.Text, nullable=True)
    related_companies = db.relationship('Company', backref='industry_companies',lazy=True)

    def __repr__(self):
        return f'Industry {self.name}'

class Company(db.Model):
    """the model to describe some company"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    industry_id = db.Column(db.Integer, db.ForeignKey('industry.id'), nullable=True)
    ticker = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    decription = db.Column(db.Text, nullable=True)
    logo = db.Column(db.String, nullable=True)
    website = db.Column(db.String, nullable=True)
    shares = db.relationship('Share', backref='shares', lazy=True)
    balance_sheet = db.relationship('Balance_sheet', backref='company_balance_sheet', lazy=True)
    cash_flow = db.relationship('Cash_flow', backref='company_cash_flow', lazy=True)

    def __repr__(self):
        return f'Company {self.name}'

class Balance_sheet(db.Model):
    """the model to save the data of the balance sheet statements"""
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    cash_and_cash_equivalents = db.Column(db.Numeric, nullable = True)
    short_term_investments = db.Column(db.Numeric, nullable = True)
    net_receivables = db.Column(db.Numeric, nullable = True)
    inventory = db.Column(db.Numeric, nullable = True)
    other_current_assets = db.Column(db.Numeric, nullable = True)
    total_current_assets = db.Column(db.Numeric, nullable = True)
    property_plant_equipment_net = db.Column(db.Numeric, nullable = True)
    goodwill = db.Column(db.Numeric, nullable = True)
    intangible_assets = db.Column(db.Numeric, nullable = True)
    long_term_investments = db.Column(db.Numeric, nullable = True)
    tax_assets = db.Column(db.Numeric, nullable = True)
    other_non_current_assets = db.Column(db.Numeric, nullable = True)
    total_non_current_assets = db.Column(db.Numeric, nullable = True)
    other_assets = db.Column(db.Numeric, nullable = True)
    total_assets = db.Column(db.Numeric, nullable = True)
    account_payables = db.Column(db.Numeric, nullable = True)
    short_term_debt = db.Column(db.Numeric, nullable = True)
    tax_payables = db.Column(db.Numeric, nullable = True)
    deffered_revenue = db.Column(db.Numeric, nullable = True)
    other_current_liabilities = db.Column(db.Numeric, nullable = True)
    total_current_liabilities = db.Column(db.Numeric, nullable = True)
    long_term_debt = db.Column(db.Numeric, nullable = True)
    deferred_revenue_non_current = db.Column(db.Numeric, nullable = True)
    deferred_tax_liabilities_non_current = db.Column(db.Numeric, nullable = True)
    other_non_current_liabilities = db.Column(db.Numeric, nullable = True)
    total_non_current_liabilities = db.Column(db.Numeric, nullable = True)
    other_liabilities = db.Column(db.Numeric, nullable = True)
    total_liabilities = db.Column(db.Numeric, nullable = True)
    common_stock = db.Column(db.Numeric, nullable = True)
    retained_earnings = db.Column(db.Numeric, nullable = True)
    accumulated_other_comprehensive_income_loss = db.Column(db.Numeric, nullable = True)
    other_total_stockholders_equity = db.Column(db.Numeric, nullable = True)
    total_stockholders_equity = db.Column(db.Numeric, nullable = True)
    total_liabilities_and_stockholders_equity = db.Column(db.Numeric, nullable = True)
    total_investments = db.Column(db.Numeric, nullable = True)
    total_debt = db.Column(db.Numeric, nullable = True)
    net_debt = db.Column(db.Numeric, nullable = True)

    def __repr__(self):
        return f'Balance sheet {self.name}'

class Cash_flow(db.Model):
    """the model to save data of the cash flow statements"""
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    net_income = db.Column(db.Numeric, nullable = True)
    depreciation_and_amortization = db.Column(db.Numeric, nullable = True)
    deferred_income_tax = db.Column(db.Numeric, nullable = True)
    stock_based_compensation = db.Column(db.Numeric, nullable = True)
    change_in_working_capital = db.Column(db.Numeric, nullable = True)
    accounts_receivables = db.Column(db.Numeric, nullable = True)
    other_working_capital = db.Column(db.Numeric, nullable = True)
    other_non_cash_items = db.Column(db.Numeric, nullable = True)
    net_cash_provided_by_operating_activities = db.Column(db.Numeric, nullable = True)
    investments_in_property_plant_and_equipment = db.Column(db.Numeric, nullable = True)
    acquisitions_net = db.Column(db.Numeric, nullable = True)
    purchases_of_investments = db.Column(db.Numeric, nullable = True)
    other_investing_activites = db.Column(db.Numeric, nullable = True)
    net_cash_used_for_investing_activities = db.Column(db.Numeric, nullable = True)
    debt_repayment = db.Column(db.Numeric, nullable = True)
    common_stock_issued = db.Column(db.Numeric, nullable = True)
    common_stock_repurchased = db.Column(db.Numeric, nullable = True)
    dividents_paid = db.Column(db.Numeric, nullable = True)
    other_financing_activites = db.Column(db.Numeric, nullable = True)
    net_cash_used_provided_by_financing_activities = db.Column(db.Numeric, nullable = True)
    effect_of_forex_changes_on_cash = db.Column(db.Numeric, nullable = True)
    net_change_in_cash = db.Column(db.Numeric, nullable = True)
    cash_at_end_of_period = db.Column(db.Numeric, nullable = True)
    cash_at_beginnig_period = db.Column(db.Numeric, nullable = True)
    operating_cash_flow = db.Column(db.Numeric, nullable = True)
    capital_expenditure = db.Column(db.Numeric, nullable = True)
    free_cash_flow = db.Column(db.Numeric, nullable = True)

    def __repr__(self):
        return f'Cash flow {self.name}'

class Share(db.Model):
    """the model to save data of the shares of different companies"""
    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    lot = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return f'Share {self.name}'