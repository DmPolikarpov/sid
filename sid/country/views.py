from flask import Blueprint
from sid.country.models import Country



blueprint = Blueprint('country', __name__, url_prefix='/country')