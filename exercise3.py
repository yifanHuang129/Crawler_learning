import csv
import os
import re
import ssl
from urllib import parse, request
from ua_info import ua_list
import random
import time


class maoyanSpider(object):
    def __init__(self):
        self.url = "https://maoyan.com/board/4?{}"

    def get_html(self, url):
        req = request.Request(url=url, headers={'User-Agent': random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

    def parse_html(self, html):
        regex = '<div class="movie-item-info".*?data-val.*?>(.*?).*?star">(.*?).*?time">上映时间:(.*?).*?div>'
        pattern = re.compile(regex)
        re_list = pattern.findall(html)
        return re_list

    def write_html(self, path, fileName, re_list):
        fileName = os.path.join(path, fileName + ".csv")
        with open(fileName, "w", encoding="uft-8") as f:
            writer = csv.writer(f)
            colName = ["Name", "Star", "Time"]
            writer.writerow(colName)
            for r in re_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                time = r[2].strip()[5:15]
                L = [name, star, time]
                writer.writerow(L)

    def run(self):
        start_page = 1
        end_page = 10
        for page in range(start_page, end_page + 1):
            pn = (page - 1) * 10
            params = {
                "offset": pn
            }
            params = parse.urlencode(params)
            url = self.url.format(params)
            if pn == 0:
                url = "https://maoyan.com/board/4"
            html = self.get_html(url)
            re_list = self.parse_html(html)
            path = "/Users/yifanhuang/PycharmProjects/pythonProject/crawler/tutorial/result/exercise3"
            fileName = "maoyan"
            self.write_html(path, fileName, re_list)

            print("successfully fetch page%d" % page)
            time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    start = time.time()
    spider = maoyanSpider()
    spider.run()
    end = time.time()
    print("Total execution time: ", end - start)
