from bs4 import BeautifulSoup
import re

# html_doc = """
# <html><head><title>"c语言中文网"</title></head>
# <body>
# <p class="title"><b>c.biancheng.net</b></p>
# <p class="website">一个学习编程的网站</p>
# <a href="http://c.biancheng.net/python/" id="link1">python教程</a>
# <a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())


soup = BeautifulSoup('<p class="Web site url"><b>c.biancheng.net</b></p>', 'html.parser')
# print(soup.p)
# print(soup.p.b)
# print(soup.p.text)
# print(soup.p.attrs)
# print(type(soup.p))
# print(type(soup.p.b))
# print(soup.p['class'])
# soup.p['class'] = ['customer', 'yifan']
# print(soup.p)
#
# soup = BeautifulSoup(html_doc, 'html.parser')
# body_tag = soup.body
# print(body_tag)
# print()
# print(body_tag.contents)
# for child in body_tag.children:
#     print(child)

# html_doc = """
# <html><head><title>"c语言中文网"</title></head>
# <body>
# <p class="title"><b>c.biancheng.net</b></p>
# <p class="website">一个学习编程的网站</p>
# <a href="http://c.biancheng.net/python/" id="link1">python教程</a>
# <a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
# <a href="http://c.biancheng.net/django/" id="link3">django教程</a>
# <p class="vip">加入我们阅读所有教程</p>
# <a href="http://vip.biancheng.net/?from=index" id="link4">成为vip</a>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.find_all('a'))
# print(soup.find_all('a', limit=2))
# print(soup.find_all('p', class_='website'))
# print(soup.find_all(id='link4'))
#
# print(soup.find_all(['a', 'b']))
# print(soup.find_all('a', id=re.compile(r'.\d')))
# print(soup.find_all(id=True))
# for tag in soup.find_all(True):
#     print(tag.name, end=" ")

# for tag in soup.find_all(re.compile('^b')):
#     print(tag)

# print(soup.find('a'))
# print(soup.find('title'))
# print(soup.find(class_=re.compile('tit')))
# print(soup.find(attrs={'class': 'vip'}))

html_doc = """
<html><head><title>"happy new year"</title></head>
<body>
<p class="title"><b>c.biancheng.net</b></p>
<p class="website">2022 is last year</p>
<a href="http://c.biancheng.net/python/" id="link1">2023 is the new year</a>
<a href="http://c.biancheng.net/c/" id="link2">hope you will be better</a>
<a href="http://c.biancheng.net/django/" id="link3">achieve more</a>
<p class="vip">加入我们阅读所有教程</p>
<a href="http://vip.biancheng.net/?from=index" id="link4">and realize your dream</a>
<p class="introduce">介绍:
<a href="http://c.biancheng.net/view/8066.html" id="link5">best</a>
<a href="http://c.biancheng.net/view/8092.html" id="link6">wishes</a>
</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
a = soup.select('p')
# a = soup.find('p', class_='introduce').text
print(a)
# print(soup.select('title'))
# b = soup.find('a', id='link1')
# print(soup.select('a[href]'))
# print(b['href'])
# print(soup.find('p', class_='vip').text)
# print(soup.select('#link1'))
# print(soup.select('html head title'))
# print(soup.select('p + a'))
# print(soup.select('p ~ a:nth-of-type(4)'))
print(soup.select('p ~ .introduce > a'))

