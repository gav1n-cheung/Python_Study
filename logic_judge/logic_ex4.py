#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
需求：
定义布尔量has_ticket，表示是否有车票
定义整型变量knife_length，表示刀的长度，单位为米
首先检查是否有车票，如果有，才允许进行安检
安检时，需要判断刀的长度，判断是否超过20厘米：
    如果超过20cm，则不允许上车
    如果不超过20cm，安检通过
如果没有车票，不允许上车
"""
has_ticket  = False
flag  =  input("是否有车票？是/否")
if flag  == "是":
    has_ticket = True
if has_ticket:
    knife_length  =  float(input("请输入刀的长度"))
    if knife_length >= 0.2:
        print("刀长超过规定，禁止上车")
    else:
        print("可以上车")
else:
    print("没车票上啥车")
