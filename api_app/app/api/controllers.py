from . import api
from flask import jsonify, request, make_response


@api.route('metro/news/')
def get_metro_news():
    """
    Выдать новости
    """
    day = request.args.get('day')
    return make_response(jsonify({'day': day}))
