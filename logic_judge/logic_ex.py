#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
练习1:定义一个整数变量age, 编写代码判断是否正确
"""
age = int(input("请输入年龄"))
if age > 120 or age < 0:
    print("年龄输入有误")
else:
    print("年龄为%d"%age)
