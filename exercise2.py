import os.path
from urllib import request, parse
import time
import random
from ua_info import ua_list


class TiebaSpider(object):
    def __init__(self):
        self.url = "http://tieba.baidu.com/f?{}"

    def get_html(self, url):
        req = request.Request(url=url, headers={"User-Agent": random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

    def parse_html(self):
        pass

    def write_html(self, path, fileName, html):
        filePath = os.path.join(path, fileName + ".html")
        with open(filePath, "w", encoding="utf-8") as f:
            f.write(html)

    def run(self):
        name = "英雄联盟"
        begin = 1
        end = 10

        for page in range(begin, end + 1):
            pn = (page - 1) * 50
            params = {
                'kw': name,
                'pn': str(pn)
            }
            params = parse.urlencode(params)
            url = self.url.format(params)
            html = self.get_html(url)
            path = "/Users/yifanhuang/PycharmProjects/pythonProject/crawler/tutorial/result/exercise2/"
            fileName = "{}-{}pages.html".format(begin, end)
            self.write_html(path, fileName, html)

            print("Successfully fetch page %d" % page)
            time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    start = time.time()
    spider = TiebaSpider()
    spider.run()
    end = time.time()
    print("execution time: %.2fs" % (end-start))