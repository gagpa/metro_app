"""
Файл с картой html для парсинга
"""
import re

metro_news_html_map = {
    'image_uri': {'tag': 'img',
                  'attrs': {'class': 'newslist__image'}
                  },

    'title': {'tag': 'span',
              'attrs': {'class': 'newslist__text-title'}
              },

    'news_uri': {'tag': 'a',
                 'attrs': {'class': 'newslist__link'}
                 },

    'published_date': {'tag': 'div',
                       'attrs': {'class': 'pagetitle__content-date'}
                       },

    'new_blocks': {'tag': 'div',
                   'attrs': {'class': re.compile('(newslist__list-item)( _warning)*')}
                   },

    'all_content': {'tag': 'div',
                    'attrs': {'class': 'newspage__content'}
                    },

    'content': {'tag': 'div',
                'attrs': {'class': 'usercontent'}
                },
}
