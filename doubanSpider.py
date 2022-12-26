import requests
import time
import random
from ua_info import ua_list
import re
import json

class doubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.time = 0

    def get_headers(self):
        headers = {'User-Agent': random.choice(ua_list)}
        return headers

    def get_pages(self, params):
        html = requests.get(url=self.url, params=params, headers=self.get_headers()).text
        html = json.loads(html)
        self.parse_page(html)

    def parse_page(self, html):
        item = {}
        for one in item:
            item['name'] = one['title'].strip()
            item['score']= float(one['score'].strip())
            print(item)
            self.i += 1

    def total_number(self, type_number):
        url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90'.format(type_number)
        headers = self.get_headers()
        html = requests.get(url = url, headers=headers).text
        re_bds = r'<a href.*?type_name=(.*?)&type=(.*?)&.*?</a>'
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        
