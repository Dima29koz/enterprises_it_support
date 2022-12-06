from flask import Blueprint

pr11 = Blueprint('pr11', __name__, url_prefix='/pr11')

from . import routes