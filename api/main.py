from flask import Flask

from api.config import ProdConfig
from api.endpoints.auth import AuthView
from api.endpoints.me import MeView
from api.error_handlers import err_handlers
from api.root import RootView
from endpoints.users import UsersView
from extentions import db, ma, migrate, bcrypt, jwt, cors, mail, oauth


def create_app(config_object=ProdConfig):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extentions(app)
    register_views(app)
    return app


def register_extentions(app):
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    mail.init_app(app)
    oauth.init_app(app)
    migrate.init_app(app, db)


def register_views(app):
    v1_prefix = app.config['V1_ROUTE_PREFIX']
    slash = app.config['TRAILING_SLASH']

    app.register_blueprint(err_handlers)
    RootView.register(app, trailing_slash=slash)
    UsersView.register(app, route_prefix=v1_prefix, trailing_slash=slash)
    AuthView.register(app, route_prefix=v1_prefix, trailing_slash=slash)
    MeView.register(app, route_prefix=v1_prefix, trailing_slash=slash, route_base='/users/me')