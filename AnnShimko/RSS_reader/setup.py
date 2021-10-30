from setuptools import setup, find_packages

setup(
    name='RSS_reader',
    version='4.0',
    description='Command-line RSS-parser',
    author='Ann Shimko',
    py_modules=['RSS_reader'],
    packages=['rss_reader'],
    include_package_data=True,
    install_requires=[
        'python-dateutil',
        'requests',
        'bs4',
        'lxml',
        'json2html',
        'reportlab'
    ],
    entry_points={
        'console_scripts': [
            'rss_reader = rss_reader.RSS_reader:main',
        ],
    },
)
