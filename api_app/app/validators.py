from marshmallow.exceptions import ValidationError

from app.serializer import ma
from configs.settings import MAX_DELTA_DAYS


class DaysField(ma.Field):
    """
    Кастомное поле для валидации количества дней.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        if not isinstance(value, str) or not value.isdigit():
            raise ValidationError('должно быть числом')
        elif int(value) < 0:
            raise ValidationError(f'должно быть положительным или равно 0')
        elif int(value) > MAX_DELTA_DAYS:
            raise ValidationError(f'должно быть меньше {MAX_DELTA_DAYS}')
        return int(value)


class NewsRequestValidator(ma.Schema):
    """
    Схема для валидирования данных /metro/news
    """

    day = DaysField(requirements=False)

    def validate_args(self, args):
        self.load(args)
