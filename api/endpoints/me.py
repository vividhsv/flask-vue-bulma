from flask import request, jsonify
from flask_classful import FlaskView, route
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.extentions import bcrypt, db
from api.models import User
from api.schemas import UserSchema


class MeView(FlaskView):

    users_schema = UserSchema()

    @jwt_required
    def index(self):
        user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)
        return self.users_schema.jsonify(user), 200

    @jwt_required
    def put(self):
        user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)

        # Check if updated email already exists
        check_user = User.query.filter(User.email == request.get_json().get('email')).first()
        if check_user and check_user.id != user.id:
            return jsonify({'error': 'User email already exists'}), 409

        user = UserSchema(only=('email', 'first_name', 'last_name', 'password')).load(request.get_json(), instance=user,partial=('email', 'first_name', 'last_name', 'password'), session=db.session).data
        password = request.get_json().get('password')
        if(password):
            user.password = bcrypt.generate_password_hash(password)
        db.session.commit()
        return UserSchema().jsonify(user), 200