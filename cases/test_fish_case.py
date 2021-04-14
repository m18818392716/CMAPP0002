#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 23:27
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : test_fish_case.py
# @Software: PyCharm
import allure
import pytest

from pages.fish_page import FishPage
from utils import run_case
from utils.read_data_from_excel import read_data_from_excel


@allure.feature("测试TestFish测试用例")
class TestFish(object):
    @allure.step("执行Excel数据驱动")
    @pytest.mark.android
    @pytest.mark.parametrize("test_fish_case",read_data_from_excel('./data/data_excel/test_login.xlsx', 'fish_case', 'fish_step'))
    # @pytest.mark.parametrize("args", readExcel('./data/data_excel/test_login.xlsx', 'login_case').get_case_step())
    # @pytest.mark.parametrize("args", readExcel('./data/data_excel/test_login.xlsx', 'login_case').get_case_step(), ids=['test1', 'test2'], name="测试登录流程")
    # @pytest.mark.parametrize(readExcel('./data/data_excel/test_login.xlsx', 'login_case').get_case_step(), name="测试登录流程")
    def test_001(self, start_app, test_fish_case):

        self.driver = start_app
        self.fp = FishPage(self.driver)

        # 执行测试用例下面的每一个操作步骤
        run_case.run_case_step(self.fp, test_fish_case)