from app.serializer import ma


class News(ma.Schema):
    """
    Схема сериализации новостей.
    """

    news = ma.String()
    header = ma.String()
    url = ma.String()
    publish_date = ma.Date()

    class Meta:
        fields = ('news', 'header', 'url', 'publish_date')
        datetimeformat = 'YYYY-mm-dd'


class Error(ma.Schema):
    """
    Схема сериализации ошибки.
    """

    code = ma.Integer()
    title = ma.String()
    detail = ma.String()

    class Meta:
        fields = ('code', 'title', 'detail',)
