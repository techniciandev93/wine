from datetime import datetime
import pandas
from collections import defaultdict

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
        raise TypeError('Год должен быть типом int')


def get_records_wine(path):
    records_category_wine = defaultdict(list)
    records_wine = pandas.read_excel(path, na_values=['N/A', 'NA'], keep_default_na=False)
    for record_wine in records_wine.to_dict(orient='records'):
        records_category_wine[record_wine['Категория']].append(
            {product: value for product, value in record_wine.items() if product != 'Категория'}
        )
    return records_category_wine
