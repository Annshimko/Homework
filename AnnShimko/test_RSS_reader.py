from unittest import TestCase, main
from RSS_reader import get_args
from RSS_reader import cache_feed
from RSS_reader import write_feed
from bs4 import BeautifulSoup
from test_data import RSS, CACHE


class RSS_Reader_Test(TestCase):
    def test_cache_feed(self):
        allnews = BeautifulSoup(RSS, 'xml')
        source = 'https://onliner.by/feed'
        self.assertEqual(cache_feed(allnews, source), CACHE)

    def test_write_feed(self):
        self.assertIsNone(write_feed([{'a': 'b'}]))


if __name__ == '__main__':
    main()
