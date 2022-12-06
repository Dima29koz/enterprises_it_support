from flask import Blueprint

pr9 = Blueprint('pr9', __name__, url_prefix='/pr9')

from . import routes