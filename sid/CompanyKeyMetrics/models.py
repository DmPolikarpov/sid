from sid.db import db

class Company_key_metrics(db.Model):
    """the model to describe key metrics of some company"""
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    market_cap = db.Column(db.Numeric, nullable = True)
    pe_ratio = db.Column(db.Numeric, nullable = True)
    price_to_sales_ratio = db.Column(db.Numeric, nullable = True)
    ptb_ratio = db.Column(db.Numeric, nullable = True)
    enterprise_value_over_ebitda = db.Column(db.Numeric, nullable = True)
    ev_to_operating_cash_flow = db.Column(db.Numeric, nullable = True)
    net_debt_to_ebitda = db.Column(db.Numeric, nullable = True)
    roe = db.Column(db.Numeric, nullable = True)

    def __repr__(self):
        return f'Company key metrics {self.company_id}'