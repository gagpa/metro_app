"""
Файл с настройками приложения flask.
"""
import os


class Config:
    """
    Общий класс настроек.
    """

    # Настройки подключения к монго. Объект БД сохранит к себе в свойства.
    MONGODB_SETTINGS = {
        'db': os.getenv('DB_NAME'),
        'host': f'mongodb://{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}',
        'port': int(os.getenv('DB_PORT')),
    }


class DevelopmentConfig(Config):
    """
    Настройки приложения flask для разработки.
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Настройки приложения flask для продакшина.
    """
    pass


# Словарь предоставляет удобный доступ объект для получения настроек приложения flask
app_configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
