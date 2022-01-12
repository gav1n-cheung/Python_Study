#!/usr/bin/env python
# -*- coding: utf-8 -*-
import keyword

"""
标识符可以由字母、下划线和数字组成
不能以数组开头
不能与关键字崇明
"""
print(keyword.kwlist)

"""
python变量的命名规则：
    命名规则可以被视为一种惯例，并无绝对与强制
    目的是为了增加代码的识别和可读性

python中的标识符是区分大小写的，比如Andy! = andy
1、在定义变量时，为了保证代码格式， = 左右应该各保留一个空格
2、在python中，如果变量名需要由二个或多个单词组成时，可以按照以下方式命名：
    a.每个单词都使用小写字母
    b.单词与单词之间使用_下划线连接
    c.例如：first_name, last_name

"""
