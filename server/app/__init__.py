from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

db = SQLAlchemy()
login_manager = LoginManager()
sio = SocketIO()
migrate = Migrate()


def create_app(config) -> Flask:
    """
    Creates app and register Blueprints

    :returns: app
    :rtype: Flask
    """
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.test_request_context():
        db.create_all()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .pr7 import pr7 as pr7_blueprint
    app.register_blueprint(pr7_blueprint)
    from .pr8 import pr8 as pr8_blueprint
    app.register_blueprint(pr8_blueprint)
    from .pr9 import pr9 as pr9_blueprint
    app.register_blueprint(pr9_blueprint)
    from .pr10 import pr10 as pr10_blueprint
    app.register_blueprint(pr10_blueprint)
    from .pr11 import pr11 as pr11_blueprint
    app.register_blueprint(pr11_blueprint)
    from .pr13 import pr13 as pr13_blueprint
    app.register_blueprint(pr13_blueprint)

    sio.init_app(app, logger=config.LOGGER, manage_session=config.MANAGE_SESSION)

    return app
