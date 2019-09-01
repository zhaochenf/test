# -*- coding: utf-8 -*-

# python--函数

#函数的作用
#1、使代码重复被使用
#2、减少代码量

#函数的定义
#一段代码的封装被称为函数

#函数的书写格式
#1、定义函数的关键字  def
#2、函数名：要符合变量的命名规则
#3、参数：关键字(必填）参数、默认参数、可变长参数
#4、返回值：使用关键字  return

# def add(x):
    #写求和代码
    # b=0
    # for i in range(x):
    #     b+=i
    # print(b)
    # return b  #return是将结果传送给函数  b是要返回的结果
    # return    #没有返回结果，返回空None
#一个函数使用return 但是没有返回结果的时候 返回None
#一个函数不使用return的时候 返回None（空值）
# print(add(201))

#如何使用函数
#1、函数的名字
#2、有参数对参数进行赋值

#sum()   #pythonde 内置函数   求和
#print(sum(range(101)))

#全局变量、局部变量、函数的作用域、函数的变量

#全部变量：定义之后整个脚本都可使用
#a="全部变量"
#print(a)

#局部变量：定义之后只能在一定的范围内使用
# def bo():
#     c="局部变量"
#     print(c)
#     return c
# bo() #等价于局部变量
# print(bo())

#将局部转为全局

#使用关键字：global
#作用：1、将局部变量转变成全局变量 2、修改全局变量的数据类型

#定义一个函数
# def k():
#     global p  #p 代表全局变量
#     p=100     #局部变量
#
# k()
# #验证p是否是全局变量
# print(p)

#修改全局变量的数据类型
#当全局变量和局部变量是同一个变量名的时候，函数优先使用局部变量
# ,当函数内没有局部变量时，向上查找相同变量名的全局变量
#找不到需要的全局变量时，代码报错NameError: name 'g' is not defined
# g="全局变量"
# def k():
#     global g  #全局变量
#     g=1000
#     print(g)
# k()
# print(g)

#pycharm 调试
#红点：被称为调试断点
#进入调试模式：绿色的小虫子
# def k(x1,x2):
#     c=x1+x2
#     print(c)
#     return c
#     print("超出函数的作用域之后，会执行吗")
# k(100,200)

#函数的作用域
#从定义函数的那一行开始一直return那一行结束
# def bo(x):
#     a=0
#     b=1
#     for i in range(1,x+1): # 阶乘之和
#         b=b*i
#         a=a+b
#     print(a)
#     return a
# print(bo(5))

#函数的参数分类
#1、必填参数：参数定义之后，在函数被使用的时候，必须传入赋值的参数
#2、默认参数：在参数被定义的时候，参数有一个默认值，在函数使用的时候，对默认参数赋值，则使用赋予值
#不对默认参数赋值，就是用默认值
# def k(x1,x2=5000): #x2=5000 x2默认参数 默认值5000
#     c=x1+x2
#     print(c)
#     return c
# print(k(100,1))
#3可变长参数：
#a、以元祖的形式赋值
# def all(*args):
#     print(args)
# all((1,2,3,45))
# all(1,2,3,45)

# def all(*args):   #args为可变长参数  可为其他 如：asd
#     x1,x2,x3=args
#     print(x1)
#     print(x2)
#     print(x3)
# all(1,2,3)

# def all(*cc):
#     m=len(cc)
#     for i in range(0,m):
#         a=cc[i]
#         c=f"s_{i+1}"
#         print(f"{c}对应的值为{a}")
# all(1,2,"qw",3)

#b、以字典的形式赋值
def k(**kwargs):
    print(kwargs)  #kwargs 字典，关于字典的所有函数都可以使用
    values=kwargs.values()
    print(values)

# #参数传递 写法一
#k(a=1,b=2,c=3)
# #写法二：先写成一个字典，**变量名
# n={"x1":4,"x2":5,"x3":6}
# k(**n)

#函数的嵌套

"""
def foo():
    #函数语句块
    return "我是foo函数返回的一段话"

def k():
    print("此时运行函数k")
    print(foo()) #执行foo函数
k()
"""


# def foo():
#     x=100 #局部变量
#     def k():
#         c=x*10
#         return c
#     return k
# print(foo()())

#@....  python的语法糖（装饰器）

#lambda   python的匿名函数

#匿名函数
#1、函数没有名字
#2、使用lambda定义
#3、作用和函数的作用相同

#定义匿名函数的格式
#lambda 参数1,参数2，……:函数语句块（表达式）
# a=lambda n,m:(n+m)*n
# print(a(2,3))
#
# a=lambda n:n+1
# print(a(1))

