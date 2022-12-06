from flask import Blueprint

pr8 = Blueprint('pr8', __name__, url_prefix='/pr8')

from . import routes