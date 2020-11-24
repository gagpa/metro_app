import requests
from bs4 import BeautifulSoup


def get_soup(link: str) -> BeautifulSoup:
    """
    Получить объект для парсинга по ссылки.
    """
    raw_html = get_html(link)
    return do_soup(raw_html)


def get_html(link: str) -> str:
    """
    Получить html
    """
    response = requests.get(link, headers={'Referer': f'{link}',
                                           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0)'
                                                         ' Gecko/20100101 Firefox/82.0',

                                           })
    if response.status_code == 200:
        return response.text


def do_soup(raw_html: str) -> BeautifulSoup:
    """
    Получить из сырого html объект для парсинга.
    """
    return BeautifulSoup(raw_html, 'html.parser')


