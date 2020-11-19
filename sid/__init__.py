from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from sid.db import db


from sid.company.views import blueprint as company_blueprint
from sid.country.views import blueprint as country_blueprint
from sid.industry.views import blueprint as industry_blueprint
from sid.share.views import blueprint as share_blueprint
from sid.cashFlow.views import blueprint as cashflow_blueprint
from sid.balanceSheet.views import blueprint as balancesheet_blueprint
from sid.user.views import blueprint as user_blueprint



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    app.register_blueprint(company_blueprint)
    app.register_blueprint(country_blueprint)
    app.register_blueprint(industry_blueprint)
    app.register_blueprint(share_blueprint)
    app.register_blueprint(cashflow_blueprint)
    app.register_blueprint(balancesheet_blueprint)
    app.register_blueprint(user_blueprint)

    @app.route('/')
    def index():
        title = "Smart invest decision"
        return render_template('index.html', page_title=title)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app

