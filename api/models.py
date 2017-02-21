from itsdangerous import URLSafeTimedSerializer, Signer

from extentions import db
from flask import current_app as app


class Base(db.Model):

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class User(Base):

    last_name = db.Column(db.String(128), nullable=False,)
    first_name = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)

    def generate_reset_token(self):
        return URLSafeTimedSerializer(app.config['SECRET_KEY'], 'reset_token').dumps(self.email)

    @classmethod
    def retrive_reset_email(cls, token):
        return URLSafeTimedSerializer(app.config['SECRET_KEY'], 'reset_token').loads(token, max_age=86400)