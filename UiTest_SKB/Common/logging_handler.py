#!/usr/bin/env python 
# encoding: utf-8 
#@author: nick
#@software: PyCharm
#@file: logging_handler_2.py
#@time: 2020/8/5 18:24
import logging

class LoggerHandler(logging.Logger):

    def __init__(self,
                 name = 'root',
                 level ='DEBUG',
                 file =None,
                 format = '%(filename)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s-%(asctime)s'
                 ):
        super().__init__(name)

        # 设置级别
        self.setLevel(level)

        fmt = logging.Formatter(format)
        # 初始化处理器
        if file:
            file_handler = logging.FileHandler(file)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)

        steam_handler = logging.StreamHandler()

        # 设置handler级别
        steam_handler.setLevel(level)
        steam_handler.setFormatter(fmt)
        self.addHandler(steam_handler)



if __name__ == '__main__':
    # yaml_data = read_yaml(config.yaml_config_path)
    # print(yaml_data)
    # logger = LoggerHandler(name=yaml_data['logger']['name'], level=yaml_data['logger']['level'],
    #                        file=yaml_data['logger']['file'])
    logger =  LoggerHandler('')
    logger.error('hellow')

