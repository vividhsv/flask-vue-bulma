import os


class Config():

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    V1_ROUTE_PREFIX = '/api/v1'
    TRAILING_SLASH = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me


class DevConfig(Config):

    ENV = 'dev'

    SERVER_URL = 'http://localhost:5000'
    DEBUG = True
    DB_NAME = 'app.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    SECRET_KEY = "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0"

    MAIL_SERVER = os.environ('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER ="noreply@example.com"
