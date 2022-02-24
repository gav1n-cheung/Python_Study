"""
字典
dictionary是除列表之外python之中最灵活的数据类型
字典同样可以用来存储多个数据
    通常用于存储描述一个物体的相关信息
和列表的区别
    列表是有序的对象集合
    字典是无序的对象集合
字典用{}定义
字典使用键值对存储数据，键值对之间使用,分隔
    键key是索引
    值value是数据
    键和值之间使用:分隔
    键必须是唯一的
    值可以取任何数据类型，但键只能使用字符串、数字或元组
"""
#   字典是一个无序的数据集合，使用print函数进行输出字典时，
#   通常输出的顺序和定义的顺序是不一致的
from sqlalchemy import false

dictionary_info = {"name": "cheung", "age": 18, "gender": True, "weight": 75.5}
print(dictionary_info)
"""
字典的常用操作
"""
#   1、取值
print(dictionary_info["name"])
# print(dictionary_info["name123"])如果取值时的指定的key不存在，程序会报错

#   2、增加/修改
#   如果修改的key不存在，则为新增键值对，否则为修改
dictionary_info["age"] = 20
print(dictionary_info)

#   3、删除
#   如果pop方法删除字典中不存在的key，则也会报错
dictionary_info.pop("age")
print(dictionary_info)

#   4、统计键值对数量
print(len(dictionary_info))

#   5、合并字典
#   如果合并的字典已经存在了相同的键，则会更新键值
dictionary_info["age"] = 18
print(dictionary_info)
dictionary_info2 = {"height": 1.75, "age": 15}
dictionary_info.update(dictionary_info2)
print(dictionary_info)

#   6、清空字典
dictionary_info.clear()
print(dictionary_info)

#   7、迭代遍历字典
dictionary_info = {"name": "cheung", "qq": "1231", "phoneNumber": 1231}
#   变量item是每一次循环中，获取到的键值对的key
for item in dictionary_info:
    print("%s : %s" % (item, dictionary_info[item]))

#   8、字典和列表配合使用
#   尽管可以使用for in 遍历字典
#   但是在开发中，更多的应用场景是：
#       使用多个键值对，存储描述一个物体的相关信息--描述更复杂的数据信息
#       将多个字典放在一个列表中，再进行遍历，在循环体内部针对每一个字典进行相同的处理
info = [{
    "name": "cheung",
    "age": 18,
    "gender": True
}, {
    "name": "gavin",
    "age": 20,
    "gender": False
}]
for item in info:
    print(item)