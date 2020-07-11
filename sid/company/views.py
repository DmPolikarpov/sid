from flask import Blueprint, render_template
from sid.company.models import Company



blueprint = Blueprint('company', __name__, url_prefix='/company')

@blueprint.route('/')
def index():
    title = 'companies'
    company_list = Company.query.order_by(Company.id.desc()).all()
    return render_template('company/index.html', title=title, company_list=company_list)

@blueprint.route('<int:company_id>', methods=['GET'])
def company_detail(company_id):
    company = Company.query.get_or_404(company_id)
    return render_template('company/detail.html', company=company)