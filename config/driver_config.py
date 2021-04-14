#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 21:31
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : driver_config.py
# @Software: PyCharm
import yaml
from appium import webdriver
from utils.get_yaml import get_yaml
from config.myLog import MyLog
logger = MyLog().log()

def appium_desired():
    # 加载yaml
    data = get_yaml('./config/app_info.yaml')

    info={}
    info['platformName']=data['platformName']
    info['platformVersion']=data['platformVersion']
    info['deviceName']=data['deviceName']
    info['noRest']=data['noRest']
    info['appPackage']=data['appPackage']
    info['appActivity']=data['appActivity']
    info['unicodeKeyboard']=data['unicodeKeyboard']
    info['resetKeyboard']=data['resetKeyboard']
    # 启动过程中有问题，加个日志
    logger.info('启动程序')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', info)
    return driver

if __name__ == '__main__':
    appium_desired()