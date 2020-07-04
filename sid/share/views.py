from flask import Blueprint
from sid.share.models import Share



blueprint = Blueprint('share', __name__, url_prefix='/share')