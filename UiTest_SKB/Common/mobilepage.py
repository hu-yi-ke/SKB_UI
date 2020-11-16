#!/usr/bin/env python 
# encoding: utf-8 
#@author: nick
#@software: PyCharm
#@file: mobilepage.py
#@time: 2020/9/3 11:28
import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.basepage import Basepage




from Common.logging_handler import LoggerHandler as LG
logger = LG(name='web',
            level='INFO',
            file=r'C:\Users\Administrator\PycharmProjects\Web_api\PO\Outputs\logs\web.txt')

class MobilePage(Basepage):

    # # 初始化driver
    #  def __init__(self,driver:Remote):
    #      super().__init__()

    #等待toast可见
    def wait_ele_visible_toast(self, loc, img_name, timeout=20, poll_fre=0.5):
        # 记录行为在干嘛
        logger.info("等待{}元素可见。".format(loc))
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=poll_fre).until(
                EC.presence_of_element_located(loc))
        except:
            # 失败截图-写入日志
            self.save_page_shot(img_name)
            logger.exception("等待元素可见失败")
            raise

    # 获取设备大小
    def get_divice_size(self):
        size = self.driver.get_window_size()
        return size

    # 获取文本toast
    def get_text(self, loc, img_name, timeout=20, poll_fre=0.5):
        logger.info("在{}获取元素{}的文本属性".format(img_name, loc))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.driver.find_element(*loc)
        ele = ele.text
        try:
            text = ele.text
        except:
            self.save_page_shot(img_name)
            logger.exception("获取元素文本属性失败")
        else:
            logger.info("获取元素文本成功")
            return text

    # 滑屏操作--上下左右
    def swipe_by_direction(self, direct,duration=200):
        """
        :param direction: up,down,left,right 往哪个方向滑动
        :return: None
        """
        size = self.get_divice_size()
        if direct.lower() == "up":
            self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9,
                              size["width"] * 0.5, size["height"] * 0.3,duration)
        elif direct.lower() == "down":
            self.driver.swipe(size["width"] * 0.5, size["height"] * 0.1,
                              size["width"] * 0.5, size["height"] * 0.9, duration)
        elif direct.lower() == "left":
            self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5,
                              size["width"] * 0.1, size["height"] * 0.5, duration)
        elif direct.lower() == "right":
            self.driver.swipe(size["width"] * 0.1, size["height"] * 0.5,
                              size["width"] * 0.9, size["height"] * 0.5, duration)

    # 列表滑动
    # toast获取
    def get_tost_msg(self,text,img_desc):
        #xpath表达式
        loc = (MobileBy.XPATH,'//*[contains(@text(),"{}")]'.format(text))
        logger.info("获取toast提示信息，toast元素：{}".format(loc))
        # 等待元素存在并获取文本信息
        return self.get_text(text,img_desc,10,0.01)

        # 混合应用
