#!/usr/bin/env python
# -*- coding: utf-8 -*-

index = 0
while index<5:
    print("hello world")
    index  = index + 1
print("一共循环了%d次"%index)

"""
赋值运算符：
在python中，使用 = 可以给变量赋值
在算数运算中，为了简化代码的编写，python还提供了一系列的与算法运算符对赢得赋值运算符
注意：赋值运算符中间不能使用空格

     =      简单的赋值运算符        c = a+b将a+b的值赋值给c
     +=     加法赋值运算符          c +=a 等效于c = c+a
     -=     减法赋值运算符
     *=     乘法赋值运算符
     /=     除法赋值运算符
     //=    取整除赋值运算符
     %=     取模赋值运算符
     **=   幂赋值运算符
"""
num1 = 1
num2 = 3
num3 = 2
num3 += num1
print(num3)
num3 -= num1
print(num3)
num3 *= num2
print(num3)
num3 /= num2
print(num3)
num3 //= num2
print(num3)
num3 %= num1
print(num3)
num3 **= num1
print(num3)

