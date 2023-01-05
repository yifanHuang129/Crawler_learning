from html_test import html_list
import random
import requests
import time
import re
from bs4 import BeautifulSoup
from ua_info import ua_list


class OSVspider(object):
    def get_detail(self):
        """This function is used to get all the detail information under h1"""
        html = html_list[0]
        soup = BeautifulSoup(html, 'html.parser')
        item = {}
        title = soup.find('h1', class_='title').text
        item['title'] = title
        if 'OSV' in title:
            self.get_osv_detail(item, soup)
        else:
            self.get_GHSA_detail(item, soup)

    def get_osv_detail(self, item, soup):
        target = soup.find('dl', class_='vulnerability-details')
        dt_pattern = 'dt:nth-of-type({})'
        dd_pattern = 'dd:nth-of-type({})'
        i = 1
        while 1:
            check = target.select(dt_pattern.format(str(i)))
            if not check:
                break
            raw_name = str(check[0])
            dt_reg = '<dt>(.*?)</dt>'
            name = re.compile(dt_reg, re.S).findall(raw_name)[0]
            if name == 'Details':
                value_list = target.find_all(['p', 'code'])
                value = []
                for v in value_list:
                    value.append(v.text.strip())

            elif name == 'References':
                raw_value = target.select(dd_pattern.format(str(i)))[0]
                value = raw_value.find('a', href=True).text
            else:
                raw_value = str(target.select(dd_pattern.format(str(i)))[0])
                dd_reg = '<dd>(.*?)</dd>'
                value = re.compile(dd_reg, re.S).findall(raw_value)[0]
            if i == 1:
                value = re.compile('<a href.*?>(.*?)</a>', re.S).findall(value)[0]
            item[name] = value
            i += 1
        self.get_more_detail(soup, item)

    def get_more_detail(self, soup, item):
        """This function is used to get all the detail information about package"""
        affected_package = soup.find('h2', class_='title').text.strip()
        value = soup.find('h2', class_='package-header').text.strip()
        item[affected_package] = value

        """
        The following part  is used to fetch the detail information about affected ranges
        The affected ranges has such a format:
        Affected ranges:
        Type: A
        Event: B, corresponding url
        """
        name_list = soup.find_all('h3', class_='mdc-layout-grid__cell--span-3')
        affected_range = name_list[0].text.strip()
        raw_value_1 = soup.find('div', class_='mdc-layout-grid__cell--span-9')
        value = {}
        sub_name_list = raw_value_1.find_all('dt')
        sub_name1 = sub_name_list[0].text.strip()
        sub_name2 = sub_name_list[1].text.strip()
        sub_value_list = raw_value_1.find_all('dd')
        sub_value1 = sub_value_list[0].text.strip()
        sub_value2 = []

        for i in range(1, len(sub_value_list)):
            element = sub_value_list[i]
            



        # sub_value2_1 = sub_value_list[1].find('div', class_='mdc-layout-grid__cell--span-3').text.strip()
        # sub_value2_2 = sub_value_list[1].select('div ~ .mdc-layout-grid__cell--span-9, .version-value > a')[1]['href']
        # sub_value2.append(sub_value2_1)
        # sub_value2.append(sub_value2_2)
        # value[sub_name1] = sub_value1
        # value[sub_name2] = sub_value2
        item[affected_range] = value

        """
        The following part is used to fetch the detail information about affected versions and severity level
        The format:
        Affected version: [a list of affected versions]
        Severity: level
        """

        # The following part is used to get affected version
        affected_version = name_list[1].text.strip()
        raw_value = soup.find_all('div', class_='version')

        def optimization(v_list):
            optimized_value = []
            for v in v_list:
                ov = v.text
                optimized_value.append(ov)
            return optimized_value

        value = optimization(raw_value)
        item[affected_version] = value

        # The following part is used to get severity level
        if name_list[2]:
            severity_info = soup.find('pre', class_='specific').text.strip()
            severity_info = severity_info.replace('{', '')
            severity_info = severity_info.replace('}', '')
            severity_info = severity_info.strip()
            severity_info = severity_info.split(':')
            name = severity_info[0].replace('"', '')
            value = severity_info[1].replace('"', '')
            item[name] = value

            pass

if __name__ == '__main__':
    start = time.time()
    agent = OSVspider()
    agent.get_detail()
    end = time.time()
