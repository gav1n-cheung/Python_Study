"""
模块是pyhton程序架构的一个核心概念
模块好比是工具包，要使用这个工具包中的工具，就需要 导入 import 这个模块
每一个以拓展名 py 结尾的python源代码的都是一个模块
在模块中定义的全局变量、函数都是模块能够提供给外界直接使用的工具

模块名也是一个标识符
    标识符可以由字母、下划线和数字组成
    不能以数字开头
    不能与关键字重名
        如果在给python文件起名时，以数字开头是无法在IDE中导入这个模块的
"""
import test_import
print(test_import.name)