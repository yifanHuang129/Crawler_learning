import random
from os import path
import requests
from ua_info import ua_list

url = 'https://img1.baidu.com/it/u=4003632682,3273526998&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500'
headers = {'User-Agent': random.choice(ua_list)}
html = requests.get(url=url, headers=headers).content

Path = "/Users/yifanhuang/PycharmProjects/pythonProject/crawler/tutorial/result"
fileName = "RequestsResult"

savePath = path.join(Path, fileName+".jpg")

with open(savePath, "wb") as f:
    f.write(html)