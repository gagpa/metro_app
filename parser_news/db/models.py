from mongoengine import Document, StringField, URLField, DateTimeField
from datetime import datetime


class News(Document):
    """
    Модель Новости.
    """
    content = StringField(db_field='content', requirements=True, unique_with='title')
    title = StringField(db_field='title', requirements=True)
    image_url = URLField(db_field='image_url')
    type = StringField(db_field='type')
    published_date = DateTimeField(db_field='published_date', null=True)
    created_date = DateTimeField(db_field='created_date', default=datetime.now())
