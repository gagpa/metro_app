from app.db import db
from datetime import datetime


class News(db.Document):
    """
    Модель Новости.
    """
    content = db.StringField(db_field='content', requirements=True, unique_with='title')
    title = db.StringField(db_field='title', requirements=True)
    image_url = db.URLField(db_field='image_url')
    type = db.StringField(db_field='type')
    published_date = db.DateTimeField(db_field='published_date', null=True)
    created_date = db.DateTimeField(db_field='created_date', default=datetime.now())
