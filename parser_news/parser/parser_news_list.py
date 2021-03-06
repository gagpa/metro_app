from urllib.parse import urljoin

from .parser_news import ParserNews
from .request_soup import get_soup


class ParserNewsList:
    parser_news = ParserNews()
    link = 'https://mosmetro.ru/press/news/?PAGEN_1={page_number}'
    url_news = 'https://mosmetro.ru/press/news/'

    def __init__(self):
        self.page_number = 0

    def parse(self, last_date=None) -> list:
        """
        Запарсить новости на текущей странице (page_number).
        """
        list_page = self.parse_next_list_page()
        news_blocks = self.parser_news.parse_news_blocks(list_page)
        news = []
        for block in news_blocks:
            try:
                news_uri = self.parser_news.parse_news_uri(block)
                title = self.parser_news.parse_title(block)
                image_uri = self.parser_news.parse_image_uri(block)
                direct_page = self.parse_direct_page(news_uri)
                published_date = self.parser_news.parse_published_date(direct_page)

                if last_date and published_date <= last_date:
                    return news

                content = self.parser_news.parse_content(direct_page)

                news.append(
                    {'title': title,
                     'published_date': published_date,
                     'content': content,
                     'image_url': urljoin(self.url_news, image_uri),
                     })
            except (AttributeError, TypeError):
                continue
        return news

    def parse_direct_page(self, uri):
        """
        Получить объект конкретной новости для парсинга.
        """
        direct_news_url = urljoin(self.url_news, uri)
        direct_page = get_soup(direct_news_url)
        return direct_page

    def parse_next_list_page(self):
        """
        Получить объект списка новостей для парсинга следующей страницы.
        """
        self.page_number += 1
        html = get_soup(self.link.format(page_number=self.page_number))
        return html
