import os
import sys

import requests

from bs4 import BeautifulSoup
from config import BANKS_DICT, TEMP_PATH, URL

from Handlers.comparsion import Comparison
from Handlers.notification import Notification


class Parser(Comparison, Notification):

    def __init__(self):
        # if you want use proxy, uncomment and change *** on socks5
        # self.proxies = dict(http='socks5://***', https='socks5://***')

        super().__init__()
        self._count = 0
        self.session = requests.session()
        self.headers = {
            'Host': 'myfin.by',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Referer': 'https://myfin.by/currency/minsk'
        }
        self._html_text = None

    def __get_html_content(self):
        try:
            # with proxy
            # response = requests.get(self.url, headers=self.headers, verify=False, proxies=self.proxies)

            response = self.session.get(URL, headers=self.headers, verify=False)
        except Exception as e:
            self._count += 1
            self._call_error_server_connection_notification(error=str(e))
            if self._count < 3:
                return self.__get_html_content()
            else: sys.exit()

        if response.ok:
            self._html_text = BeautifulSoup(response.text, 'html5lib')
            with open(os.path.join(TEMP_PATH, 'result.html'), 'w', encoding='utf-8') as f:
                f.write(str(self._html_text))
        else:
            self._call_response_error(response=str(response.status_code))

    @staticmethod
    def __parse_table():
        with open(os.path.join(TEMP_PATH, 'result.html'), 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html5lib')
            table = soup.findAll('table', class_='rates-table-sort')
            my_table = table[0]

            with open(os.path.join(TEMP_PATH, 'result.txt'), 'w', encoding='utf-8') as f:
                rows = my_table.findChildren('tr')
                for row in rows:
                    cells = row.findChildren(['td', 'a'])
                    for cell in cells:
                        value = cell.text
                        f.write(value + '\n')

    def __parse_bank_and_course(self):
        with open(os.path.join(TEMP_PATH, 'result.txt'), 'r', encoding='utf-8') as f:
            file = f.readlines()

        for s in range(len(file)):
            search = file[s].replace('\n', '')
            for bank in BANKS_DICT.keys():
                if search == bank:
                    current_course = (float(file[s + 1].replace('\n', '')),
                                      float(file[s + 2].replace('\n', '')),
                                      float(file[s + 3].replace('\n', '')),
                                      float(file[s + 4].replace('\n', '')),
                                      float(file[s + 5].replace('\n', '')),
                                      float(file[s + 6].replace('\n', '')))
                    self._comparison_of_courses(BANKS_DICT[search], current_course)

    def __clear_temp(self):
        open(os.path.join(TEMP_PATH, 'result.html'), 'w', encoding='utf-8') as res_h:
        res_h.close()
        open(os.path.join(TEMP_PATH, 'result.txt'), 'w', encoding='utf-8') as res_t:
        res_t.close()


    def run_all(self):
        self.__get_html_content()
        self.__parse_table()
        self.__parse_bank_and_course()
        self._search_max_courses()
        self._search_min_courses()
        self.run_notification(self._min_course_dict, self._max_course_dict)
        self.__clear_temp()