# import random
# a=lambda n: random.randint(1,10)*n
# print(a(3))

# b=random.randint(1,10)
# print(b)
#
# c=[i for i in range(10)]  #python列表推导式
# c.reverse()
# print(c)
# print(c[::-1])
#
#python列表推导式

#列表推导式定义
#1、生成的结果是新的列表
#2、使用循环语句、if语句
#3、使用python的库（模块）
#4、使用函数

#列表推导式格式
#[表达式 for 变量 in 列表]    或者  [表达式 for 变量 in 列表 if 条件]

#生成1~10的列表
# a=[i for i in range(1,11) if i>5]
# print(a)

# a=[lambda m :m+i for i in range(1,11) if i>5]
# #a=[l1,l2,l3,l4,l5]
# print(a[0](10))

#a=[[1,2],[3,4],[5,6]]
#a = [x for y in a for x in y  ]
#print(a)

# def function(x,y,*args):
#     print(x,y,args)
#
# function(1,2,3,4,5,6,7,8)

#open(): 打开文件、txt文件、Excel文件
#如何查看源代码
#1、选中
#2、Ctrl +B

#open()
#file：文件的名字 a.txt  b.excel
#mode='r': 读取文件的模式，r：读取模式 w:写入模式 a:追加写入模式 b:二进制写入 +:追加
#encoding=None：指定文件的编码方式，utf-8,utf-16 ,gbk,gb2312

#向文件写入内容
"""
f=open(file="a.txt",mode="w",encoding="utf-8")
#write(): 写入  传入字符串、想写入的文字
f.write("hello python")
#close(): 关闭
f.close()
"""
"""
#读取文件中内容

f=open(file="a.txt",mode="r",encoding="utf-8")
#read():读取文件所有的内容
#text=f.read()
#print(text)

#readlines(n):  每次读取一行，n有数值，读取指定数值的行数
text=f.readlines(5) #返回一个 列表
print(text)
# c=[]
# for i in text:
#     c.append(i.strip())
# print(c)
f.close()
"""

# a=["a","b","c"]
# f=open(file="a.txt",mode="w",encoding="utf-8")
# for i in a:
#     #f.write(f"{i}\n")
#     f.write(i+"\n")
# f.close()

#输入文件名可查看文件内容
# def foo(a):
#     f = open( file=a,mode="r", encoding="utf-8")
#     text = f.read()
#     #print(text)
#     f.close()
#     return text
#
# print(foo("a.txt"))

# def k(h):
#     f = open(file=h,mode="r",encoding="utf-8")
#     s = f.read()
#
#     b = []
#     for i in s:
#         b.append(i.strip())
#
#     f.close()
#     return b
# print(k("a.txt"))
#


#python---面向对象(oop)

#类是对客观世界中事物的抽象，而对象是类实例化后的实体

#1、面向对象是一种高级编程语言的编程思想
#   面向过程--函数式编程--面向对象
#2、作用：
#   a、减少代码的重复性
#   b、减少变量引用
#3、面向对象的特点
#  a、封装
#  b、继承
#  c、多态
#4、类的组成（三要素）
#  a、方法
#  b、属性#
#5、类的书写格式
#  a、class 关键字，定义一个类
#  b、每个单词的首字母大写
#  c、object：代表python所有类的基础
#   d、面向过程、函数式代码的语句块

#例如
#class 类名(object):
#     语句块(面向过程、函数式)

#定义一个类
"""
class Student(object):
    #类的属性
    height=170     #身高
    weight=180     #体重
    def name(self,n):
        k="hello"    #局部变量(实例属性)
        print(f"有个人叫{n},他的身高{self.height}cm,体重{self.weight}Kg")
        print(k)

#类的使用
s1=Student() #被称为对象/类的实例
#类的实例使用类的方法
s1.name("哈哈")
"""



# class country(object):
#     a="建党节"
#     b="7.1"
#     c="中国"
#     def qwe(self,n):
#         print(f"名字:{n},节日:{self.a},日期:{self.b},国家:{self.c}")
# country().qwe("中国共产党")

class A(object ):
    #类的属性
    banji=12
    __sex="男"     #类的私有属性
    def __init__(self,name,age):   #类的构造方法
        #如果定义了init方法，在创造对象的时候，必须传入参数
        #对象的属性
        self.name=name
        self.age=age
        self.__g="abc"  #对象的私有属性
    #普通方法
    def show(self):
        k="hello"  #局部变量
        print(f"有个人的名字叫{self.name},年龄是{self.age},班级是{self.banji}")
        #print(k)
        #在类的方法内使用类的属性（公有、私有），对象属性（公有、私有）
        print(f"公有类属性{self.banji},私有类属性{self.__sex},"
              f"公有对象属性{self.age},私有对象属性{self.__g}")

    @staticmethod
    def foo():   #静态方法-->类似于函数
        print("类的静态方法")
    @classmethod
    def koo(cls):    #类方法 cls和self的作用一致，只不过换了个名字而已
        print("类的类方法")
    def __siyou(self):  #私有方法
        print("类的私有方法")

    def yu(self):
        #在类的方法中使用其他方法的方式
        #self.方法名（所有的方法）
        self.__siyou()

