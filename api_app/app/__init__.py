
from flask import Flask

from app.db import db
from app.serializer import ma
from configs.app_config import app_configs
from configs.settings import APP_MODE


def create_app(config_name):
    """
    Создать объект приложения.
    """
    app = Flask(__name__)

    config = app_configs[config_name]
    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)

    from .api import api
    app.register_blueprint(blueprint=api, url_prefix='/api/v1')

    return app


app = create_app(APP_MODE)
