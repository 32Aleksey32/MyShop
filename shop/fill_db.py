import os

import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

DATA = [
    'user.sql',
    'category.sql',
    'product.sql',
    'cart.sql',
    'order.sql',
    'review.sql',
    'cart_product.sql'
]


def main(filename: str):
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dumps_directory = os.path.join(project_path, 'dumps')
    file_path = os.path.join(dumps_directory, filename)

    with connection.cursor() as cursor:
        with open(file_path, 'r') as file:
            sql_script = file.read()
            cursor.execute(sql_script)


if __name__ == "__main__":
    for sql_filename in DATA:
        main(filename=sql_filename)
    print('База данных успешно заполнена!')
