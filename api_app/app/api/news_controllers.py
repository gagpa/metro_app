from flask import jsonify, request, make_response

from app.schemas import News as NewsSchema
from app.services.news import get_metro_news as service_get_metro_news
from app.validators import NewsRequestValidator
from . import api


@api.route('/metro/news')
def get_metro_news():
    """
    Выдать новости
    """
    NewsRequestValidator().validate_args(request.args)
    day = request.args.get('day')
    news = service_get_metro_news(day)
    schema = NewsSchema()
    if news:
        content = [schema.dump(n) for n in news]
    else:
        content = schema.dump(news)
    return make_response(jsonify(content))
