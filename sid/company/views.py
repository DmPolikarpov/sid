from flask import Blueprint, render_template
from datetime import datetime, timedelta
from sid.company.models import Company
from sid.share.models import Share
from sid.CompanyKeyMetrics.models import Company_key_metrics


blueprint = Blueprint('company', __name__, url_prefix='/company')

@blueprint.route('/1')
@blueprint.route('/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    per_page = 15
    title = 'companies'
    company_list = Company.query.order_by(Company.id.desc()).paginate(page, per_page, error_out=False)
    return render_template('company/index.html', title=title, company_list=company_list)

@blueprint.route('/detail/<int:company_id>', methods=['GET'])
def company_detail(company_id):
    company = Company.query.get_or_404(company_id)
    date_now = datetime.now()
    one_month = (date_now - timedelta(days=30)).date()
    six_months = (date_now - timedelta(days=182)).date()
    one_year = datetime(date_now.year-1, date_now.month, date_now.day).date()
    five_years = datetime(date_now.year-5, date_now.month, date_now.day).date()
    ten_years = datetime(date_now.year-10, date_now.month, date_now.day).date()
    last_year = datetime.strptime('2019-12-31', '%Y-%m-%d').date()
    shares = Share.query.filter_by(company_id=company_id).all()
    if not shares:
        abort(404)
    keyMetrics = Company_key_metrics.query.filter_by(company_id=company_id).filter_by(date=last_year).all()
    if not keyMetrics:
        abort(404)
    return render_template('company/detail.html',
                            company = company,
                            one_month = one_month,
                            six_months = six_months,
                            one_year = one_year,
                            five_years = five_years,
                            ten_years = ten_years,
                            shares = shares,
                            keyMetrics = keyMetrics
                            )