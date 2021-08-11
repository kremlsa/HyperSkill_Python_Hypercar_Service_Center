# -*- coding: utf-8 -*-
import http.cookiejar
import io
import os
import re
import sqlite3
import urllib

import requests

from hstest import CheckResult, DjangoTest


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))



class HyperCarTest(DjangoTest):

    use_database = False

    COMMON_LINK_PATTERN = '''<a[^>]+href=['"]([a-zA-Z\d/_]+)['"][^>]*>'''
    CSRF_PATTERN = b'<input[^>]+name="csrfmiddlewaretoken" ' \
                   b'value="(?P<csrf>\w+)"[^>]*>'
    GROUPS_FIRST_PATTERN = '<h4>.*?</h4>.*?<ul>.+?</ul>'
    GROUPS_SECOND_PATTERN = (
        '''<a[^>]+href=['"]([a-zA-Z\d/_]+)['"][^>]*>(.+?)</a>'''
    )
    H2_PATTERN = '<h2>(.+?)</h2>'
    LINK_WITH_TEXT_PATTERN = '''<a[^>]+href=['"]([a-zA-Z\d/_?=]+)['"][^>]*>(.+?)</a>'''
    PARAGRAPH_PATTERN = '<p>(.+?)</p>'
    SRC_PATTERN = '''<source[^>]+src=['"]([a-zA-Z\d/_.]+)['"][^>]*>'''
    TEXT_LINK_PATTERN = '''<a[^>]+href=['"][a-zA-Z\d/_]+['"][^>]*>(.+?)</a>'''
    cookie_jar = http.cookiejar.CookieJar()
    USERNAME = 'Test'
    PASSWORD = 'TestPassword123'
    TAG = 'testtag'

    def check_main_header(self) -> CheckResult:
        try:
            page = self.read_page(self.get_url() + 'welcome/')
        except urllib.error.URLError:
            return CheckResult.wrong(
                'Cannot connect to the main page.'
            )

        h2_headers = re.findall(self.H2_PATTERN, page, re.S)
        h2_headers = self.__stripped_list(h2_headers)
        main_header = 'Welcome to the Hypercar Service!'

        is_main_header = False
        for h2_header in h2_headers:
            if main_header in h2_header:
                is_main_header = True
                break

        if not is_main_header:
            return CheckResult.wrong(
                'Main page should contain <h2> element with text "Welcome to the Hypercar Service!"'
            )

        return CheckResult.correct()

    def check_menu_page_links(self):

        menu_links = ["/get_ticket/change_oil","/get_ticket/inflate_tires","/get_ticket/diagnostic"]

        try:
            page = self.read_page(self.get_url() + 'menu/')
        except urllib.error.URLError:
            return CheckResult.wrong(
                'Cannot connect to the main page.'
            )

        links_from_page = re.findall(self.LINK_WITH_TEXT_PATTERN, page, re.S)
        links_from_page = self.__stripped_list_with_tuple(links_from_page)
        print(links_from_page)
        for link in menu_links:
            if link not in links_from_page:
                return CheckResult.wrong(
                    f'Menu page should contain <a> element with href {link}'
                )

        return CheckResult.correct()

    def __stripped_list(self, list):
        return [item.strip() for item in list]

    def __stripped_list_with_tuple(self, list):
        return [item[0].strip() for item in list]
