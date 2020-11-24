from bs4 import BeautifulSoup

from serializers.date_translator import translate, transform
from .html_map import metro_news_html_map as map


class ParserNews:
    """
    Парсит из блоков поля.
    """

    def parse_title(self, block: BeautifulSoup) -> str:
        """
        Запарсить заголовок статьи.
        """
        title_map = map['title']
        title = block.find(title_map['tag'], attrs=title_map['attrs']).text
        return title

    def parse_news_uri(self, block: BeautifulSoup) -> str:
        """
        Запарсить URI новости.
        """
        news_uri_map = map['news_uri']
        news_uri = block.find(news_uri_map['tag'], attrs=news_uri_map['attrs'])['href']
        return news_uri

    def parse_published_date(self, block: BeautifulSoup) -> str:
        """
        Запарсить дату публикации.
        """
        published_date_map = map['published_date']
        published_date = block.find(published_date_map['tag'], attrs=published_date_map['attrs']).text
        return transform(translate(published_date))


    def parse_content(self, block: BeautifulSoup) -> str:
        """
        Запарсить контент.
        """
        all_content_map = map['all_content']
        all_content = block.find(all_content_map['tag'], attrs=all_content_map['attrs'])

        content_map = map['content']
        content = all_content.find(content_map['tag'], attrs=content_map['attrs'], recursive=False).text
        return content.strip().replace('\n', '')

    def parse_image_uri(self, block: BeautifulSoup) -> str or None:
        """
        Запарсить URI картинки.
        """
        image_uri_map = map['image_uri']
        image_uri = block.find(image_uri_map['tag'], attrs=image_uri_map['attrs'])['src']
        return image_uri


    def parse_news_blocks(self, block: BeautifulSoup) -> list:
        """
        Запарсить на странице новостные блоки.
        """
        new_blocks_map = map['new_blocks']
        news_blocks = block.find_all(new_blocks_map['tag'], attrs=new_blocks_map['attrs'])
        return news_blocks
