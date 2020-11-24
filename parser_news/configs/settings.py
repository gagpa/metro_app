"""
Файл с настройками
"""

import os


# Настройки подключения к БД MongoDB
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
