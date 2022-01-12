"""
函数基础

所谓函数，就是把具有独立功能的代码块组置为一个小模块，在需要的时候调用，函数的使用包含两个步骤：
    1、定义函数--封装独立的功能
    2、调用函数--享受封装的成果
定义函数的格式如下：
    def 函数名():
        函数封装的代码
        ....

    1、def 是英文define的缩写
    2、函数名称应该表达函数封装代码的功能，方便后续的调用
    3、函数名称的命名应该符合标识符的命名规则
        可以由字母、下划线和数字组成
        不能以数字开头
        不能与关键字重名
    
    函数的返回值
    语法 return 返回内容

"""
def muilt(max):
    """乘法表"""
    index = 1
    print(sayHello(1,2))
    while index<=max:
        index1=0
        while index1<=index:
            print("%d * %d = %d"%(index,index1,index*index1),end="\t")
            index1+=1;
        index+=1;
        print()

def sayHello(num1,num2):
    """输出测试"""
    return num1+num2

muilt(4)


