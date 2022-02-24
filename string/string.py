"""
字符串
1、字符串的定义
    字符串就是一串字符，是编程语言中表示文本的数据类型
    在python种可以使用一堆双引号“”或者一对单引号''定义一个字符串
        虽然可以使用\"或者\'做字符串的转义，但是在实际开发中：
            如果字符串内部需要使用",可以使用"定义字符串
            如果字符串内部需要使用',可以使用"定义字符串
    也可以使用索引获取一个字符串中指定位置的字符，索引计数从0开始
    也可以使用for循环遍历字符串中每一个字符
"""



str1 = "hello world"
str2 = 'my name is "cheung"'
print(str2)

print(str2[1])

for item in str2:
    print(item)

"""
2、字符串的常用操作
"""
#   (1)统计字符串长度
print(len(str1))
#   (2)统计某一个小字符串出现的次数
print(str1.count("l"))
print(str1.count("a"))  #   如果找不到子字符串，程序不会报错，计数为0
#   (3)某一个子字符串出现的位置
print(str1.index("llo"))
# print(str1.index("abc"))  如果找不到子字符串，程序会报错

"""
字符串中的判断操作
string.isspace()        如果string中只包含空格，则返回true
string.isalnum()        如果string至少有一个字符并且所有字符都是字符或数字则返回True
string.isalpha()        如果string至少有一个字符并且所有字符都是字母则返回true

    这三个方法都不能判断小数
    isdecimal不能识别(1)这种数字和unicode 字符串
    isnumeric能够判断中文数字
    开发中使用isdecimal较多
string.isdecimal()      如果string只包含数字则返回True，全角数字
string.isdigit()        如果string只包含数字则返回True，全角数字，(1),\u00b2
string.isnumeric()      如果string只包含数字则返回True，全角数字，汉字数字
string.istitle()        如果string是标题化的(每个单词的首字母大写)，则返回true
string.islower()        如果string中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回true
string.isupper()        如果string中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回true
"""

strSpace = "   \t\n\r"
print(strSpace.isspace())   #   python中\t,\n,\r也属于空白字符

strNum1 = "kalskd123"
print(strNum1.isalnum())

strNum2 = "kaskd "
print(strNum2.isalnum())

strTitle = "Time Is Losing"
print(strTitle.istitle())

strLower = "timeislosing"
print(strLower.islower())

strUpper = "TIMEISLOSING"
print(strUpper.isupper())

"""
string.startwith(str)       检查字符串是否是以str开头，否则返回true
string.endwith(str)         检查字符串是否是以str结束，否则返回true
string.find(str,start=0,end=len(string))    检测str是否包含在string中，如果start和end指定的范围，则检查是否包含在指定范围内，如果是返回开始的索引，否则返回-1;而具有相似功能的index查找失败会使程序报错
string.replace(old_str,new_str,num=string.count(old))   把string中的old_str替换成new_str,如果num指定，则替换不超过num次
"""

strFind = "time is losing"
print(strFind.startswith("me"))
print(strFind.endswith("ing"))
print(strFind.find("is", 0, len(strFind)))
print(strFind.replace("is", "are")) #   使用该方法替换，不会改变原来的字符串

"""
文本对齐
"""

poem = ["\t\n登黄雀楼",
        "王之涣","\t白日依山尽","\n黄河入海流","欲穷千里目","更上一层楼"]
for item in poem:
    print("|%s|"%item.center(10, "　")) #   居中对齐

for item in poem:
    print("|%s|"%item.ljust(10,"　"))   #   左对齐

"""
去除空白字符
string.lstrip() 截掉string左边(开始)的空白字符
string.rstrip() 截掉string右边(末尾)的空白字符
string.strip()  截掉string左右两边的空白字符
"""
for item in poem:
    print("|%s|"%item.strip().center(10,"　"))

"""
拆分和连接
string.split(str="",num)    以str为分隔符拆分string,如果num有指定值，则仅分隔num+1个字符串，str默认包含'\t','\n','r'和空格
string.join(seq)            以string作为分隔符，将seq中所有的元素(的字符串表示)，合并为一个新的字符串
"""
strSplit="kajdka jkajd  jksald"
strList=strSplit.split()
print(strList)
for item in strList:
    print(item)
strSplit2="who's your daddy?"
print(strSplit2.split("s"))
print(" ".join(strList))
"""
字符串的切片
    切片方法适用于字符串、列表和元组
        切片使用索引值来限定范围，从一个大的字符串中切出小的字符串
        列表和元组都是有序的集合，都能够通过索引值获取到对应的数据
        字典是一个无序的集合，是使用键值对保存数据
        可以使用倒序进行索引，即在最后一个字符是-1，向左逐次减小
字符串[开始索引:结束索引:步长]     
"""
num_str="0123456789"
#   截取从2-5位置的字符串
print(num_str[2:6])
#   截取从2-末尾的字符串
print(num_str[2:])
#   截取从开始-5的字符串
print(num_str[:6])
#   截取完整的字符串
print(num_str[:])
#   从开始位置，每隔一个字符截取字符串
print(num_str[::2])
#   从索引1开始，每隔一个取一个
print(num_str[1::2])
#   截取从2~末尾-1的字符串
print(num_str[2:-1])
#   截取字符串末尾两个字符
print(num_str[-2:])
#   字符串的逆序
print(num_str[-1::-1])