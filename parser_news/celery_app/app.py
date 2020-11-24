from celery import Celery

from configs.settings import BROKER_PROTOCOL, BROKER_PASSWORD, BROKER_PORT, BROKER_HOST, BROKER_USER
from services.update_news import update_news

app = Celery(broker=f'{BROKER_PROTOCOL}://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}//')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(600.0, update_news_in_db.s('hello'), name='add every 10 min')


@app.task
def update_news_in_db():
    update_news()
