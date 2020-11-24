from datetime import datetime


RU_MONTH_VALUES = {
    'Января': '01',
    'Февраля': '02',
    'Марта': '03',
    'Апреля': '04',
    'Мая': '05',
    'Июня': '06',
    'Июля': '07',
    'Августа': '08',
    'Сентября': '09',
    'Октября': '10',
    'Ноября': '11',
    'Декабря': '12',
}


def translate(date: str):
    for key in RU_MONTH_VALUES.keys():
        if key in date:
            date = date.replace(key, RU_MONTH_VALUES[key])
            return date


def transform(date: str):
    date = datetime.strptime(date, '%d %m %Y')
    return date
