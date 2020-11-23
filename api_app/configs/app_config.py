import os

class Config:
    pass


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
