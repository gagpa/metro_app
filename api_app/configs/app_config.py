import os


class Config:
    MONGODB_SETTINGS = {
        'db': os.getenv('DB_NAME'),
        'host': f'mongodb://{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}',
        'port': int(os.getenv('DB_PORT')),
    }


class DevelopmentConfig(Config):
    """
    Настройки для разработки
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Настройки для продакшина.
    """
    pass


app_configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
