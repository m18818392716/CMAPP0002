#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 23:20
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : main.py
# @Software: PyCharm
import os
from datetime import time

import pytest
import subprocess
from config.myLog import MyLog

PATH = os.path.split(os.path.realpath(__file__))[0]
xml_report_path = PATH + "/allure-result/xml"
html_report_path = PATH + "/allure-report/html"
tm = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))


def invoke(md):
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o

if __name__ == '__main__':
    xml_report_path = './allure-result/xml'
    html_report_path = './allure-report/html'
    logger = MyLog().log()
    # args = ['-s', '-q', "./cases/test_search_case.py", "./cases/test_login_case.py"]
    args = ["./cases/test_search_case.py", "./cases/test_login_case.py"]
    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    invoke(cmd)
    logger.info("-----------------------------END: %s------------------------------------" % tm)

    # pytest.main(["-s", "./cases/test_search_case.py", "./cases/test_login_case.py"])