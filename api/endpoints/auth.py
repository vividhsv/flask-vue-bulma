import gevent
from flask import current_app
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for
from flask_mail import Message
from flask_jwt_extended import create_access_token
from flask_classful import FlaskView, route
from itsdangerous import SignatureExpired, BadTimeSignature

from api.extentions import db, bcrypt, mail
from api.models import User
from api.schemas import UserSchema


class AuthView(FlaskView):

    @route('/login', methods=['POST'], endpoint='login')
    def login(self):
        post_data = request.get_json()
        user = User.query.filter_by(email=post_data.get('email')).first()

        if user and bcrypt.check_password_hash(user.password, post_data.get('password')):
            resp = {'auth_token': create_access_token(identity=user.id)}
            return jsonify(resp), 200
        else:
            resp = {'error': 'Invalid username or password. Please try again'}
            return jsonify(resp), 401

    @route('/registration', methods=['POST'], endpoint='register')
    def registration(self):
        user = UserSchema().load(request.get_json(), session=db.session).data
        user_exists = db.session.query(db.exists().where(User.email == user.email)).scalar()
        if user_exists:
            return jsonify({"error": "User already exists"}), 409
        user.password = bcrypt.generate_password_hash(user.password)
        db.session.add(user)
        db.session.commit()
        return UserSchema().jsonify(user), 201

    @route('/reset', methods=['POST'], endpoint='reset')
    def reset(self):
        post_data = request.get_json()
        user = User.query.filter_by(email=post_data.get('email')).first()

        if not user:
            resp = {'error': 'User does not exist'}
            return jsonify(resp), 404
        else:
            reset_url = "{}/#/auth/reset?token={}".format(current_app.config['SERVER_URL'], user.generate_reset_token())

            def task():
                mail.send(Message(
                    sender='noreply@fue.com',
                    recipients=[user.email],
                    subject='Password Reset',
                    html=render_template('emails/reset_password.html', first_name=user.first_name, reset_url=reset_url)
                ))

            gevent.spawn(task()).start()
            return jsonify({'message': 'Reset link has been emailed. Please check your email to reset your password'}), 201

    @route('/reset/<token>', methods=['POST'], endpoint='reset_with_token')
    def reset_with_token(self, token):
        try:
            email = User.retrive_reset_email(token)
        except SignatureExpired:
            return jsonify({'error': 'Expired reset link'}), 400
        except BadTimeSignature:
            return jsonify({'error': 'Invalid reset link'}), 400

        user = User.query.filter_by(email=email).first_or_404()
        if not user:
            resp = {'error': 'User does not exist'}
            return jsonify(resp), 404
        else:
            user.password = bcrypt.generate_password_hash(request.get_json().get('password'))
            db.session.commit()
            return jsonify({'message': 'Password reset successfully'}), 201
