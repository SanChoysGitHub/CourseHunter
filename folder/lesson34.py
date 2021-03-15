# Beautiful soup 4 * Parsing Sport Site *

from bs4 import BeautifulSoup
import urllib.request

# req = urllib.request.urlopen('https://www.ua-football.com/sport')  # Open URL address
# html = req.read()  # Reading HTML-file
#
# soup = BeautifulSoup(html, 'html.parser')
# news = soup.find_all('li', class_='liga-news-item')
#
# results = []
# domain = 'https://www.ua-football.com'
#
# for item in news:
#     title = item.find('span', class_='d-block').get_text(strip=True)  # Parsing title
#     desc = item.find('span', class_='name-dop').get_text(strip=True)  # Parsing description
#     href = item.a.get('href')  # Parsing link
#     results.append({  # Dictionary with information about sport-site
#         'title': title,
#         'desc': desc,
#         'href': href,
#     })
#
#
#
# f = open('news.txt', 'w', encoding='utf-8')  # Create or add information on file
# num = 1
# for item in results:
#     f.write(f'\nНовость № {num}\n\n\t
#     Title: {item["title"]}\n\tDescription: {item["desc"]}\n\tLink: {domain}{item["href"]}\n**\n')
#     num += 1


req = urllib.request.urlopen('https://www.ua-football.com/sport')  # Open URL address
html = req.read()  # Reading HTML-file

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='liga-news-item')

results = []
domain = 'https://www.ua-football.com'


def parsing_site():
    for item in news:
        title = item.find('span', class_='d-block').get_text(strip=True)  # Parsing title
        desc = item.find('span', class_='name-dop').get_text(strip=True)  # Parsing description
        href = item.a.get('href')  # Parsing link
        results.append({  # Dictionary with information about sport-site
            'title': title,
            'desc': desc,
            'href': href,
        })


def add_dict():
    f = open('news.txt', 'w', encoding='utf-8')  # Create or add information on file
    num = 1
    return(f.write(f'\nНовость № {num}'f'\n\n\tTitle: {item["title"]}\n\tDescription: {item["desc"]}\n\tLink: {domain}{item["href"]}\n**\n') for item in results)


parsing_site()
add_dict()




