from setuptools import setup, find_packages
setup(
    name = 'RSS_reader',
    version = '4.0',
    description = 'Command-line RSS-parser',
    author = 'Ann Shimko',
    py_modules = ['RSS_reader'],
    install_requires=[
        'python-dateutil',
        'requests',
        'bs4',
        'lxml',
        'json2html',
        'reportlab'
      ],
    package_data={"fonts":
    [
        'DejaVuSerif-Bold.ttf',
        'DejaVuSerif-Italic.ttf',
        'DejaVuSerif-BoldItalic.ttf',
        'DejaVuSerif.ttf',
        'DejaVu Fonts License.txt',
        ]
    },
)