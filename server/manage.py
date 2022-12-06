from server.app import create_app, sio, db
from server import config

app = create_app(config.DevelopmentConfig)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
