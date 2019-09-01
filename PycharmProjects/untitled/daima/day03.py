# -*- coding: utf-8 -*-
#python 基本数据类型 字典

#字典的特点？
#1、以键值对的形式保存数据
#2、键必须是唯一的,键是不可以更改的
#3、值可以是一个或者多个
#4、值可以是数值类型、字符串类型、元组类型、集合类型、列表类型、字典类型

#定义字典的格式
#定义字典的格式
#1、使用英文的{}包裹元素
#2、key 【键】：value【值】 每个字典元素之间使用英文的逗号分隔
# d={
#     "a":["bowen",12]
# }
# print(d)


#定义空字典
# d={} #空字典

# d={
#     "a":123,
#     "b":["bowen",123],
#     "c":["we"]
# }
# print(d)
#向子典内添加元素
# d["a"]="字典的值"
# print(d)

# d["a"]="新的字典值"
# print(d)
#当字典的键存在，再对键进行赋值的时候，会更改原来的键对应的值

#获取字典中键对应的值,通过键取值
# print(d["a"])

#字典的方法
#get（"字典键"）：获取字典中键对应的值
# value=d.get("a")
# print(value)

#key():获取字典中所有的键
# key=d.keys()
# print(key)

#values()：获取字典中所有的值
# values=d.values()
# print (values)

#clear(): 清空字典中所有的元素
# d.clear()
# print(d)

#copy(): 复制字典
# f=d.copy()
# print(f)

#pop("需要被删除的key"):  删除字典中给定key对应的值  返回键对应的值
# s=d.pop("a")
# print(s)
# print(d)

#popitem(): 默认删除字典中最后一个键值对，返回一个新的字典
# d.popitem()  #删除的过程
# print(d)

#len(): 求字典的键值对个数
# l=len(d)
# print(l)

#formkeys(seq,value): 新建字典设置默认值
#seq: 传入一个有序的对象，列表，元祖
#value：设置字典键对应的值，可以不写 None代表空
# seq=[1,"2",4]
#定义新的字典的变量名
# new_d=dict.fromkeys(seq)  #不给出默认值
# print(new_d)

# new_d=dict.fromkeys(seq,"100亿")  #给出默认值
# print(new_d)

#items（）: 将字典中的键值对 转换为元组，可以被循环（for）使用
# c=d.items()
# print(c)

# for i,j in c:
#     print(i,j)

#update("需要添加字典的变量名"):将多个字典组合成一个字典
# d1={1:"hello","a":"字典一"}
# d2={2:"world","b":"字典二"}
#
# d3=d1.update(d2)    #字典组合添加的过程，后面的放进前面的
# print(d1)

#setdefault("key",默认值): 向子典中添加键值对，并设置默认值
#key：需要新增的字典键
#默认值：符合基本数据类型的都行，可以不写，不写默认为None
#k={1:1000,2:2000}
#添加不存在的key，设置默认值
# k.setdefault("key1",999)
# print(k)
#如果设置的key已经存在，不更改键值对
# k.setdefault("key1")
# print(k)

#当直接使用for循环的时候输出的是字典的键
# for i in k:
#     print(i)
#字典转字符串
#print(str(k))
#判断数据类型 使用type（）
#print(type(str(k)))




#不可变得数据类型
#1、数值类型
#2、字符串
#3、元组

#可变的数据类型
#1、列表
#2、字典
#3、集合

#id() 返回变量在内存中的位置
# name="123"
# print(id(name))



##python 基本数据类型  --元祖

#元祖的特点
#1、是一种不可变的数据容器，元祖一旦被定义，里面的元素不可以被修改
#2、支持索引，有顺序

#元祖的书写方式
#1、使用英文的小括号包裹元素()
#2、元素可以是数值、字符串、列表、元祖、字典、集合
#3、每个元素使用英文的逗号分隔
# a=(123,"hello",(32,"python"),[12,23],{12:23,"qw":"qwe"})
# print(a)
#定义空元祖
# t=()
#元祖支持拼接，结果是一个新的元祖
#a1=("hello","world",123,"hai")
# print(a+a1)
#元祖支持重复输出，结果一个新元祖
# print(a1*2)
#元祖支持索引，结果是一个新的结果
#print(a1[1:3])
#print(a1[::-1]) #反转元祖里的元素

