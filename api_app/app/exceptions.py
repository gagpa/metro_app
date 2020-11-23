class NewsNotFounded(Exception):
    """
    Новости не найдены.
    """
    error = {'code': 200,
             'title': 'NotFounded',
             'detail': 'Сервис не может предоставить данные',
             }


class InvalidDayArgs(Exception):
    """
    Передан неверный аргумент day.
    """
    error = {'code': 400,
             'title': 'ValidationError',
             'detail': 'Передан неверный аргумент day',
             }
