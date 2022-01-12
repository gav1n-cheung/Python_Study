#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
\t  ==  制表符
\n  ==  在控制台输出一个换行符
\r  ==  输出一个回车
\"  ==  输出引号
"""

row = 1
while row <= 9:
    col  = 1
    while col <= row:
        print("%d*%d  = %d"%(row, col, row*col), end = "\t")
        col += 1
    print()
    row += 1
    

