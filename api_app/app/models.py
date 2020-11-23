from app.db import db
from datetime import datetime


class News(db.Document):
    """
    Модель Новостей.
    """
    news = db.StringField(db_field='news', requirements=True, unique_with='header')
    header = db.StringField(db_field='header', requirements=True)
    url = db.URLField(db_field='url', requirements=True, unique=True)
    publish_date = db.DateTimeField(db_field='publish_date', requirements=True)
    save_date = db.DateTimeField(db_field='save_date', default=datetime.now())
