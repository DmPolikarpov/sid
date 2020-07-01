from sid.db import db

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