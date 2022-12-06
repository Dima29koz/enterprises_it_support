import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    LOGGER = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    MANAGE_SESSION = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOGGER = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app_dir, 'test.db')
