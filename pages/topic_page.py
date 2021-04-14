from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.myLog import MyLog
logger = MyLog().log()

class TopicPage(BasePage):

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