#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

"""
需求：
1、从控制台输入要出的拳--石头(1)/剪刀(2)/布(3)
2、电脑随机出拳--先假定电脑只会出石头，完成整体代码功能
3、比较胜负

"""

player  =  int(input("你要出什么？ 石头(1)/剪刀(2)/布(3)"))

computer  = random.randint(1, 3)  #双闭区间产生随机数，下限必须小于上限
print("电脑出拳%d"%computer)
if player == 1:
    if computer == 1:
        print("平局")
    elif computer  == 2:
        print("你赢了")
    else:
        print("你输了")
elif player  == 2:
    if computer  == 1:
        print("你输了")
    elif computer  == 2:
        print("平局")
    else:
        print("你赢了")
else:
    if computer  == 1:
        print("你赢了")
    elif computer  == 2:
        print("你输了")
    else:
        print("平局")

if player == computer:
    print("平局")
elif player-computer == -1 or player-computer  == 2:
    print("你赢了")
else:
    print("你输了")
