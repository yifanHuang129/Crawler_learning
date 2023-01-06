from html_test import html_list
import random
import requests
import time
import re
from bs4 import BeautifulSoup
from ua_info import ua_list
import os
import pandas as pd


class OSVspider(object):
    def __init__(self):
        self.osv_df = pd.DataFrame()
        self.cve_df = pd.DataFrame()
        self.osv_encounter = 1
        self.cve_encounter = 1

    def get_detail(self):
        """This function is used to get all the detail information under h1"""
        for html in html_list:
            soup = BeautifulSoup(html, 'html.parser')
            item = {}
            title = soup.find('h1', class_='title')
            title = self.get_text(title)
            item['title'] = title
            target = soup.find('dl', class_='vulnerability-details')
            dt_pattern = 'dt:nth-of-type({})'
            dd_pattern = 'dd:nth-of-type({})'
            i = 1
            while 1:
                check = target.select(dt_pattern.format(str(i)))
                if not check:
                    break
                name = self.get_text(check[0])

                if name == 'References':
                    raw_value = target.select(dd_pattern.format(str(i)))
                    value_list = raw_value[0].find_all('a', href=True)
                    value = self.optimization(value_list, 'h')
                else:
                    raw_value = target.select(dd_pattern.format(str(i)))
                    value = self.get_text(raw_value[0])
                item[name] = value
                i += 1
            self.get_more_detail(soup, item, title)

    def get_more_detail(self, soup, item, title):
        """This function is used to get all the detail information about package"""
        affected_package = soup.find('h2', class_='title')
        value = soup.find('h2', class_='package-header')
        if value:
            affected_package = self.get_text(affected_package)
            value = self.get_text(value)
            item[affected_package] = value
        else:
            item['Affected packages'] = ''

        """
        The following part  is used to fetch the detail information about affected ranges
        The affected ranges has such a format:
        Affected ranges:
        Type: A
        Event: (B, corresponding url)
        """
        name_list = soup.find_all('h3', class_='mdc-layout-grid__cell--span-3')
        raw_value = soup.find('div', class_='mdc-layout-grid__cell--span-9')
        if raw_value:
            affected_range = name_list[0]
            affected_range = self.get_text(affected_range)
            value = {}

            # get two sub_key_name
            sub_name_list = raw_value.find_all('dt')
            vul_type = sub_name_list[0]
            vul_type = self.get_text(vul_type)
            event = sub_name_list[1]
            event = self.get_text(event)

            # get the value for vul_type
            sub_value_list = raw_value.find_all('dd')
            vul_type_value = sub_value_list[0]
            vul_type_value = self.get_text(vul_type_value)
            value[vul_type] = vul_type_value

            # get the value for events
            element = sub_value_list[1]
            raw_status = element.find_all('div', class_='mdc-layout-grid__cell--span-3')
            status = self.optimization(raw_status, 't')
            raw_href = element.select('div.mdc-layout-grid__cell--span-9.version-value > a')
            href = self.optimization(raw_href, 'h')
            if not href:
                # combine the status and corresponding version
                version_list = element.select('div.mdc-layout-grid__cell--span-9.version-value')
                version = self.optimization(version_list, 't')
                event_value = list(zip(status, version))
            else:
                # combine the status and corresponding url
                event_value = list(zip(status, href))

            value[event] = event_value
            item[affected_range] = value
        else:
            item['Affected ranges'] = ''

        """
        The following part is used to fetch the detail information about affected versions and severity level
        The format:
        Affected version: [a list of affected versions]
        Severity: level
        """

        # The following part is used to get affected version
        raw_value = soup.find_all('div', class_='version')
        if raw_value:
            affected_version = name_list[1]
            affected_version = self.get_text(affected_version)
            value = self.optimization(raw_value, 't')
            item[affected_version] = value
        else:
            item['Affected version'] = ''

        # The following part is used to get severity level
        severity_info = soup.find('pre', class_='specific')
        if severity_info:
            severity_info = self.get_text(severity_info)
            severity_info = severity_info.replace('{', '')
            severity_info = severity_info.replace('}', '')
            severity_info = severity_info.strip()
            severity_info = severity_info.split(':')
            name = severity_info[0].replace('"', '')
            value = severity_info[1].replace('"', '')
            item[name] = value
        else:
            item['Severity'] = ''

        if 'OSV' in title:
            self.write_OSV(item)
        else:
            self.write_CVE(item)

    def write_OSV(self, item):
        if self.osv_encounter == 1:
            self.osv_df = pd.DataFrame.from_dict(item, orient='columns')
            self.osv_encounter += 1
        else:
            self.osv_df = pd.concat([self.osv_df, pd.DataFrame.from_dict(item, orient='columns')], ignore_index=True)

    def write_CVE(self, item):
        if self.cve_encounter == 1:
            self.cve_df = pd.DataFrame.from_dict(item, orient='index')
            self.osv_encounter += 1
        else:
            self.cve_df = pd.concat([self.cve_df, pd.DataFrame.from_dict(item, orient='index')], ignore_index=True)

    def save_data(self):
        path = './result/'
        OSV_path = os.path.join(path, 'OSV.csv')
        CVE_path = os.path.join(path, 'OSV_CVE.csv')
        self.osv_df.to_csv(OSV_path, encoding='utf-8', index=False)
        self.cve_df.to_csv(CVE_path, encoding='utf-8', index=False)

    def optimization(self, v_list, key):
        """
        key: t/h
        t stands for text
        h stands for href
        """
        optimized_value = []
        if key == 't':
            for v in v_list:
                ov = v.text.strip()
                optimized_value.append(ov)
        if key == 'h':
            for v in v_list:
                hv = v['href']
                optimized_value.append(hv)
        return optimized_value

    def get_text(self, target):
        return target.text.strip()

    def run(self):
        self.get_detail()
        self.save_data()


if __name__ == '__main__':
    start = time.time()
    agent = OSVspider()
    agent.run()
    end = time.time()
