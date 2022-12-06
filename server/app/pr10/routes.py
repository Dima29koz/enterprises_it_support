from flask import render_template, request

from . import pr10
from server.app.utils.api.address_api import get_address_data


@pr10.route('/', methods=['POST', 'GET'])
def index():
    return render_template('pr10/index.html')


@pr10.route('/get_address', methods=['GET'])
def get_address():
    return get_address_data(request.args.get('field1', ''))
