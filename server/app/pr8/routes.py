from flask import render_template, request

from server.app.pr8 import pr8
from server.app.utils.api.weather_api import get_weather


@pr8.route('/', methods=['POST', 'GET'])
def index():
    return render_template('pr8/index.html')


@pr8.route('/get_weather', methods=['GET'])
def index1():
    return get_weather(request.args.get('field1', ''))
