from flask import make_response, jsonify
from marshmallow.exceptions import ValidationError
from app.schemas import ResponseError
from . import api


@api.errorhandler(ValidationError)
def validation_error(e):
    error = {
        'code': 400,
        'title': 'Validation Error',
        'detail': e.messages
    }
    error = ResponseError().dump({'data': error})
    return make_response(jsonify(error))


@api.app_errorhandler(404)
def page_not_found(e):
    error = {
        'code': 404,
        'title': 'Not Found',
        'detail': 'Данная страница не найдена',
    }
    error = ResponseError().dump({'data': error})
    return make_response(jsonify(error))
