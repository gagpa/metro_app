import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from db.models import News
from parser.parser_news_list import ParserNewsList

if __name__ == '__main__':

    last_date = News.objects.order_by('id').first().published_date
    parser = ParserNewsList()

    while True:

        news = parser.parse(last_date)
        for n in news:
            News(**n).save()

        if len(news) < 24:
            break
