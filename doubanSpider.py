import requests
import time
import random
from ua_info import ua_list
import json
import re
import pandas as pd

class doubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.i = 0
        self.df = pd.DataFrame()

    def get_headers(self):
        headers = {'User-Agent': random.choice(ua_list)}
        return headers

    def get_page(self, param):
        res = requests.get(url=self.url, params=param, headers=self.get_headers())
        html = res.text
        html = json.loads(html)
        self.parse_page(html)

    def parse_page(self, html):
        item = {}
        for one in html:
            item['name'] = one['title'].strip()
            item['rate'] = one['score'].strip()
            item['regions'] = one['regions']
            item['star'] = one['actors']
            self.i += 1
            self.write_page(item)

    def write_page(self, item):
        if self.i == 1:
            self.df = pd.DataFrame.from_dict(item, orient='index')
        else:
            self.df = pd.concat([self.df, pd.DataFrame.from_dict(item, orient='index')], ignore_index=True)

    def save_page(self):
        path = "./result/doubanSpider.csv"
        self.df.to_csv(path, encoding='utf-8', index=False)

    def total_number(self, type_number):
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type_number)
        res = requests.get(url=url, headers=self.get_headers())
        html = res.json()
        total = int(html['total'])
        return total

    def get_all_type_films(self):
        url = 'https://movie.douban.com/chart'
        headers = self.get_headers()
        html = requests.get(url=url, headers=headers).text
        re_bds = r'<a href.*?type_name=(.*?)&type=(.*?)&.*?</a>'
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        type_dict = {}
        menu = ''
        for r in r_list:
            type_dict[r[0].strip()] = r[1].strip()
            menu += r[0].strip() + '|'

        return type_dict

    def run(self):
        type_dict = self.get_all_type_films()
        for key in type_dict:
            type_number = type_dict[key]
            total_number = self.total_number(type_number)
            for start in range(0, (total_number+1), 20):
                params = {
                    'type': type_number,
                    'interval_id': "100:90",
                    'action': "",
                    'start': str(start),
                    'limit': 20
                }
                self.get_page(params)
                time.sleep(random.randint(1, 3))

        print("Total movie number is %d" %self.i)
        self.save_page()

if __name__ == '__main__':
    start = time.time()
    agent = doubanSpider()
    agent.run()
    end = time.time()
    print("Total cost: ", end-start)