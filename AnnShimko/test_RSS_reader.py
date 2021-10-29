from unittest import TestCase, main
from RSS_reader import get_args, convert2html, cache_feed, write_feed, read_cache, convert2pdf
from bs4 import BeautifulSoup
from test_data import RSS, CACHE
import shutil
import os
import filecmp


class RssReaderTest(TestCase):
    def test_get_agrs(self):
        self.assertIsNone(get_args().source)
        self.assertFalse(get_args().json)
        self.assertFalse(get_args().verbose)
        self.assertIsNone(get_args().limit)
        self.assertIsNone(get_args().date)
        self.assertFalse(get_args().tohtml)
        self.assertFalse(get_args().topdf)

    def test_cache_feed(self):
        allnews = BeautifulSoup(RSS, 'xml')
        source = 'https://onliner.by/feed'
        self.assertEqual(cache_feed(allnews, source), CACHE)

    def test_write_feed(self):
        self.assertIsNone(write_feed([{'a': 'b'}]))

    def test_read_cache(self):
        Title = 'В России сделали вакцину «Спутник», которую надо закапывать в нос'
        self.assertEqual(read_cache(None, '20211026', 1, 'test_cache.json')[0]['Title'], Title)

    def test_convert_html(self):
        shutil.rmtree('html_files')
        convert2html(CACHE)
        files = os.listdir('html_files')
        assert len(files) == 1
        assert filecmp.cmp('test_news_feed.html', f'html_files/{files[0]}')

    def test_convert_pdf(self):
        shutil.rmtree('pdf_files')
        convert2pdf(CACHE)
        files = os.listdir('pdf_files')
        assert len(files) == 1
        # assert filecmp.cmp('test_news_feed.pdf', f'pdf_files/{files[0]}')

if __name__ == '__main__':
    main()
