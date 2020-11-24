"""
Файл с настройками
"""

import os


# Настройки подключения к БД MongoDB
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


# Настройки подключения к брокеру

# Протокол брокера
BROKER_PROTOCOL = os.getenv('BROKER_PROTOCOL')

# Пользователь брокера
BROKER_USER = os.getenv('BROKER_USER')

# Пароль от пользователя
BROKER_PASSWORD = os.getenv('BROKER_PASSWORD')

# Хост брокера
BROKER_HOST = os.getenv('BROKER_HOST')

# Порт брокера
BROKER_PORT = os.getenv('BROKER_PORT')

# Полный URl для соединения с брокером
BROKER = f'{BROKER_PROTOCOL}://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}//'

SCHEDULE_TIMEOUT = int(os.getenv('SCHEDULE_TIMEOUT')) or 600
