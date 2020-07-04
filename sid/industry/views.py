from flask import Blueprint
from sid.industry.models import Industry



blueprint = Blueprint('industry', __name__, url_prefix='/industry')