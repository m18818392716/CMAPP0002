# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# # @Time    : 2021/4/12 23:34
# # @Author  : Susanna
# # @Email   : m18818392716@163.com
# # @File    : run_case.py
# # @Software: PyCharm
# import openpyxl
#
#
# def run_case(path, sheetname):
#     excel = openpyxl.load_workbook('./data/data_excel/test_login.xlsx')
#     sheet = excel['Sheet4']
#     print(sheet)
#
#     # 读取excel内容，实现文件驱动自动化执行
#     for value in sheet.values:
#         # 定义一个字典参数，用于接收excel中的所有参数内容
#         args = {}
#         # 定位方法
#         args['name'] = value[2]
#         # 定位路径
#         args['value'] = value[3]
#         # 输入内容
#         args['txt'] = value[4]
#         # 预期结果
#         args['expect'] = value[6]
#         # 基于A列进行判断是否为测试用例
#         if type(value[0]) is int:
#             '''
#                 在读取关键字时，分为几类情况：
#                     1. 关键字驱动类的实例化
#                     2. 断言类型的关键字
#             '''
#             print("继续操作")
#             # 判断是否实例化
#             if value[1] == 'start_app':
#                 pass
#             # 非特殊关键字，通过反射机制实现
#             else:
#                 print("进入主程序")
#                 getattr(self.lp, value[1])(**args)
#                 # getattr(wk, 'open')(**args)
#                 # wk.open(**args)
#                 # 原有的open函数是 def open(self,url):
#                 '''
#                     如果是open，只需要传入value[4]
#                     如果是input，则需要传入value[2],value[3],value[4]
#                     如果是click，则需要传入value[2],value[3]
#                     **args不定长传参，不定义参数数量的多少，说白了就是一个字典格式
#                     但是字典是键值对形式存在
#                 '''
#
#     print("执行完毕！")
import time

import allure

from config.myLog import MyLog
logger = MyLog().log()

def run_case_step(page_object, test_case):

    # case_count = len(test_case)
    i = 1

    for step in test_case:

        # 定义一个字典参数，用于接收excel中的所有参数内容
        args1 = {}
        # 用例编号
        args1['case_id'] = step['用例编号']
        # 步骤编号
        args1['step_id'] = step['步骤编号']
        # 定位方法
        args1['name'] = step['定位方法']
        # 定位路径
        args1['value'] = step['元素路径']
        # 输入内容
        args1['txt'] = step['输入内容']
        # 预期结果
        args1['expect'] = step['预期结果']

        # 基于A列进行判断是否为测试用例
        if (str(step['步骤编号']).startswith('step_')):
            '''
                在读取关键字时，分为几类情况：
                    1. 关键字驱动类的实例化
                    2. 断言类型的关键字
            '''
            # print("继续操作")
            # 判断是否实例化
            if step['事件'] == 'start_app':
                pass
            # 非特殊关键字，通过反射机制实现
            else:
                # print("进入主程序")
                with allure.step('step{}: {} '.format(i, step['描述'])):
                    getattr(page_object, step['事件'])(**args1)
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
        i+=1
        # logger.info('执行完第{}个测试用例，用例名称为：{}'.format(i,step['用例编号']))

    # logger.info("模块名称: {}   所有测试用例执行完毕！,总计用例数：{}条".format(page_object.__name__, case_count))