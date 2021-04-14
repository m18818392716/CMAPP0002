#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 21:48
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : test_search_case.py
# @Software: PyCharm
import allure
import openpyxl
import pytest

from pages.search_page import SearchPage

excel = openpyxl.load_workbook('./data/data_excel/test_search.xlsx')
sheet = excel['search_page']
print(sheet)

@allure.feature("测试TestSearch测试用例")
class TestSearch(object):

    @allure.step("执行Excel数据驱动")
    @pytest.mark.android
    def test_001(self, start_app):

        self.driver = start_app
        self.sp = SearchPage(self.driver)

        # 读取excel内容，实现文件驱动自动化执行
        for value in sheet.values:
            # 定义一个字典参数，用于接收excel中的所有参数内容
            args = {}
            # 定位方法
            args['name'] = value[2]
            # 定位路径
            args['value'] = value[3]
            # 输入内容
            args['txt'] = value[4]
            # 预期结果
            args['expect'] = value[6]
            # 基于A列进行判断是否为测试用例
            if type(value[0]) is int:
                '''
                    在读取关键字时，分为几类情况：
                        1. 关键字驱动类的实例化
                        2. 断言类型的关键字
                '''
                print("继续操作")
                # 判断是否实例化
                if value[1] == 'start_app':
                    pass
                # 非特殊关键字，通过反射机制实现
                else:
                    print("进入主程序")
                    getattr(self.sp, value[1])(**args)
                    # getattr(wk, 'open')(**args)
                    # wk.open(**args)
                    # 原有的open函数是 def open(self,url):
                    '''
                        如果是open，只需要传入value[4]
                        如果是input，则需要传入value[2],value[3],value[4]
                        如果是click，则需要传入value[2],value[3]
                        **args不定长传参，不定义参数数量的多少，说白了就是一个字典格式
                        但是字典是键值对形式存在
                    '''

        print("执行完毕！")