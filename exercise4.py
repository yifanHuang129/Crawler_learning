import os
from ua_info import ua_list
import random
import time
import requests
from lxml.html import etree
import pandas as pd


class secondhandSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}'
        self.time = 1
        self.count = 1

    def get_header(self):
        headers = {
            'User-Agent': random.choice(ua_list)
        }
        return headers

    def get_html(self, url):
        if self.time < 5:
            try:
                res = requests.get(url=url, headers=self.get_header(), timeout=5)
                html = res.text
                return html
            except Exception as e:
                print(e)
                self.time += 1
                self.get_html(url)


    def parse_html(self, url):
        html = self.get_html(url)
        if html:
            p = etree.HTML(html)
            h_list = p.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
            df = pd.DataFrame()
            for h in h_list:
                item = {}
                name_list = h.xpath('.//a[@data-el="region"]/text()')
                item['name'] = [name_list[0].strip()] if name_list else None
                detail_list = h.xpath('.//div[@class="houseInfo"]/text()')
                if detail_list:
                    L = detail_list[0].split("|")
                    if L:
                        item['model'] = [L[0].strip()]
                        item['area'] = [L[1].strip()]
                        item['direction'] = [L[2].strip()]
                        item['perfect'] = [L[3].strip()]
                        item['floor'] = [L[4].strip()]

                address_list = h.xpath('.//div[@class="positionInfo"]/a/text()')
                item['address'] = address_list[0].strip()
                totalPrice_list = h.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')
                unitPrice_list = h.xpath('.//div[@class="unitPrice"]/span/text()')
                item['total price'] = [totalPrice_list[0].strip()] if totalPrice_list else None
                item['unit price'] = [unitPrice_list[0].strip()] if unitPrice_list else None
                csv_File = "./result/exercise4.csv"
                if self.count == 1:
                    df = pd.DataFrame(item)
                    self.count += 1
                else:
                    df = pd.concat([df, pd.DataFrame(item)], ignore_index=True)

            try:
                if os.path.exists(csv_File):
                    df.to_csv(csv_File, mode='a', encoding='utf-8', index=False)
                else:
                    df.to_csv(csv_File, encoding='utf-8', index=False)
                self.count = 1
            except IOError:
                print('IO error')

    def run(self):
        try:
            for i in range(1, 101):
                url = self.url.format(i)
                self.parse_html(url)
                time.sleep(random.randint(1, 3))
        except Exception as e:
            print('Error occurs: ', e)


if __name__ == '__main__':
    start = time.time()
    agent = secondhandSpider()
    agent.run()
    end = time.time()
    print('Total cost: ', end - start)
