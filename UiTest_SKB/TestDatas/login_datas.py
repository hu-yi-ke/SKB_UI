#!/usr/bin/env python 
# encoding: utf-8 
#@author: nick
#@software: PyCharm
#@file: login_datas.py
#@time: 2020/8/22 22:43

#异常场景--用户名为空、密码为空、用户名格式不正确
datas = [{"user": "", "passwd": "python", "check": "请输入手机号","case_name":"没有输入手机号"},
         {"user": "18684720553", "passwd": "", "check": "请输入密码","case_name":"没有输入密码"},
         {"user": "1868472055", "passwd": "python", "check": "请输入正确的手机号","case_name":"没有输入正确的手机号"},
         ]

# 正常场景
success = ("18684720553","python")