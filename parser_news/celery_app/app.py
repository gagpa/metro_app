from celery import Celery

from configs.settings import BROKER, SCHEDULE_TIMEOUT
from services.update_news import update_news

app = Celery(broker=BROKER)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Записывавет задачи в расписание.
    """
    sender.add_periodic_task(SCHEDULE_TIMEOUT, update_news_in_db.s(), name='add every 10 min')


@app.task
def update_news_in_db():
    """
    Задача на обновление данных в очереди.
    """
    update_news()