#len（） 求元祖的长度
# print(len(a1))

#max()  求元祖的最大值
# t3=("a","b","c","d")
# print(max(t3))
#min()  求元祖的最大值
# t3=("a","b","c","d")
# print(min(t3))

#count("需要统计的元素") 统计元祖中某个元素出现的次数
# print(a)
# print(a.count(1))

#index("需要查找的元素")  返回元素在元祖中的索引值,找不到异常
#异常：tuple.index(x): x not in tuple
# print(a.index(123))

#del 跟元祖的变量名 删除元祖 全部删除，类似于mysql中的drop
# del t3  #NameError: name 't3' is not defined
# print(t3)
#tuple()  列表转元祖
# b = [123, 'xyz', 'zara', 'abc']
# a = tuple(b)
# print(a)

#当元祖里只有一个元素的时候，要加英文的逗号,没逗号是解释器默认是int
# a=(1,)
# print(type(a))

#python 基本数据类型  --集合

#集合的特点
#无序的、不重复的数据容器

#集合的书写格式
#1、使用英文的大括号包裹元素
#2、元素可以是：字符串、元组、数值
#3、每个元素逗号分隔

#定义一个空集合
# s=set()  #{} 空字典
# s1={"ac",2,(202,"qwe")}
# print(s1)

#add("需要添加的元素")  向集合添加元素
# s1.add("python")
# print(s1)
#remove("需要删除的指定元素")   删除集合内的指定元素
# s1.remove('python')  #不存在报错KeyError: 'pytho'
# print(s1)

#pop()   随机删除一个元素，默认删除最后一个元素
# s1.pop()
# print(s1)
#discard("指定删除的元素"）删除集合内的指定元素 指定元素不存在不报错
# s1.discard("ac")
# print(s1)

#update("集合")  将集合B中的元素添加到集合A中
# A={"qwe",2019}
# B={'hello',212}
# A.update(B)
# print(A)
#copy()  复制集合
# b=s1.copy()
# print(b)
#clear()  清空集合 del
# s1.clear()
# print(s1)

# s3={1,2,3,4,5,6}
# s4={3,4,5,6}
#  difference("集合B") ：求集合B相对于集合A的差集
# n=s3.difference(s4)  #s4相对于s3的差集
# print(n)
# difference_update("集合B")删除多个集合都存在的元素，操作是在原集合A上执行的
# s3.difference_update(s4)
# print(s3)
#intersection("集合B")求两个集合A、B的交集，没有交集返回空集
# j=s3.intersection(s4)
# print(j)
#intersection_update("集合B") 删除不是交集的部分，返回删除后的集合A
# s3.intersection_update(s4)
# print(s3)
#isdisjoint("集合B") :判断两个集合A、B是否存在交集，不存在返回True,存在返回False
#print(s3.isdisjoint(s4))
#issubset("集合"A) ：   判断集合B是否是集合A的子集，是返回True，不是返回False
# print(s4.issubset(s3))
#issuperset("集合B"): 判断集合B中的元素是否全部在集合A中，是返回True，不是返回False
# print(s3.issuperset(s4))
#symmetric_difference() :找出两个集合中不重复的元素集合，返回一个新集合
# n3=s3.symmetric_difference(s4)
# print(n3)
#symmetric_difference_update(): 找出两个集合相同的部分，移除集合A在集合B中相同的元素，移除
#集合B在集合A中相同的元素
# s3={1,2,3,4,5,6}
# s4={3,4,5,6,7,8}
# s3.symmetric_difference_update(s4)
# print(s3)
#union("集合B")：求集合A、B的并集，返回一个新集合、重复元素只出现一次
# n4=s3.union(s4)
# print(n4)

#去重
a=[1,22,3,3,4,5,5,5,6,7]
#a={1,2,3,3,4,5,5,6,6,7}
print(set(a))     #返回字典
print(list(set(a)))    #返回列表


# b={"a","a","cd","cs","cd",12,34}
# print(list(set(b)))
#

# import random  #随机数模块
# a=random .randint(0,10) #随机生成一个整数
# print(a)


#将列表 li=["alex","seven"] 转换成字典且字典的 key 按照 10 开始向后递增
# li=["alex","seven"]
# li_dic = {}
# for k,v in enumerate(li,10):
#     li_dic[k] = v
#     print(f"k={k}")
# print(li_dic)


