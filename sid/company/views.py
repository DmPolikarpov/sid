from flask import Blueprint, render_template
from datetime import datetime
from sid.company.models import Company
from sid.share.models import Share



blueprint = Blueprint('company', __name__, url_prefix='/company')

@blueprint.route('/1')
@blueprint.route('/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    per_page = 10
    title = 'companies'
    company_list = Company.query.order_by(Company.id.desc()).paginate(page, per_page, error_out=False)
    return render_template('company/index.html', title=title, company_list=company_list)

@blueprint.route('/detail/<int:company_id>', methods=['GET'])
def company_detail(company_id):
    company = Company.query.get_or_404(company_id)
    date_now = datetime.now()
    one_year = datetime(date_now.year-1, date_now.month, date_now.day).date()
    five_year = datetime(date_now.year-5, date_now.month, date_now.day).date()
    one_year_shares = Share.query.filter_by(company_id=company_id).filter(Share.trading_date > one_year).all()
    five_year_shares = Share.query.filter_by(company_id=company_id).filter(Share.trading_date > five_year).all()
    if not one_year_shares:
        abort(404)
    if not five_year_shares:
        abort(404)
    return render_template('company/detail.html', company=company, one_year_shares=one_year_shares, five_year_shares=five_year_shares)