from marshmallow.exceptions import ValidationError

from app.exceptions import InvalidDayArgs
from app.serializer import ma


class GetMetroNewsDayValidator(ma.Schema):
    """
    Схема для валидирования данных /metro/news
    """

    day = ma.Integer(requirements=False)

    def validate_args(self, args):
        try:
            self.load(args)
        except ValidationError:
            raise InvalidDayArgs
