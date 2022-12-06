from flask import render_template, request

from ..pr9 import pr9
from server.app.utils.api.bank_api import get_bank_data


@pr9.route('/', methods=['POST', 'GET'])
def index():
    return render_template('pr9/index.html')


@pr9.route('/get_fin_data', methods=['GET'])
def get_fin_data():
    return get_bank_data(request.args.get('field1', ''))