#类的方法可以被那些使用？
#A.show()   #报错
#a=A("张三",12)
#a.yu()
# a.show()   #对象名.普通方法名-->使用普通方法
# a.foo()    #对象名.静态方法名-->使用静态方法
# a.koo()    #对象名.类方法名-->使用类方法
# #a.__siyou()  #报错
# A.foo()
# A.koo()
"""
1、类中的普通方法不能被类名.方法名的方式使用
2、对象名.普通方法名-->使用普通方法
3、对象名.静态方法名-->使用静态方法
 @staticmethod：将普通方法转变为静态方法的装饰器
4、对象名.类方法名-->使用类方法
 @classmethod：将普通方法转变为类方法的装饰器
5、私有方法不可以在类的外部使用
6、类名.类方法名/类名.静态方法名 可以使用类方法、静态方法
"""
#类的属性可以被哪些使用
#print(A.banji)  #类的共有属性，可以直接使用类名.属名性
#print(A.__sex)  #类的私有属性，不能在类的外部通过类名.属性名的方式使用
"""
1、类的共有属性，可以直接使用类名.属名性
2、类的私有属性，不能在类的外部通过类名.属性名的方式使用
3、对象公有属性，通过对象名.属性名的方式使用
4、对象私有属性，不能再类外部通过对象名.属性名的方式使用
5、类名.对象的属性是不可以的
6、私有属性在定义之后，不希望被修改，可以通过：self.__变量名/self._类名__变量名的方式使用它



#对象使用类的属性
a=A("张三",99)
#print(a.banji)
print(a.age)
#print(a.__g)


#类的使用
a=A("张三",12)   #这个是创造对象的过程
a.show() #对象使用类的方法，类的方法只有类的对象才能用
"""
# class  HelloWord(object):
#     r = input("输入")
#     t = input("输入")
#     def h(self,x):
#         if len(self.r) > len(self.t):
#             print(type(len(self.r)))
#             print(f"条件{x}成立。A问：{self.r}，B回答：{self.t}")
#         else:
#             print("没事没事")
#
# a = HelloWord()
# a.h("ds")

#属性？
#1、类的属性
#   私有
#   共有
#2、对象（实例）属性

"""
区分类的属性和对象属性
1、类的属性：定义在类的内部、方法的外部
2、对象属性：定义在init方法的内部
"""
"""
公有和私有？
私有是以双下划线开头：__sex="男"
"""

#方法：静态方法 类方法 普通方法 私有方法


#-- 继承
"""
class B(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print(f"B类中的普通方法")
        return self.name,self.age

#(类名)：代表继承于XX类，只要被继承类有的，继承类都可以直接使用
class C(B):

    def talk(self):
        #res=self.say()
        res=super().say()
        print(res)
    #多态-->重写方法
    def say(self):
        print("C类里的方法")

c1=C("李四",21)
c1.talk()
c1.say()
"""
"""
多态：继承类对被继承类的方法的重写（方法名一样，语句块不一样）
如何使用在多态之后使用被继承类的方法？
  使用supper().被继承类的方法
"""
"""
class A(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class B(A):
    def __init__(self,sex,name,age):
        A.__init__(self,name,age)
    def abc(self):
        print(sex,name,age)
a=B("李四",23,"zhao")
a.A()
"""



"""
pip-->path
python的第三方包下载工具
作用？
下载python的第三方包
什么是python的包？
python脚本文件的汇总，集合被称为包
pip命令？
pip install 包名  下载包，找到下载
pip list  查看pip下载过的所有包
pip install PyMySQL  下载mysql包

impore json  库
json.loads(想转的内容)   将json转为python字典
json.dumps(想转的内容)    将python字典转成json字符串

https://www.runoob.com/python/python-json.html

"""


import paramiko
class A(object):
    t=paramiko.Transport('192.168.10.29',22)
    t.connect(username='root',password='123456')
    def __init__(self,name1,name2):
        self.name1=name1
        self.name2=name2
    def qwe(self):
        sftp=paramiko.SFTPClient.from_transport(self.t)
        x=self.name1
        y=self.name2
        sftp.get(x,y)
        self.t.close()
a=('')