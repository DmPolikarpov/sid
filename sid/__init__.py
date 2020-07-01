from flask import Flask, render_template
from sid.db import db

from sid.company.views import blueprint as company_blueprint
from sid.country.views import blueprint as country_blueprint
from sid.industry.views import blueprint as industry_blueprint
from sid.share.views import blueprint as share_blueprint
from sid.cashFlow.views import blueprint as cashflow_blueprint
from sid.balanceSheet.views import blueprint as balancesheet_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    app.register_blueprint(company_blueprint)
    app.register_blueprint(country_blueprint)
    app.register_blueprint(industry_blueprint)
    app.register_blueprint(share_blueprint)
    app.register_blueprint(cashflow_blueprint)
    app.register_blueprint(balancesheet_blueprint)

    @app.route('/')
    def index():
        title = "Smart invest decision"
        return render_template('index.html', page_title=title)
    return app

