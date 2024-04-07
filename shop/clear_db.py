import os

import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def main():
    with connection.cursor() as cursor:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'shop'")
        tables = cursor.fetchall()
        for table in tables:
            cursor.execute(f"TRUNCATE TABLE shop.{table[0]} CASCADE")


if __name__ == "__main__":
    main()
    print('База данных успешно очищена!')
