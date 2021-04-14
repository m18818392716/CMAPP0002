#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 21:31
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : base_page.py
# @Software: PyCharm

# 基类，封装的公共方法都在这里
import os
import time
from datetime import datetime
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from config.myLog import MyLog
import allure

command0 ='adb shell ime list -s'
command1 ='adb shell settings get secure default_input_method'
command3 ='adb shell ime set io.appium.settings/.UnicodeIME'
sougou_xiaomi = 'adb shell ime set com.sohu.inputmethod.sogou/.SogouIME'

class BasePage:

    '''
        https://blog.csdn.net/cc8945203/article/details/103765505    allure  错误日志截图

    '''
    def __init__(self, driver):
        self.logger = MyLog().log()
        self.driver = driver
        self.width =  self.driver.get_window_size()['width']
        self.height =  self.driver.get_window_size()['height']


    def screenshot_element(self, **kwargs):
        # 元素区域截图
        element = self.driver.find_element(kwargs['name'], kwargs['value'])
        pngbyte = element.screenshot_as_png
        allure.attach(pngbyte, allure.attachment_type.PNG)

    def _capture_screenshot(self, img_doc):
        # fileName = config.tmpPath + '/' + str(uuid.uuid1()) + '.png'
        file_name = "../images/{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), img_doc)
        self.driver.get_screenshot_as_file(file_name)
        return file_name

    def save_screenshot(self, img_doc):
        '''
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        '''
        file_name = self._capture_screenshot(img_doc)
        self.driver.save_screenshot(file_name)
        if os.path.exists(file_name):
            with open(file_name, mode='rb') as f:
                file = f.read()
            allure.attach(file, img_doc, allure.attachment_type.PNG)
            self.logger.info("页面截图文件保存在：{}".format(file_name))
        else:
            pass


    # 切换键盘输入法-搜狗输入法
    def switch_keyboard_sougo(self, **kwargs):
        os.system(sougou_xiaomi)

    # 切换键盘输入法-Appium默认输入法
    def switch_keyboard_default(self, **kwargs):
        os.system(command3)

    def keyborad_button(self, **kwargs):
        self.driver.press_keycode(kwargs['value'])
    # 元素定位
    def locator(self, is_need_displayed = True, **kwargs):
        try:
            if is_need_displayed:
                self.logger.info("通过" + kwargs['name'] + "定位， 元素是" + kwargs['value'])
                WebDriverWait(self.driver, 5, 0.5).until(
                    lambda el: self.driver.find_element(kwargs['name'], kwargs['value']), message='元素查找失败')
        except Exception as e:
            self.logger.info("定位元素错误")
            raise e
            # raise Exception("页面中未能找到 [%s]" % self.driver.find_element(kwargs['name'], kwargs['value']))
        return self.driver.find_element(kwargs['name'], kwargs['value'])

    # 输入
    # self.driver.find_element_by_id('').sendkey('')
    def input(self, **kwargs):
        with allure.step('输入内容：{}'.format(kwargs['txt'])):
            self.locator(**kwargs).send_keys(kwargs['txt'])

    #点击
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # 文本断言校验  判断实际值  是否与  期望值一致
    def assert_text(self, **kwargs):
        assert self.locator(**kwargs).text == kwargs['expect_text'], '断言失败'

    # 强制等待
    def wait(self, **kwargs):
        sleep(kwargs['txt'])

    # 显示等待
    def visit_wait(self, **kwargs):
        return WebDriverWait(self.driver, kwargs['txt'], 0.5).until(
            lambda el: self.locator(**kwargs), message='查找元素失败')

    # 退出
    def quit(self, **kwargs):
        self.driver.quit()

    def fail_picture(self):
        f = self.get_screenshot_as_file()
        self.logger.info('失败用例截图:{filename}'.format(filename=f))
        allure.attach.file(f, '失败用例截图:{filename}'.format(filename=f), allure.attachment_type.PNG)

    def get_screenshot_as_file(self):
        '''在本地截图函数'''
        try:
            pic_pth = '../images/'
            filename = pic_pth + str(time.time()).split('.')[0] + '.png'
            filename = filename.replace('\\', '/')
            self.driver.get_screenshot_as_file(filename)
            self.logger.info('get_screenshot_as_file {filename}'.format(filename=filename))
            return filename
        except Exception as e:
            self.logger.info(e)
            return None

    def swip_down(self, count=1, method=None, speed=1000):
        """ 向下滑动,常用于下拉刷新
        :param count: 滑动次数
        :param method: 传入的方法 method(action) ,如果返回为True,则终止刷新
        :param speed: 滑动速度 ms
        """
        if count == 1:
            self.driver.swipe(self.width / 2, self.height * 2 / 5, self.width / 2, self.height * 4 / 5, speed)
            sleep(1)
        else:
            for x in range(count):
                self.driver.swipe(self.width / 2, self.height * 2 / 5, self.width / 2, self.height * 4 / 5, speed)
                sleep(1)
                try:
                    if method(self):
                        break
                except:
                    pass
        self.logger.info("[滑动]向下刷新 ")

    def swip_up(self, count=1, method=None, speed=1000):
        """ 向上刷新
        :param count: 滑动次数
        :param method: 传入的方法 method(action) ,如果返回为True,则终止刷新
        :param speed: 滑动速度 ms
        :return:
        """
        if count == 1:
            sleep(1)
            self.driver.swipe(self.width / 2, self.height * 3 / 4, self.width / 2, self.height / 4, speed)
            sleep(2)
        else:
            for x in range(count):
                self.driver.swipe(self.width / 2, self.height * 3 / 4, self.width / 2, self.height / 4, speed)
                sleep(2)
                try:
                    if method(self):
                        break
                except:
                    pass
        self.logger.info("[滑动]向上刷新 ")

    def swip_left(self, height=0.5, count=1, speed=1000):
        """ 向左滑动
        :param height: 高度满屏幕为1
        :param count: 滑动次数
        :param speed: 滑动速度 ms
        :return:
        """
        for x in range(count):
            sleep(1)
            self.driver.swipe(self.width * 7 / 8, self.height * height, self.width / 8, self.height * height, speed)
            sleep(2)
            self.logger.info("[滑动]向左滑动")

    def swip_right(self, height=0.5, count=1, speed=1000):
        """向右滑动
        :param height: 高度满屏幕为1
        :param count: 滑动次数
        :param speed: 滑动速度 ms
        :return:
        """
        for x in range(count):
            sleep(1)
            self.driver.swipe(self.width / 8, self.height * height, self.width * 7 / 8, self.height * height, speed)
            sleep(2)
            self.logger.info("[滑动]向右滑动 ")






    def split_locator(self, locator):
        """
        分解定位表达式，如'css,.username',拆分后返回'css selector'和定位表达式'.username'(class为username的元素)
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        :return: locator_dict[by], value:返回定位方式和定位表达式
        """
        by = locator.split(',')[0]
        value = locator.split(',')[1]
        locator_dict = {
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link': 'link text',
            'plink': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector',
        }
        if by not in locator_dict.keys():
            raise NameError("wrong locator!'id','name','class','tag','link','plink','xpath','css',exp:'id,username'")
        return locator_dict[by], value

    def wait_element(self, locator, sec=30):
        """
        等待元素出现
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param sec:等待秒数
        """
        by, value = self.split_locator(locator)
        try:
            WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value),
                                                     message='element not found!!!')
            self.logger.info(u'等待元素：%s' % locator)
            return True
        except TimeoutException as e:
            return False
        except Exception as e:
            raise e


    def get_element(self, locator, sec=60):
        """
        获取一个元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param sec:等待秒数
        :return: 元素可找到返回element对象，否则返回False
        """
        if self.wait_element(locator, sec):
            by, value = self.split_locator(locator)
            try:
                element = self.driver.find_element(by=by, value=value)
                self.logger.info(u'获取元素：%s' % locator)
                return element
            except Exception as e:
                raise e
        else:
            return False


    def get_elements(self, locator):
        """
        获取一组元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: elements
        """
        by, value = self.split_locator(locator)
        try:
            elements = WebDriverWait(self.driver, 60, 1).until(lambda x: x.find_elements(by=by, value=value))
            self.logger.info(u'获取元素列表：%s' % locator)
            return elements
        except Exception as e:
            raise e

    #  通过下标获取元素值
    def get_element_by_index(self, locator, index):
        """
        获取一组元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: elements
        """
        by, value = self.split_locator(locator)
        try:
            elements = WebDriverWait(self.driver, 60, 1).until(lambda x: x.find_elements(by=by, value=value))
            self.logger.info(u'获取元素列表：%s' % locator)
            return elements[index]
        except Exception as e:
            raise e

    #  通过text获取元素值
    def get_element_by_text(self, locator, text):
        """
        获取一组元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: elements
        """
        by, value = self.split_locator(locator)
        try:
            elements = WebDriverWait(self.driver, 60, 1).until(lambda x: x.find_elements(by=by, value=value))
            self.logger.info(u'获取元素列表：%s' % locator)
            for element in elements:
                if element.text == text:
                    return element
        except Exception as e:
            raise e