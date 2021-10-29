RSS_reader.py is a one-shot RSS-parser a command-line utility which receives RSS URL and prints results in human-readable format.
An exaple of the result is displayed below:
verion 1.1

$ RSS_reader.py https://onliner.by/feed

RSS:            Onliner
RSS link:       https://onliner.by/feed

Title:          Астрономы, кажется, увидели первую планету вне нашей галактики
News link:      https://tech.onliner.by/2021/10/27/astronomy-kazhetsya-uvideli-pervuyu-planetu-vne-nashej-galaktiki
Published:      2021-10-27
Image source:   https://content.onliner.by/news/thumbnail/f8c62e44ce920b972fe6098243e4698e.jpeg
Description:    Астрономы обнаружили намеки на то, что может быть первой планетой за пределами нашей галактики, которую человечество сумело разглядеть. Око
ло 5000 экзопланет мы знаем сейчас за пределами Солнечной системы, но все они находятся в галактике Млечный путь. А столь далеких соседей по Вселенной мы е
ще не видели.Читать далее…

usage: RSS_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                     source

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     shows this help message and exit
  --version      Prints version info
  --json         Prints result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limits news topics if this parameter provided
  
In case of using --json argument utility converts the news into JSON format. 
JSON structure of data in this case is the following:
it comprises as list, containing dictionaries, each corresponding to separate news.
The example structure is provided below:
[
	{
	'RSS':            'Onliner'
	'RSS link':       'https://onliner.by/feed'
	'Title':          'Астрономы, кажется, увидели первую планету вне нашей галактики'
	'News link':      'https://tech.onliner.by/2021/10/27/astronomy-kazhetsya-uvideli-pervuyu-planetu-vne-nashej-galaktiki'
	'Published':      '2021-10-27'
	'Image source':   'https://content.onliner.by/news/thumbnail/f8c62e44ce920b972fe6098243e4698e.jpeg'
	'Description':    'Астрономы обнаружили намеки на то, что может быть первой планетой за пределами нашей галактики, которую человечество сумело разглядеть. Око
ло 5000 экзопланет мы знаем сейчас за пределами Солнечной системы, но все они находятся в галактике Млечный путь. А столь далеких соседей по Вселенной мы е
ще не видели.Читать далее…'
	},
	{
		...
		
	},
	...,
]
With the argument --verbose set the program prints logs in stdout.

