from bs4 import BeautifulSoup
import urllib.request

# *************************************************************


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         print('Wrong age')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')


class Employee(Person):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def more_info(self):
        print(f'{self.name} works in {self.company}')

    def print_info(self):
        super().print_info()
        print(f'Company: {self.company}')

    def __str__(self):
        # return f'Name: {self.name}'
        return 'Class ' + self.__class__.__name__


class Car:
    def __init__(self, name):
        self.name = name
        self.year = 2015
        self.hp = 340
        self.color = 'Rainbow'

    def car_info(self):
        print(f'Car: {self.name},'
              f' Year: {self.year},'
              f' Horses_Power: {self.hp},'
              f' Color_Car : {self.color}'
              )

    @property
    def name_car(self):
        return self.name()


# ************************************************************


# class Parser:
#
#     def __init__(self, req):
#         self.req = req
#         # self.news = news
#
#     def open_url(self):
#         req = urllib.request.urlopen(self.req)
#         html = req.read()
#         print(html)
#         return html
#
#     def find_html(self, html):
#         soup = BeautifulSoup(html, 'html.parser')
#         news = soup.find_all('li', class_='liga-news-item')
#         return news
#
#     def parsing(self, news):
#         results = []
#         for item in news:
#             # kind_of_sport = item.find('span', class_='section-name').get_text(strip=True)
#             title = item.find('span', class_='fz-16').get_text(strip=True)
#             # desc = item.find('span', class_='name-dop').get_text(strip=True)
#             href = item.a.get('href')
#             results.append({
#                 # 'kind_of_sport': kind_of_sport,
#                 'title': title,
#                 # 'description': desc,
#                 'href': href,
#             })
#             print(title, href)
#         return results
#
#     def site_info(self, title, href):
#         print(f'Title: {title},'
#               f' Href: {href},'
#               )

# //////////////////////////////////////////////////////////////////

# class Parser:
#
#     raw_html = ''
#     html = ''
#     results = []
#
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         req = urllib.request.urlopen(self.url)
#         self.raw_html = req.read()
#         self.html = BeautifulSoup(self.raw_html, 'html.parser')
#
#     def parsing(self):
#         news = self.html.find_all('li', class_='liga-news-item')
#
#         for item in news:
#             title = item.find('span', class_='d-block').get_text(strip=True)
#             desc = item.find('span', class_='name-dop').get_text(strip=True)
#             href = item.a.get('href')
#             self.results.append({
#                 'title': title,
#                 'desc': desc,
#                 'href': href,
#             })
#
#     def save(self):
#         with open(self.path, 'w', encoding='utf-8') as f:
#             i = 1
#             for item in self.results:
#                 f.write(f'\nНовость № {i}'f'\n\n\tTitle: {item["title"]}'
#                         f'\n\tDescription: {item["desc"]}'
#                         f'\n\tLink: {item["href"]}\n*****************\n'
#                         )
#                 i += 1
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#         self.save()
# /*///*/*//*/*/*/*/*/*//*/*/*/*/*/*/*//*/*/*/*/*/*//*//*/*//*/


class Parser:

    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path, tag, tag_class, tag_title, tag_class_):
        self.url = url
        self.path = path
        self.tag = tag
        self.tag_class = tag_class
        self.tag_title = tag_title
        self.tag_class_ = tag_class_

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all(self.tag, self.tag_class)

        for item in news:
            title = item.find(self.tag_title, self.tag_class_).get_text(strip=True)
            desc = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'\nНовость № {i}'f'\n\n\tTitle: {item["title"]}'
                        f'\n\tDescription: {item["desc"]}'
                        f'\n\tLink: {item["href"]}\n*****************\n'
                        )
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()



