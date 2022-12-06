from flask import Blueprint

pr7 = Blueprint('pr7', __name__, url_prefix='/pr7')

from . import routes