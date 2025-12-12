from setuptools import setup, find_packages

setup(
    name='review_analyzer',
    version='0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyramid',
        'waitress',
        'SQLAlchemy',
        'psycopg2-binary',
        'pyramid_tm',
        'zope.sqlalchemy',
        'python-dotenv',
        'google-genai',
        'transformers',
    ],
    entry_points={
        'paste.app_factory': [
            'main = review_analyzer:main',
        ],
    },
)