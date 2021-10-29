import subprocess
import sys
import os
from datetime import datetime
import urllib.request
import json
import argparse
import logging

try:
    from dateutil.parser import parse
except ModuleNotFoundError as error:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'dateutil.parser'])
    from dateutil.parser import parse
try:
    import requests
except ModuleNotFoundError as error:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    import requests
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError as error:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'bs4'])
    from bs4 import BeautifulSoup


def exception_wrapper(exit_mode=True):
    """Wraps the function in oreder to catch an exception, if exit_mode - exits the app and writes an exit message"""

    def inner_wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as error:
                logging.exception(error)
                if exit_mode:
                    exit(f'An error occured: {error} \nExit to prevent further errors')

        return wrapper

    return inner_wrapper


@exception_wrapper()
def get_args():
    """ Unpacks arguments from command line and returns them as "args" object."""
    parser = argparse.ArgumentParser(description='Parses an RSS feed')
    parser.add_argument('source', type=str, help='a source for parsing')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('--json', action='store_true', help='write collected feed into json file')
    parser.add_argument('--verbose', action='store_true', help='verbose status message')
    parser.add_argument('--limit', type=int, help='Limit of news in feed. In case of None Limit all feed is provided')
    args = parser.parse_args()
    if args.limit and args.limit <= 0:
        exit("Error: wrong --limit argument, limit value should be positive number")
    return args


@exception_wrapper()
def parse_news(source):
    """Requests the source page content and parses it with BeautifulSoup module"""
    url = requests.get(source)
    if url.status_code != 200:
        exit('Error opening RSS-feed')
    all_news = BeautifulSoup(url.content.decode('utf-8'), 'xml')
    return all_news


@exception_wrapper()
def cache_feed(allnews, source):
    """Creates list of dictionaries containing fields RSS-feed"""
    cache_list = []
    channel = allnews.channel
    entries = allnews.find_all('item')
    for entry in entries:
        cache_dict = {
            'RSS': channel.title.text,
            'RSS link': source,
        }
        cache_dict.update({
            'Title': entry.title.text,
            'News link': entry.link.text,
            'Published': str(parse(entry.pubDate.text).date()),
            'Image source': []
        })
        if entry.description:
            cache_dict.update({'Description': BeautifulSoup(entry.description.text, 'html.parser').text})
            if BeautifulSoup(entry.description.text, 'html.parser').img:
                URL = BeautifulSoup(entry.description.text, "html.parser").img["src"]
                cache_dict['Image source'].append(URL)

        if entry.find('media:content'):
            for item in str(entry.find('media:content')).split():
                if 'url' in item:
                    URL = item.strip('url="').strip('"')
            cache_dict['Image source'].append(URL)

        cache_list.append(cache_dict)
    return cache_list


@exception_wrapper()
def write_feed(feed_list, writing_mode=None):
    """Prints parsed RSS-feed depending on writing mode:
    if writing_mode is not None - into <<news_feed + posfix depending on current date-time>>.json file
    in json_files folder
    and prints content of the file into stdout
    else - prints parsed RSS-feed into stdout"""

    if writing_mode:
        if not os.path.exists('json_files'):
            os.makedirs('json_files')
        file_name = "json_files/news_feed" + str(datetime.now())
        file_name = file_name.replace(':', '').replace('.', '') + '.json'

        with open(file_name, "w", encoding='utf8') as file:
            json.dump(feed_list, file, ensure_ascii=False, indent=4)
        print(feed_list)
    else:
        if feed_list != []:
            for news in feed_list:
                for key, value in news.items():
                    if key != 'Image source':
                        print(f'{key + ":":<15} {value}')
                    else:
                        for link in value:
                            print(f'{key + ":":<15} {link}')
                    if key == 'RSS link':
                        print()
                print()
                print()
        else:
            print('Feed is empty')


@exception_wrapper()
def main_block():
    """Declares global variables.
    Takes arguments from commandline using get_args function.
    Creates logger.
    Parses news and displays them in proper format in stdout (text or json ),
    as well as .json file is being created while args.json option is set."""

    global args
    global logger

    args = get_args()

    if args.verbose:
        logging.basicConfig(level='NOTSET', stream=sys.stdout)
        logger = logging.getLogger()
    else:
        logging.basicConfig(level=80)

    allnews = parse_news(args.source)
    feed_list = cache_feed(allnews, args.source)[:args.limit]
    write_feed(feed_list, args.json)


if __name__ == "__main__":
    main_block()
