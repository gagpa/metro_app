from flask import jsonify, request, make_response

from app.schemas import ResponseNews
from app.services.news import get_metro_news as service_get_metro_news
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
    news = service_get_metro_news(day)
    schema = ResponseNews()

    content = schema.dump({'data': news})
    return make_response(jsonify(content))
