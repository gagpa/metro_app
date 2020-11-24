import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from db.models import News
from parser.parser_news_list import ParserNewsList

if __name__ == '__main__':
    parser = ParserNewsList()

    news = parser.parse()
    for n in news:
        News(**n).save()
