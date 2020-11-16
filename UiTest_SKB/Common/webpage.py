#!/usr/bin/env python 
# encoding: utf-8 
#@author: nick
#@software: PyCharm
#@file: webpage.py
#@time: 2020/9/3 11:31

import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.logging_handler import LoggerHandler as LG


logger = LG(name='web', level='INFO', file=r'C:\Users\Administrator\PycharmProjects\Web_api\PO\Outputs\logs\web.txt')
# 实现记录日志记录、截图
class Webpage():

    # 初始化driver
    def __init__(self,driver:WebDriver):
        self.driver = driver

