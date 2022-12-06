from flask import render_template, redirect, url_for, request, jsonify

from server.app.pr7 import pr7
from server.app.pr7.forms import Index1Form, Index3Form
from server.app.utils.search import get_matches

NAMES = ['user1', 'user2', 'user3', 'user4', 'support1', 'support2', 'support3', 'support4']


@pr7.route('/')
def index():
    return render_template('pr7/index.html')


@pr7.route('/index1', methods=['POST', 'GET'])
def index1():
    form = Index1Form()
    if form.validate_on_submit():
        field1 = form.field1.data
        field2 = form.field2.data
        return redirect(url_for('pr7.index2', field1=field1, field2=field2))
    return render_template('pr7/index1.html', form=form)


@pr7.route('/index2')
def index2():
    return render_template('pr7/index2.html', field1=request.args.get('field1'), field2=request.args.get('field2'))


@pr7.route('/index3', methods=['POST', 'GET'])
def index3():
    form = Index3Form()
    return render_template('pr7/index3.html', form=form)


@pr7.route('/index4', methods=['GET'])
def index4():
    return jsonify({'matches': get_matches(request.args.get('field1', ''), NAMES)})

