###
# 列表的定义
# List(列表)是python种使用最频繁的数据类型，在其他语言中通常叫做数组
# 专门用于存储一串信息
# 列表用[]定义，数据之间使用,分割
# 列表的索引从0开始（索引就是数据在列表中的位置编号，索引又可以被称为下标）
#   注意：从列表中取值时，如果超出索引范围，程序会报错
###
from sqlalchemy import true


name_list = ["cheung", "gavin", "wangwu"]
print(name_list)
#   1、取值和取索引
print(name_list[0])  # 取值

# 已知数据的内容，想确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错
print(name_list.index("gavin"))  # 取索引

#   2、修改数据
name_list[0] = "maybe"
print(name_list)

#   3、增加数据
#在末尾追加数据
name_list.append("burning")
print(name_list)
#在指定位置插入数据
name_list.insert(3, "zhou")
print(name_list)
# 追加列表 
temp_list=["sun" , "zhao"]
name_list.extend(temp_list)
print(name_list)

#   4、删除数据
#   删除列表最后一个数据,pop方法默认可以把列表中最后一个元素删除，也可以指定索引删除
# temp_list.pop()
temp_list.pop(0)
print(temp_list)
#   清除整个列表
temp_list.clear()
print(temp_list)
#   输出指定内容的第一个数据
temp_list.append("burnning")
temp_list.append("burnning")
print(temp_list)
temp_list.remove("burnning")
print(temp_list)
#   使用del关键字来删除列表元素,del关键字本质上是用来将一个变量从内存中删除的
#   注意：如果使用del关键字将变量从内存中删除，后续的代码就不能再使用这个变量了
#   再日常开发种，要从列表中删除数据，建议使用列表提供的方法
del temp_list[0]
print(temp_list)
name ="小明"
del name
#   5、列表统计
print(len(name_list))   # 统计列表长度
print(name_list.count("cheung"))    #统计指定元素的出现次数

#   6、列表排序
#   升序
num_list=[0,3,2,5]
num_list.sort()
print(num_list)
#   降序
num_list.sort(reverse=True)
print(num_list)
#   反转
name_list.reverse()
#   7、循环遍历
#   遍历就是从头到尾依次从列表中获取数据
#       在循环体内部针对每一个元素，执行相同的操作
#   在python种为了提高列表的遍历效率，专门提供的迭代iteration遍历
#   使用for就能够实现迭代遍历
for name in name_list:
    print(name)

# 常用方法：len(列表)          获取列表的长度n+1
#          列表.count(数据)    获取数据在列表中出现的次数
#          列表.sort()         升序排列列表
#          列表.sort(reverse=True) 降序排列
#          列表.reverse()      反转/逆序排列列表
#          列表[索引]          从列表中取值
#          列表.index(数据)    获得数据第一次出现的索引
#          del 列表[索引]      删除指定索引的数据
#          列表.remove(数据)   删除第一个出现的指定数据
#          列表.pop            删除末尾数据
#          列表.pop(索引)      删除指定索引的数据
#          列表.insert(索引,数据)   在指定位置插入数据
#          列表.append(数据)   在末尾追加数据
#          列表.extend(列表2)  将列表2的数据追加到列表1
# 在开发中列表最常用的场景是：
# 1、列表存储相同类型的数据
# 2、通过跌打遍历，在循环内部，针对列表中的每一项元素，执行相同的操作