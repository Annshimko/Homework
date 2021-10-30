RSS_reader.py is a one-shot RSS-parser a command-line utility which receives RSS URL and prints results in human-readable format.
An exaple of the result is displayed below:
version 4.0

$ RSS_reader.py https://onliner.by/feed

RSS:            Onliner
RSS link:       https://onliner.by/feed

Title:          Назван новый предок человека, живший полмиллиона лет назад
News link:      https://tech.onliner.by/2021/10/29/nazvan-novyj-predok-cheloveka-zhivshij-polmilliona-let-nazad
Published:      2021-10-29
Image source:   https://content.onliner.by/news/thumbnail/b391f5663552fe77f051a106ec64be15.jpeg
Description:    Проживавший на территории нынешней Эфиопии в среднем плейстоцене новый вид предка человека назвали Homo bodoensis. Об этом пишет Phys.org
, а полная научная статья опубликована в журнале Evolutionary Anthropology Issues News and Reviews.Читать далее…


usage: RSS_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                     source

Pure Python command-line RSS reader.


optional arguments:
  --source         RSS URL
  -h, --help     shows this help message and exit
  --version      Prints version info
  --json         Prints result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limits news topics if this parameter provided
  --date DATE 	 provides the possibility to search cached news by date in %Y%m%d format,
		 if no --source argument provided, searches by date through all sources in cache.
  --tohtml	 converts the feed into html format
  --topdf	 converts the feed into pdf format
  
In case of using --json argument utility converts the news into JSON format. 
JSON structure of data in this case is the following:
it comprises as list, containing dictionaries, each corresponding to separate news.
The example structure is provided below:
[
  {
  'RSS':'Onliner'
  'RSS link':'https://onliner.by/feed'
  'Title':'Назван новый предок человека, живший полмиллиона лет назад'
  'News link':'https://tech.onliner.by/2021/10/29/nazvan-novyj-predok-cheloveka-zhivshij-polmilliona-let-nazad'
  'Published':'2021-10-29'
  'Image source':'[('https://content.onliner.by/news/thumbnail/b391f5663552fe77f051a106ec64be15.jpeg', 'images/content.onliner.bynewsthumbnailb391f566355
2fe77f051a106ec64be15.jpeg')]'
  'Description':'Проживавший на территории нынешней Эфиопии в среднем плейстоцене новый вид предка человека назвали Homo bodoensis. Об этом пишет Phys.or
g, а полная научная статья опубликована в журнале Evolutionary Anthropology Issues News and Reviews.Читать далее…'
 },
,
	{
		...
		
	},
	..
]
With the argument --verbose set the program prints logs in stdout.

There's news caching function implemented in version 3.0. News are kept in a local storage in cache.json file in JSON data format.
While reading the feed once, all news feed is being cached. 
Later, during RSS_reader execution existing cache is compared with the feed and upcoming news is added. 
Simultaneously, feed images are cached into "images" folder.

Using --date argument news can be searched by date from cache. The date should be provided in %Y%m%d format, for example: 20211029.
If no --source provided, the search is performed through all sources for this date. 
--date mode works with files, stored in local folders created while news caching.
--date mode doesn't requre Internet connection.

--tohtml and --topdf arguments allows to convert the feed into html and pdf formats correspondingly, including images in the body of the news field.


Installation and setup:

Windows:
C:\Users\...\dist> py -3 -m pip install RSS_reader-4.0.tar.gz
Unix-like OS:
.../dist$ sudo python3 -m pip install RSS_reader-4.0.tar.gz
