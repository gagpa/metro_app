from flask import Blueprint

api = Blueprint(__name__, 'api')

from . import news_controllers, errors
