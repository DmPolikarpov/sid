from flask import Blueprint
from sid.cashFlow.models import Cash_flow



blueprint = Blueprint('cashflow', __name__, url_prefix='/cashflow')