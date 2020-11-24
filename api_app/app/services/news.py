from datetime import datetime, timedelta

from app.models import News
from configs.settings import DEFAULT_DELTA_DAYS


def get_metro_news(delta_day: int = None) -> list:
    """
    Получить новости метро delta_day за последние delta_day дней.
    Возвращает список со структурой:
        [
          {
            content: str,
            title: str,
            image_url: str,
            published_date: datetime,
           }, ...
        ]
    """
    delta_day = delta_day or DEFAULT_DELTA_DAYS
    news = get_metro_news_from_db(int(delta_day))
    return news


def get_metro_news_from_db(delta_day: int) -> list:
    """
    Получить новости метро из БД за последние delta_day дней.
    Возвращает список со структурой:
        [
          {
            content: str,
            title: str,
            image_url: str,
            published_date: datetime,
           }, ...
        ]
    """
    delta_date = datetime.now() - timedelta(days=delta_day)
    news = News.objects(published_date__gte=delta_date)
    return news
