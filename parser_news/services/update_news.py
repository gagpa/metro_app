from db.models import News
from parser.parser_news_list import ParserNewsList


def update_news():
    news = News.objects.order_by('id').first()
    if news:
        last_date = news.published_date
    else:
        last_date = None
    parser = ParserNewsList()
    while True:
        news = parser.parse(last_date)
        for n in news:
            News(**n).save()
        if len(news) == 0:
            break
