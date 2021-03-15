from classes import Parser

parser = Parser('https://www.ua-football.com/sport',
                'news.txt',
                'li', 'liga-news-item',
                'span', 'd-block',
                )
parser.run()
# print(parser.raw_html)
# print(parser.html)
print(parser.results)

