#!/usr/bin/env python
# -*- coding: utf-8 -*-

price  =  input("请输入苹果的单价")
weight  =  input("请输入苹果的重量")
print("苹果的单价为:"+price+" 苹果重量为:"+weight)
price_float = float(price)
weight_float = float(weight)
money = price_float*weight_float
print(money)


