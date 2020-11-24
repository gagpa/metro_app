"""
Файл создание подключения к БД
"""

from mongoengine import connect

from configs.settings import DB_NAME, DB_HOST, DB_PORT

db = connect(DB_NAME,
             host=f'mongodb://{DB_HOST}:{DB_PORT}/{DB_NAME}',
             port=int(DB_PORT))
