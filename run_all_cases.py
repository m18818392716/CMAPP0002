#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 21:50
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : run_main.py
# @Software: PyCharm
import subprocess

import openpyxl
import pytest
import allure

from base.base_page import BasePage
from config.driver_config import appium_desired
from pages.login_page import LoginPage
from utils import run_case
from utils.operation_excel import readExcel
from utils.read_data_from_excel import read_data_from_excel

# excel = openpyxl.load_workbook('./data/data_excel/test_login.xlsx')
# sheet1 = excel['login_case']
# sheet2 = excel['login_step']
# print(sheet1)
# print(sheet2)

@allure.feature("测试TestLogin")
class TestLogin(object):

    @allure.step("执行Excel数据驱动")
    @pytest.mark.android
    @pytest.mark.parametrize("args", read_data_from_excel('./data/data_excel/test_login.xlsx', 'login_case', 'login_step'))
    # @pytest.mark.parametrize("args", readExcel('./data/data_excel/test_login.xlsx', 'login_case').get_case_step())
    # @pytest.mark.parametrize("args", readExcel('./data/data_excel/test_login.xlsx', 'login_case').get_case_step(), ids=['test1', 'test2'], name="测试登录流程")
    # @pytest.mark.parametrize(readExcel('./data/data_excel/test_login.xlsx', 'login_case').get_case_step(), name="测试登录流程")
    def test_001(self, start_app, args):

        self.driver = start_app
        self.lp = LoginPage(self.driver)
        # 执行测试用例下面的每一个操作步骤
        run_case.run_case_step(self.lp, args)

        # for step in args:
        #
        #     # 定义一个字典参数，用于接收excel中的所有参数内容
        #     args1 = {}
        #     # 用例编号
        #     args1['case_id'] = step['用例编号']
        #     # 步骤编号
        #     args1['step_id'] = step['步骤编号']
        #     # 定位方法
        #     args1['name'] = step['定位方法']
        #     # 定位路径
        #     args1['value'] = step['元素路径']
        #     # 输入内容
        #     args1['txt'] = step['输入内容']
        #     # 预期结果
        #     args1['expect'] = step['预期结果']
        #
        #     # 基于A列进行判断是否为测试用例
        #     if (str(step['步骤编号']).startswith('step_')):
        #         '''
        #             在读取关键字时，分为几类情况：
        #                 1. 关键字驱动类的实例化
        #                 2. 断言类型的关键字
        #         '''
        #         print("继续操作")
        #         # 判断是否实例化
        #         if step['事件'] == 'start_app':
        #             pass
        #         # 非特殊关键字，通过反射机制实现
        #         else:
        #             print("进入主程序")
        #             getattr(self.lp, step['事件'])(**args1)
        #             # getattr(wk, 'open')(**args)
        #             # wk.open(**args)
        #             # 原有的open函数是 def open(self,url):
        #             '''
        #                 如果是open，只需要传入value[4]
        #                 如果是input，则需要传入value[2],value[3],value[4]
        #                 如果是click，则需要传入value[2],value[3]
        #                 **args不定长传参，不定义参数数量的多少，说白了就是一个字典格式
        #                 但是字典是键值对形式存在
        #             '''
        # print("执行完毕！")



    #     case_list = []
    #     # 读取excel内容，实现文件驱动自动化执行
    #     for value in sheet1.values:
    #         # 定义一个字典参数，用于接收excel中的所有参数内容
    #         args = {}
    #         # 用例编号
    #         args['case_id'] = value[0]
    #         # 用例名称
    #         args['case_name'] = value[1]
    #         # 是否运行
    #         args['is_run'] = value[2]
    #
    #         if args['is_run'] == 'Yes':
    #             case_list.append(args['case_id'])
    #         else:
    #             pass
    #
    #     for i in case_list:
    #
    #     for value in sheet2.values:
    #         # 定义一个字典参数，用于接收excel中的所有参数内容
    #         args = {}
    #         # 用例编号
    #         args['case_id'] = value[0]
    #         # 步骤编号
    #         args['step_id'] = value[1]
    #         # 定位方法
    #         args['name'] = value[3]
    #         # 定位路径
    #         args['value'] = value[4]
    #         # 输入内容
    #         args['txt'] = value[5]
    #         # 预期结果
    #         args['expect'] = value[7]
    #
    #         if args['case_id'] in case_list:
    #
    #             # 基于A列进行判断是否为测试用例
    #             if (str(value[1]).startswith('step_')):
    #                 '''
    #                     在读取关键字时，分为几类情况：
    #                         1. 关键字驱动类的实例化
    #                         2. 断言类型的关键字
    #                 '''
    #                 print("继续操作")
    #                 # 判断是否实例化
    #                 if value[2] == 'start_app':
    #                     pass
    #                 # 非特殊关键字，通过反射机制实现
    #                 else:
    #                     print("进入主程序")
    #                     getattr(self.lp, value[2])(**args)
    #                     # getattr(wk, 'open')(**args)
    #                     # wk.open(**args)
    #                     # 原有的open函数是 def open(self,url):
    #                     '''
    #                         如果是open，只需要传入value[4]
    #                         如果是input，则需要传入value[2],value[3],value[4]
    #                         如果是click，则需要传入value[2],value[3]
    #                         **args不定长传参，不定义参数数量的多少，说白了就是一个字典格式
    #                         但是字典是键值对形式存在
    #                     '''
    #
    #     print("执行完毕！")
    #
    # def test_002(self):
    #     print("test 002")
    #
    # def test_003(self):
    #     print("test 003")
    #
    # def test_004(self):
    #     print("test 004")

def invoke(md):
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o

if __name__ == '__main__':
    xml_report_path = './allure-result/xml'
    html_report_path = './allure-report/html'
    # pytest.main(["-s", "run_all_cases.py", "./cases/test_fish_case.py"])
    args = ['-s', '-q', "run_all_cases.py"]
    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    invoke(cmd)
    # dt = DataTest()
    # dt.run()