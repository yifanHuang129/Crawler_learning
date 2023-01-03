import random
import requests
import time
import re
from bs4 import BeautifulSoup
from ua_info import ua_list


class OSVspider(object):
    def __init__(self):
        self.url = 'https://osv.dev/list?{}'

    def get_headers(self):
        headers = {'User-Agent': random.choice(ua_list)}

    def get_html(self, url):
        html = requests.get(url=url, headers=self.get_headers(), timeout=5).text
        time.sleep(random.randint(1, 2))
        if html:
            self.parse_html(html)
            return True
        else:
            return False

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('a', href=re.compile(r'/vulnerability/.*?'))
        for item in a:
            if item.has_attr('href'):
                OSV_detail_url = item['href']
                url = 'https://osv.dev{}'.format(OSV_detail_url)
                self.get_detail(url)

    def get_detail(self, url):
        html = requests.get(url=url, headers=self.get_headers())
        time.sleep(random.randint(1, 2))
        soup = BeautifulSoup(html, 'html.parser')
        item = {}
        title = soup.select('h1', class_='title').text
        item['title'] = title
        dt_pattern = 'dl ~ .vulnerability-details > dt:nth-of-type({})'
        dd_pattern = 'dl ~ .vulnerability-details > dd:nth-of-type({})'
        i = 1
        while 1:
            name = soup.select(dt_pattern.format(i))
            if name == []:
                break
            value = soup.select(dd_pattern.format(i))
            item[name] = value
            i += 1
        pass

    def save_detail(self, html):
        pass

    def run(self):
        i = 1
        flag = True
        while (flag):
            url = self.url.format(i)
            flag = self.get_html(url)
            i += 1


if __name__ == '__main__':
    start = time.time()
    agent = OSVspider()
    agent.run()
    end = time.time()