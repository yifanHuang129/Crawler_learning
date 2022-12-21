import random
from urllib import request
from crawler.tutorial import ua_info

# response = request.urlopen('https://httpbin.org/get')
#
# html = response.read().decode()
# print(html)

url = 'https://httpbin.org/get'
header = random.sample(ua_info.ua_list, 1)[0]
headers = {
    'User-Agent':header
}

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

print(html)

