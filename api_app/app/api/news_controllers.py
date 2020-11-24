from flask import jsonify, request, make_response

from app.schemas import ResponseNews
from app.services.news import get as news_service
from app.validators import NewsRequestValidator
from . import api


@api.route('/metro/news')
def get():
    """
    Выдать новости.
    args: day - integer.
    """
    NewsRequestValidator().validate_args(request.args)
    day = request.args.get('day')
    news = news_service(day)
    schema = ResponseNews()
    content = schema.dump({'data': news})
    return make_response(jsonify(content))
