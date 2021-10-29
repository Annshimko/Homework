from setuptools import setup
setup(
    name = 'RSS_reader',
    version = '1.1',
    description = 'Command-line RSS-parser',
    author = 'Ann Shimko',
    py_modules = ['RSS_reader'],
    install_requires=[
        'dateutil.parser',
        'requests',
        'bs4',
      ],
)