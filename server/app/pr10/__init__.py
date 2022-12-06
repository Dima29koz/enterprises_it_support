from flask import Blueprint

pr10 = Blueprint('pr10', __name__, url_prefix='/pr10')

from . import routes