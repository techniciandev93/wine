from datetime import datetime
import pandas
from collections import defaultdict


class YearTypeError(TypeError):
    pass


year = (datetime.now() - datetime(1920, 1, 1)).days // 365


def get_correct_form_word(year):
    if isinstance(year, int):
        if 10 < int(str(year)[-2:]) < 20:
            return "лет"
        last_digit = int(str(year)[-1])
        if last_digit == 1:
            return "год"
        elif last_digit == 0 or 5 <= last_digit <= 9:
            return "лет"
        elif 2 <= last_digit <= 4:
            return "года"
    else:
        raise YearTypeError('Год должен быть типом int')


def get_wine_records(path):
    category_wine_records = defaultdict(list)
    wine_records = pandas.read_excel(path, na_values=['N/A', 'NA'], keep_default_na=False)
    for wine_record in wine_records.to_dict(orient='records'):
        category_wine_records[wine_record['Категория']].append(
            {product: value for product, value in wine_record.items() if product != 'Категория'}
        )
    return category_wine_records
