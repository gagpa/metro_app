from flask import Blueprint

api = Blueprint(__file__, 'api')

from . import controllers, errors
