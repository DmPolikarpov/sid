from flask import Blueprint
from sid.company.models import Company




blueprint = Blueprint('company', __name__, url_prefix='/company')