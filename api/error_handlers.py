from flask import Blueprint
from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import DatabaseError
from webargs import ValidationError as WebArgsError

err_handlers = Blueprint('err_handlers', __name__)


@err_handlers.app_errorhandler(400)
def handle_bad_request(err):
    if err.description:
        return err.description, 400
    return 'Bad Request', 400


@err_handlers.app_errorhandler(404)
def handle_not_found(err):
    return jsonify({'error': 'Not found'}), 404


@err_handlers.app_errorhandler(422)
def handle_unprocessable_entity(err):
    # webargs attaches additional metadata to the `data` attribute
    data = getattr(err, 'data')
    if data:
        # Get validations from the ValidationError object
        messages = data['messages']
    else:
        messages = ['Invalid request']
    return jsonify({'error': messages}), 422


@err_handlers.app_errorhandler(500)
def handle_bad_request(err):
    if err.description:
        return err.description, 500
    print err
    return 'Server Error. Please try again', 500


@err_handlers.app_errorhandler(ValidationError)
def handle_validation_errors(err):
    return jsonify({
        "error": err.messages
    }), 400


@err_handlers.app_errorhandler(DatabaseError)
def handle_database_errors(err):
    return jsonify({
        "error": "Server Error. Please try again"
    }), 500