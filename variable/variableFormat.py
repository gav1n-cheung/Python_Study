#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
如果想要在输出文字信息的同时输出数据，则需要使用格式化操作符
% 被称为格式化操作符，专门用于处理字符串中的格式
  含有%的字符串，被称为格式化字符串
  %和不同的字符连用，不同类型的数据需要使用不用的格式化字符

%s  字符串
%d  有符号十进制整数，%06d表示输出的整数显示位数，不足的地方使用0补全
%f  浮点数，…%0.2f表示小数点后只显示两位
%%  输出%
"""
price = float(input("请输入单价"))
weight = float(input("请输入重量"))
print("苹果的单价为：%0.2f，重量为%0.2f，总价为%0.2f"%(price, weight, price*weight))

name  = input("输入姓名")
print("我的名字为%s"%name)
student_no =int(input("请输入学号"))
print("学号为%d"%student_no)
print("%0.2f%%"%(0.2*100))
