# -*- coding: utf-8 -*-
from hstest import dynamic_test

from test.base import HyperCarTest

class HyperServiceTestRunner(HyperCarTest):

    funcs = [
        # 1 task
        HyperCarTest.check_main_header,

        # 2 task
        HyperCarTest.check_menu_page_links,
    ]

    @dynamic_test(data=funcs)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    HyperServiceTestRunner().run_tests()

