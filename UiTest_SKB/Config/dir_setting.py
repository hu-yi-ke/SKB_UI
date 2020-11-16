#!/usr/bin/env python 
# encoding: utf-8 
#@author: nick
#@software: PyCharm
#@file: dir_setting.py
#@time: 2020/9/3 14:31
import os


class Config():

    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试用例路径
    cases_path = os.path.join(root_path,"TestCases")

    #yaml文件路径
    yaml_path = os.path.join(root_path,"Config")

print(Config.yaml_path)
