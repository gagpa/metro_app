from flask import jsonify, request, make_response

from app.schemas import News as NewsSchema
from app.services.news import get_metro_news as service_get_metro_news
from app.validators import GetMetroNewsDayValidator
from configs.settings import default_delay_days
from . import api


@api.route('/metro/news')
def get_metro_news():
    """
    Выдать новости
    """
    GetMetroNewsDayValidator().validate_args(request.args)
    day = request.args.get('day', default_delay_days)
    news = service_get_metro_news(int(day))
    schema = NewsSchema()
    news = [schema.dump(new) for new in news]
    return make_response(jsonify(news))
