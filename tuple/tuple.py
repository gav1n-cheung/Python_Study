"""
元组
tuple与列表类型，不同之处在于元组的元素不能修改
    元组表示多个元素组成的序列
    元组在python开发中，有特殊的应用场景
用于存储一串信息，数据之间用“，”分隔
元组用()定义
元组的索引从0开始
"""

from msilib import type_short
from joblib import PrintTime

info_tuple = ("cheung", 18, 1.75)
print(type(info_tuple))
print(info_tuple[0])  # 获取数据仍然使用[]

empty_tuple = ()  # 创建空元组，很少使用
single_tuple = (5)  #   创建只有一个元素的元组，则编译器不会认为他是元组类型
print(type(single_tuple))
single_tuple = (5, )  # 这样才能创建一个具有一个元素的元组
print(type(single_tuple))

#   元组的常用操作
print(empty_tuple.count("cheung"))  #   计算cheung在元组内出现的次数
print(info_tuple.index(18))  #  得到18在元组内的索引，如果没有该元素，程序报错
print(len(info_tuple))  #   获取元组长度

#   迭代遍历元组
for item in info_tuple:
    print(item)

#   元组的应用场景
#   函数的参数和返回值，一个函数可以接受任意多个参数，或者 一次返回多个数据
#   格式化字符串，格式化字符串后面的()本质上就是一个元组
#   让列表不可以被修改，以保护数据安全
info_tuple = ("cheung", 18, 175)
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)
print(type(info_str))
#   元组和列表之间的转换
#   使用list函数将元组转换为列表,list(元组)
#   使用tuple函数将列表转换为列表，tuple(列表)
info_list=list(info_tuple)
print(type(info_list))
for item in info_list:
    print(item)
tuple(info_tuple)
print(type(info_tuple))