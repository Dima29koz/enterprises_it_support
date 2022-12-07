from flask import Blueprint

pr13 = Blueprint('pr13', __name__, url_prefix='/pr13')

from . import routes