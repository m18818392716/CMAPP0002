#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 21:29
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : get_yaml.py
# @Software: PyCharm

import yaml

def get_yaml(path):
    f = open(path, encoding="utf8")
    result = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return  result