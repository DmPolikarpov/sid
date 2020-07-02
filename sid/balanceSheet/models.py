from sid.db import db

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