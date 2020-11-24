from app.serializer import ma


class News(ma.Schema):
    """
    Схема сериализации новостей.
    """

    content = ma.String()
    title = ma.String()
    image_url = ma.String()
    published_date = ma.Date()

    class Meta:
        fields = ('content', 'title', 'image_url', 'published_date')
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


class ResponseNews(ma.Schema):
    """
    Схема ответа с новостями.
    """
    data = ma.List(ma.Nested(News), default=[])
    success = ma.Boolean(default=True)


class ResponseError(ma.Schema):
    """
    Схема ответа об ошибке
    """
    data = ma.Nested(Error)
    success = ma.Boolean(default=False)
