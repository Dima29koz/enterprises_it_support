from flask import render_template

from server.app import login_manager
from server.app.main import main


@login_manager.user_loader
def load_user(user_id):
    return None


@main.route('/')
def index():
    return render_template('index.html')
