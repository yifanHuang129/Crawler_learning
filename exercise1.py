import random
from urllib import request
from urllib import parse
from ua_info import ua_list
import os.path

query_string = {
    'wd' : '色图'
}

result = parse.urlencode(query_string)
url = "http://www.baidu.com/s?{}".format(result)

headers = {
    'User-Agent': random.sample(ua_list, 1)[0]
}

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

save_path = "/Users/yifanhuang/PycharmProjects/pythonProject/crawler/tutorial/result"
name_of_file = "exercise1"
fileName = os.path.join(save_path, name_of_file+".html")
with open(fileName, 'w', encoding='utf-8') as f:
    f.write(html)
