from flask import url_for, redirect, request, render_template, flash
from flask_login import current_user, login_user, login_required, logout_user

from server.app.pr13 import pr13
from server.app.pr13.forms import LoginForm, RegistrationForm
from server.app.pr13.models import get_user_by_name, User


@pr13.route('/')
def index():
    return render_template('pr13/index.html')


@pr13.route('/login_success')
@login_required
def login_success():
    return render_template('pr13/login_success.html')


@pr13.route('/login', methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(request.args.get("next") or url_for('pr13.login_success'))

    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_name(form.name.data)
        if user and user.check_password(form.pwd.data):
            rm = form.remember.data
            login_user(user, remember=rm)
            return redirect(request.args.get("next") or url_for('pr13.login_success'))
        flash("Неверная пара логин/пароль", "error")
    return render_template("pr13/login.html", form=form)


@pr13.route('/registration', methods=["POST", "GET"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.user_email.data, form.pwd.data)
        return redirect(url_for('pr13.login'))
    return render_template('pr13/registration.html', form=form)


@pr13.route("/logout")
@login_required
def logout():
    """
    view of `logout` page
    logs out user
    """
    logout_user()
    return redirect(url_for('pr13.index'))
