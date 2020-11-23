from app.exceptions import NewsNotFounded
from app.models import News
from datetime import datetime, timedelta


def get_metro_news(delta_day: int) -> list:
    """
    Получить новости метро delta_day за последние delta_day дней.
    Возвращает список со структурой:
        [
          {
            news: str,
            header: str,
            url: str,
            publish_date: YYYY-mm-dd,
           }, ...
        ]
    """
    news = get_metro_news_from_db(delta_day)
    return news


def get_metro_news_from_db(delta_day: int) -> list:
    """
    Получить новости метро из БД за последние delta_day дней.
    Возвращает список со структурой:
        [
          {
            news: str,
            header: str,
            url: str,
            publish_date: datetime,
           }, ...
        ]
    """
    delta_date = datetime.now() - timedelta(days=delta_day)
    news = News.objects(publish_date__gte=delta_date)
    if news:
        return news
    raise NewsNotFounded
