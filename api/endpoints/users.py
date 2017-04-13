from flask import jsonify
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_classful import FlaskView, route
from webargs.flaskparser import parser

from api.extentions import db, bcrypt
from api.schemas import UserSchema, UserPageSchema, PageArgsSchema
from api.models import User


class UsersView(FlaskView):

    users_schema = UserSchema()
    users_page = UserPageSchema()
    page_args = PageArgsSchema()

    @jwt_required
    def index(self):
        args = parser.parse(self.page_args, request)
        users = User.query.paginate(args['page'], args['per_page'], error_out=False)
        return jsonify(self.users_page.dump(users).data), 200

    @jwt_required
    def get(self, pk):
        user = User.query.get_or_404(pk)
        return self.users_schema.jsonify(user), 200

    @jwt_required
    def post(self):
        user = UserSchema().load(request.get_json(), session=db.session).data
        user_exists = db.session.query(db.exists().where(User.email == user.email)).scalar()
        if user_exists:
            return jsonify({"error": "User already exists"}), 409
        user.password = bcrypt.generate_password_hash(user.password)
        db.session.add(user)
        db.session.commit()
        return UserSchema().jsonify(user), 201

    @jwt_required
    def put(self, pk):
        user = User.query.get_or_404(pk)

        # Check if updated email already exists
        check_user = User.query.filter(User.email == request.get_json().get('email')).first()
        if check_user and check_user.id != user.id:
            return jsonify({'error': 'User email already exists'}), 409

        user = UserSchema(only=('email', 'first_name', 'last_name', 'password')).load(request.get_json(), instance=user,partial=('email', 'first_name', 'last_name', 'password'), session=db.session).data
        if(user.password):
            user.password = bcrypt.generate_password_hash(user.password)
        db.session.commit()
        return UserSchema().jsonify(user), 200

    @jwt_required
    def delete(self, pk):
        user = User.query.get_or_404(pk)
        db.session.delete(user)
        db.session.commit()
        return '', 204