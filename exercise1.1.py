import os.path
import random
from urllib import parse
from urllib import request
from crawler.tutorial.ua_info import ua_list


def get_url(word):
    query_string = {
        'wd': word
    }

    url = "http://www.baidu.com/s?{}".format(parse.urlencode(query_string))
    return url


def request_url(url, fileName):
    headers = {
        'User-Agent': random.sample(ua_list, 1)[0]
    }
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(html)


def generateFileName(savePath, fileName):
    fileName = os.path.join(savePath, fileName + ".html")
    return fileName


if __name__ == "__main__":
    word = "色图"
    path = "/Users/yifanhuang/PycharmProjects/pythonProject/crawler/tutorial/result"
    request_url(get_url(word), generateFileName(path, "result1.1"))
