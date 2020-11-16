#!/usr/bin/env python 
# encoding: utf-8 
#@author: nick
#@software: PyCharm
#@file: basepage.py
#@time: 2020/8/25 14:51
"""
1、等待可见
2、查找元素
3、点击--前提：等待和查找
4、输入--前提：等待和查找
5、获取属性--前提：等待和查找
6、获取文本-前提：等待和查找
"""

import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.logging_handler import LoggerHandler as LG


logger = LG(name='web', level='INFO', file=r'C:\Users\Administrator\PycharmProjects\Web_api\PO\Outputs\logs\web.txt')
# 实现记录日志记录、截图
class Basepage():

    # 初始化driver
    def __init__(self,driver:WebDriver or Remote):
        self.driver = driver

    # 等待元素可见-日志+截图
    def wait_ele_visible(self,loc,img_name,timeout=20,poll_fre=0.5):
        # 记录行为在干嘛
        logger.info("等待{}元素可见。".format(loc))
        try:
            WebDriverWait(self.driver, timeout,poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except:
                #失败截图-写入日志
                self.save_page_shot(img_name)
                logger.exception("等待元素可见失败")
                raise

    #等待元素可点击
    def wait_ele_clickable(self,loc,img_name,timeout=20,poll_fre=0.5):
        try:
            WebDriverWait(self.driver, timeout,poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except:
                #失败截图-写入日志
                self.save_page_shot(img_name)
                logger.exception("等待元素可见失败")
                raise

    # 查找元素
    def get_element(self, loc, img_name):
        # 记录行为在干嘛
        logger.info("在{}查找元素{}".format(img_name, loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.save_page_shot(img_name)
            logger.exception("查找元素失败")
            raise
        else:
            return ele

    # 查找元素们
    def get_elements(self,loc,img_name):
        # 记录行为在干嘛
        logger.info("在{}查找所有匹配的元素{}".format(img_name,loc))
        try:
            eles = self.driver.find_elements(*loc)
        except:
            self.save_page_shot(img_name)
            logger.exception("查找元素失败")
            raise
        else:
            return eles

    #点击元素
    def click_element(self,loc,img_name,timeout=20,poll_fre=0.5):
        '''
        :param loc:
        :param img_name: 页面名称_页面行为
        :param timeout:
        :param poll_fre:
        :return:
        '''
        logger.info("在{}点击{}元素".format(img_name, loc))
        #先可见并查找成功
        self.wait_ele_visible(loc,img_name,timeout,poll_fre) #必要前提
        ele = self.get_element(loc,img_name) #必要前提
        try:
            ele.click()
        except:
            self.save_page_shot(img_name)
            logger.exception("点击元素失败")
            raise

    #输入文本
    def input_text(self,loc,value,img_name,timeout=20,poll_fre=0.5):
        logger.info("在{}往元素{}输入文本值：{}".format(img_name, loc,value))
        # 先可见并查找成功
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        eles = self.get_element(loc, img_name)
        try:
            eles.send_keys(value)
        except:
            self.save_page_shot(img_name)
            logger.exception("输入文本失败")
            raise

    # 获取属性
    def get_ele_attribute(self,loc,attr_name,img_name,timeout=20,poll_fre=0.5):
        logger.info("在{}获取元素{}的{}属性".format(img_name, loc, attr_name))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        try:
            value = ele.get_attribute(attr_name)
        except:
            self.save_page_shot(img_name)
            logger.exception("获取属性值失败")
        else:
            logger.info("获取元素属性成功")
            return value

    #获取文本
    def get_ele_text(self,loc,img_name,timeout=20,poll_fre=0.5):
        logger.info("在{}获取元素{}的文本属性".format(img_name, loc))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        try:
            text = ele.text
        except:
            self.save_page_shot(img_name)
            logger.exception("获取元素文本属性失败")
        else:
            logger.info("获取元素文本成功")
            return text


    #截图
    def save_page_shot(self,img_name):
        """
        :param img_name:页面名称_页面行为
        :param filepath:
        :return:
        """
        #将图片存储到Outputs的screenshots中，图片命名
        #命名规则：页面名称_页面行为_时间.png
        #文件完整名称
        now_time = time.strftime("%Y-%m-%d %H_%M_%S")
        file_path = r"C:\Users\Administrator\PycharmProjects\Web_api\PO\Common\Outputs\screenshots"
        file_name = "{}_{}.png".format(img_name,now_time)

        self.driver.save_screenshot(file_path +'/'+ file_name)
        logger.info("页面图片保存在:{}".format(file_path+'/'+file_name))

    # 获取设备大小
    def get_divice_size(self):
        size = self.driver.get_window_size()
        return size
    # 滑屏操作--上下左右
    def swipe_by_direction(self,direction):
        """
        :param direction: up,down,left,right 往哪个方向滑动
        :return: None
        """
        size = self.get_divice_size()
        if direction == "up":
            self.driver.swipe(size["width"]*0.5,size["height"]*0.9,size["width"]*0.5,size["height"]*0.3,200)

    # 列表滑动
    # toast获取
    # 混合应用
    def _deal_element(self, loc, img_name, timeout, poll_fre, wait_type):
        pass


"""
    #iframe窗口切换
    def switch_to_iframe(self,loc,img_name):
        #loc可以有3种形式
        try:
            WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except:
            self.save_page_shot(img_name)
            logger.exception("获取窗口失败")
            raise
        else:
            logger.info("获取窗口成功")
"""

if __name__ == '__main__':
    driver = webdriver.Chrome()
    bs = Basepage(driver).save_page_shot('11')
    driver.quit()


# alert切换
#js执行
#滚动条操作
#上传文件--windows