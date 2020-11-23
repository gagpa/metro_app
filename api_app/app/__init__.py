from flask import Flask
from configs.app_config import app_configs
import os


def create_app(config_name):
    """
    Создать объект приложения.
    """
    app = Flask(__name__)

    config = app_configs[config_name]
    app.config.from_object(config)

    from .api import api
    app.register_blueprint(blueprint=api, url_prefix='/api/v1')

    return app


app = create_app(os.getenv('APP_MODE'))
