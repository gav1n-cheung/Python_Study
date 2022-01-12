#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
控制台输出五行*, 每行*数量依次递增
"""
index  =  0
while index<10:
    index1 = 0
    while index1<index:
        print("*", end  = "")
        index1 += 1
    print()
    index += 1

