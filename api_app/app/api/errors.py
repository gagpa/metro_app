from flask import make_response, jsonify

from app.exceptions import NewsNotFounded, InvalidDayArgs
from app.schemas import Error
from . import api


@api.errorhandler(InvalidDayArgs)
def invalid_days_args(e):
    schema = Error()
    error = schema.dump(InvalidDayArgs.error)
    return make_response(jsonify(error))


@api.errorhandler(NewsNotFounded)
def invalid_days_args(e):
    schema = Error()
    error = schema.dump(NewsNotFounded.error)
    return make_response(jsonify(error))


@api.app_errorhandler(404)
def page_not_found(e):
    schema = Error()
    error = {'code': 404,
             'title': 'Not Found',
             'detail': 'Данная страница не найдена',
             }
    error = schema.dump(error)
    return make_response(jsonify(error))
