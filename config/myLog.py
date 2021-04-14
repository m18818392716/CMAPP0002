#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 21:37
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : myLog.py
# @Software: PyCharm

import logging, os, time
# from common.function import program_get

class MyLog():

    def __init__(self):
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG) # 全局日志等级

        # 避免日志重复输出
        if not self.logger.handlers:
            # 日志路径位置
            # self.log_path = os.path.join(program_get(), "Logs", "")
            self.log_path = './Logs/'

            self.log_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
            self.log_name = self.log_path + self.log_time + "log.log"
            print(self.log_name)
            # 创建handle
            fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            # 定义handle输出格式
            formatter = logging.Formatter(fmt="%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s",
                                         datefmt="%Y/%M/%d/%X")
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            fh.close()

    def log(self):
        return self.logger

if __name__ == '__main__':
    logger = MyLog().logger
    logger.info("日志工具类测试成功")