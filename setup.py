from setuptools import find_packages, setup

REQUIRES = [
    'Django==4.2.6',
    'Pillow==10.1.0',
    'djangorestframework==3.14.0',
    'psycopg2==2.9.9',
    'setuptools==65.5.1',
    'wheel==0.38.4',
    'pip==23.3.2',
    'python-dotenv==1.0.1',
    "django-filter==24.2"
]


CODESTYLE_REQUIRES = [
    'flake8==6.1.0',
    'isort==5.13.2',
]


setup(
    name='shop',
    packages=find_packages(),
    install_requires=REQUIRES,
    extras_require={'codestyle': CODESTYLE_REQUIRES}
)
