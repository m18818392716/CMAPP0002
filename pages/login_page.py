#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 21:30
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : login_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.driver_config import appium_desired
from config.myLog import MyLog
logger = MyLog().log()

class LoginPage(BasePage):

    rlMine = (By.ID, 'com.tnaot.newspro:id/rlMine')
    ivMineSetting = (By.ID, 'com.tnaot.newspro:id/ivMineSetting')
    rlExit = (By.ID, 'com.tnaot.newspro:id/rlExit')
    button1 = (By.ID, 'android:id/button1')# 确认 退出
    button2 = (By.ID, 'android:id/button2')# 取消 退出
    tv_login_btn = (By.ID, 'com.tnaot.newspro:id/tv_login_btn')# 登录/注册按钮

    tv_main_password_login = (By.ID, 'com.tnaot.newspro:id/tv_main_password_login')# 密码登录
    tv_main_phone_login = (By.ID, 'com.tnaot.newspro:id/tv_main_phone_login')# 验证码登录
    tv_main_facebook_login = (By.ID, 'com.tnaot.newspro:id/tv_main_facebook_login')# 第三方Facebook登录

    ll_password_area_code = (By.ID, 'com.tnaot.newspro:id/ll_password_area_code')# 区号选择
    china_area = (By.XPATH, "//*[@text='中国']")# 选择中国
    user = (By.ID, 'com.tnaot.newspro:id/et_password_phone_num')
    pwd = (By.ID, 'com.tnaot.newspro:id/et_phone_password')
    button = (By.ID, 'com.tnaot.newspro:id/ibtn_password_login')

    rlHome = (By.ID, 'com.tnaot.newspro:id/rlHome')# 点击首页Tab
    iv_top_search = (By.ID, 'com.tnaot.newspro:id/iv_top_search')# 点击搜索按钮
    et_search_keywords = (By.ID, 'com.tnaot.newspro:id/et_search_keywords')# 输入搜索内容

    # def login(self,username,password):
    #     # 点击取消
    #     self.check_cancel()
    #     # 点击跳过
    #     self.check_skip()
    #     # 输入用户名，输入密码,点击登录
    #     log.info('请输入用户名%s'%username)
    #     self.input_(self.user,username)
    #     log.info('请输入密码%s' %password)
    #     self.input_(self.pwd, password)
    #     self.click(self.button)


    # def login(self,username,password):
    #     # 点击我的
    #     self.click(self.rlMine)
    #     # 点击登录/注册
    #     self.click(self.tv_login_btn)
    #     # 点击密码登录
    #     self.click(self.tv_main_password_login)
    #     # 点击区号
    #     self.click(self.ll_password_area_code)
    #     # 选择【中国】
    #     self.click(self.china_area)
    #     # 输入用户名，输入密码,点击登录
    #     logger.info('请输入用户名%s'%username)
    #     self.input(self.user,username)
    #     logger.info('请输入密码%s' %password)
    #     self.input(self.pwd, password)
    #     self.click(self.button)

# 要测试各种情况，测正常的情况，异常的情况。先进行unittest用例管理框架
# 结合ddt，想要把测试数据放在yaml中，放在代码就放在代码中

# if __name__ == '__main__':
#     driver = appium_desired()
#     lp = LoginPage(driver)
#     lp.login('18818392716','123456')