from unittest import TestCase, main
from RSS_reader import get_args, cache_feed, write_feed, read_cache
from bs4 import BeautifulSoup
from test_data import RSS, CACHE


class RssReaderTest(TestCase):
    def test_get_agrs(self):
        self.assertIsNone(get_args().source)
        self.assertFalse(get_args().json)
        self.assertFalse(get_args().verbose)
        self.assertIsNone(get_args().limit)
        self.assertIsNone(get_args().date)

    def test_cache_feed(self):
        allnews = BeautifulSoup(RSS, 'xml')
        source = 'https://onliner.by/feed'
        self.assertEqual(cache_feed(allnews, source), CACHE)

    def test_write_feed(self):
        self.assertIsNone(write_feed([{'a': 'b'}]))

    def test_read_cache(self):
        Title = 'В России сделали вакцину «Спутник», которую надо закапывать в нос'
        self.assertEqual(read_cache(None, '20211026', 1, 'test_cache.json')[0]['Title'], Title)


if __name__ == '__main__':
    main()
