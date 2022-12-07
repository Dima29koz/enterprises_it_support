from flask import render_template

from server.app.main import main


@main.route('/')
def index():
    return render_template('index.html')
