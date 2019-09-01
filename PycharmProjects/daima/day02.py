# -*- coding: utf-8 -*-
#模拟天猫登录脚本
# name = input("请输入用户名")
# password = input ("请输入密码")
#
# if name =="赵晨飞":
#     if password == "123456":
#         print("登录成功")
#     else:
#         print("密码错误，登录失败")
# else:
#     print("登录失败，登录失败")
# num_1=10
# num_2=20
# 1、 * 应用于多个数字变量的求积
# h=num_1*num_2
# print(h)
# 2、 / 应用于多个数字变量的求商
# k=num_2 / num_1
# print(k)
# 3、 % 应用于多个数字变量的求模（求余）
# num_3 = 101
# num_4 = 5
# g=num_3 % nnum_1 = 10
# 4、 + 应用于多个数字变量的求和
# t = num_1+num_2
# print(t)
# 5、 - 应用于多个数字变量的求差
# s=num_1-num_2
# print(s)um_4
# print(g)
# 6、  ** 应用于多个数字变量的求幂（次方）
# print(num_1 ** num_2)
# 7、 //  应用于多个数字变量的相除求整数
# t = num_3 // num_4
# print(t)


# 计算器 输入任意两个数字进行计算，选择计算方式
# numa= int(input("请输入第一个数字"))
# numb= int(input("请输入第二个数字"))
# ji = int(input("请选择计算方式 1相加 2相减 3相乘 4相除 "))
# if ji == 1:
#     A = numa + numb
#     print(A)
# elif ji == 2:
#     B= numa - numb
#     print(B)
# elif ji == 3:
#     C= numa * numb
#     print(C)
# elif ji == 4:
#     D= numa / numb
#     print(D)
# else:
#     print("你的计算方法没有")
# 判断学生成绩情况优秀及格良好不及格
# num = int(input("请输入成绩"))
# if num >= 90:
#     print("优秀")
# elif   80 <= num <90:
#     print("良好")
# elif  60 <= num <80:
#     print("及格")
# else:
#     print("不及格")
# 赋值运算符
# 1、 = 赋值运算法   arg = 20
# 2、 += 加法赋值运算法  arg += 100   arg = arg +100
# 3、 -=减法             arg -= 100   arg = arg -100
# 4、 *= 乘法            arg *= 100   arg = arg *100
# 5、 /= 除法             arg /= 100  arg = arg /100
# 6、 %= 求余数          arg %= 100   arg = arg %100
# 7、 **= 幂等           arg **= 100   arg = arg **100
# 8、 //= 求商           arg //=100    arg = arg //100
# arg = 20
# arg += 100
# print(arg)

# 逻辑运算法
# and 与运算：第一个条件为假，不判断第二个条件  两个条件
# or  或运算： 第一个条件为假，继续判断第二个条件 两个条件
# not 非运算：把真返回假吧，假返回真 两个条件
# x = 100
# y = 50
# z = 30
# if x > y and  y > z:
#     print("x的值最大")
# if  x == 100:
#     print("x等于100")
# if  y != 50:
#     print("y不等于50")
# else:
#     print("not语句不成立")
# 判断三角形
# a=int(input("输入第一边"))
# b=int(input("输入第二边"))
# c=int(input("输入第三边"))
# if a + b > c and  a+c > b and  b+c > a:
#     if a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or b**2 + c**2 > a**2:
#         print("锐角")
#     elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
#         print("钝角")
#     elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print("直角")
# else:
#     print("不是三角形")
#判断三个数的大小 最大 最小 第二大
# a=int(input("输入第一数"))
# b=int(input("输入第二数"))
# c=int(input("输入第三数"))
# if a > b > c:
#     print(a, c ,b)
# elif a < b < c:
#     print(c ,a ,b)
# elif a > c > b:
#     print(a ,b, c )
# elif b > a > c:
#     print(b,c,a)
# elif b > c > a:
#     print(b,a,c)
# elif b < a < c:
#     print(c,b,a)
#  成员运算符--> 判断子成员是否在某个序列内
#  in 在  --> true       不在 -->false
# not in 不在   --> false   在-> true
# str1 = "zhao chen fei"
# str2 = "博文"
# if str1 in str2:
#     print("in 条件成立")
# else:
#     print("in 不条件成立")
# 字符串
# str1 ="hello"
# str2="world"
# str3="123"
# 求字符串长度
# l=len(str1)
# print(l)
#字符串拼接
# new_str = str1 + str2
# print(new_str)
#字符串重复输出
# print("团长，你倒是开跑呀!\n" * 5)
#字符串切片 步长指的是间隔几个取值 默认是1 开始的索引值默认是0 结束索引默认是最后一个
# s="博文智生1903届小朋友"
#[开始：结束：步长]
# print(s[1:8])
# print(s[1:8:2])
#取字符 字符串变量名字[索引值]  从左往右0开始  从右往左 -1 开始
# print(s[-2])


#1、find():查找字符串中的子字符串,如果找到，返回子字符串的第一个字符的索引值，找不到结果是-1
#   rfind()  从右开始
#定义字符串a
# a="hello"
#定义子字符串b
# b="o"
# print(a.find(b))
#2、index():查找字符串中的子字符串,如果找到，返回子字符串的第一个字符的索引值，找不到抛出异
#   rindex  从右开始
# 定义字符串a
# a="hello"
#定义子字符串b
# b="h"
# print(a.index(b))
#异常报错的关注点
#(1)、最后一行指的报错类型：报错内容
#(2)、那个文件，哪一行报错
#3、title():将英文单词首字母大写，其他的字母小写
# str="hello world"
# print(str.title())
#4、upper():将所有英文小写字母转换成大写的英文字母
# str1="hello python"
# print(str1.upper())
#5、swapcase():将所有英文大写字母转成小写的英文字母,如果里面有小写，将小写转为大写
# str2="HELLO WORLD"
# print(str2.swapcase())
# 6、count() 子字符串在字符串出现的次数，返回的结果是数字,不存在于字符串中，返回数字0
# str3="123123bowen python"
# c="o"
# print(str3.count(c))
#7、startswith():判断字符串是否以某个子字符串开头，是的话，返回布尔值True,不是则返回False
# print(str3.startswith("bowen"))
# print(str3.startswith("1"))
#8、endswith():判断字符串是否以某个子字符串结尾，是的话，返回布尔值True,不是则返回False
# print(str3.endswith("python"))
# print(str3.endswith("bowen"))
#9、max():求字符串中的最大值,返回根据字符的编码方式 asscii码最大值的字符
# str4="0123abcd"
# print(max(str4))
#10、min():求字符串中的最小值,返回根据字符的编码方式 asscii码最小值的字符
# print(min(str4))
#11、格式化字符串输出，变量放在字符串中，让他输出变量对应的值
#(1)f"字符串{变量名}"
#(2)"字符串{}".format(变量名)
#(3)%s 输出字符串  %d 输出数字
# name ="博文"
# age=18
#第一种
# str5=("我在的学校是%s"%(name),"我今年%d岁"%(age))
# print(str5)
#第二种
# str5=f"我在的学校是{name},我今年{age}岁"
# print(str5)
#第三种
# str5="我在的学校是{},我今年{}岁".format(name,age)
# print(str5)
#12、split() 切割字符串，指定字符或者字符串进行切割，返回一个列表，指定切割次数,指定字符不能为空
# str7="I know I beautiful"
# g=str7.split(" ",2)
# print(g)
# 例：python 使用input(),输入一段英文，每个英文单词以空格分割，求最后一个单词长度
#a=input("请输入一段英文")
#s=a.split(" ")
#print(f"最后一个单词长度：{len(s[-1])}")
#13、lstrip():删除字符串的指定字符，默认删除空格，从左侧开始,指定字符串不存在就不删除
#str8=" 博文 智生1903届"
# print(f"删除之后的字符串:{str8.lstrip('博')}")

#14、rstrip():删除字符串的指定字符，默认删除空格，从右侧开始,指定字符串不存在就不删除
#15、strip():删除字符串的指定字符，默认删除空格，两边同时删除,指定字符串不存在就不删除
#print(f"使用strip操作之后的字符串:{str8.strip('19')}")
#16、repleace():替换字符串中的字符或子字符串，第一个是原始字符，第二个新的字符,
# 如果原始字符不存在，不替换，保持原样输出
#str9="I,know,I,beautiful "
#print(str9.replace(","," "))
#原始字符不存在
# print(str9.replace("123456"," "))
#17、join(): 将列表中的元素拼接成字符串,第一个变量必须是字符串，第二个是列表
# s1="_"
# s2=["1","2","3"]
# print(s1.join(s2))

#返回布尔值
#18、isdigit() 判断字符串的字符全部都是数字，如果是返回True,不是返回False
# s="1233"
# print(s.isdigit())
#19、istitle()  判断字符串是否为标题，如果是返回True,不是返回False
# str10="Hello World"
# print(str10.istitle())
#20、isupper() 判断字符串中的字母全部是大写，如果是返回True,不是返回False
# str11="HEELO WORLD"
# print(str11.isupper())
#21、islower() 判断字符串中的字母全部是小写，如果是返回True,不是返回False
# str12="hello world"
# print(str12.islower())
#22、isalnum(): 判断字符串中所有字符由数字或字母组成，如果是返回True,不是返回False
# str13="123on"
# "qwe\n"
# "123"
# print(str13.isalnum())
#23、isalpha(): 判断字符串中所有的字符全部是字母，如果是返回True,不是返回False
# str14="niha"
# "qw qq"
# "xx\n"
# print(str14.isalpha())
#24、isspace():判断字符串中只包含空白字符，如果是返回True,不是返回False
#空白字符包含：空格 、\n、\t、\r（回车）
# str15=" "
# print(str15.isspace())
#25、isdecimal() 判断字符串是否只包含十进制的数字，如果是返回True,不是返回False
# str16="0o14" #表示八进制 -->对应十进制12
# print(str16.isdecimal())

# s="Hello World"
# for i in s:
    # print(f"子字符串是{i}")

# print(range(1,10))
#99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}x{i}={j*i}\t",end="")
#     print()



#python 基本数据类型---列表

#列表的组成？
#1、英文的中括号[]
#2、列表里可以放字符串、数字、列表、元祖、字典、集合
#3、有序的、可以变得数据容器（列表定义）
#4、每个元素以英文的逗号分隔

#定义一个列表
# l=["abc",1,["hello",2019]]
#print(l)
#定义一个空列表
#s=[] # 0、空字符串、空列表、空元祖、空字典、空集合在if条件判断的时候全部返回false

#索引值取列表中的元素
#print(l[0:2])
#print(l[-1])   #当只取一个元素的时候返回该元素本身的数据类型
#type() 是用来判断数据类型的
#print(type(l[-1]))
#如何获取列表中的列表元素？
#k=l[-1] #["hello",2019]
#print(k[0])
#print(l[-1][0])
#替换列表中的元素
# print(f"之前的l列表{l}")
# l[0]="博文"
# print(f"之后的l列表{l}")
#向列表中添加元素  append（需要添加的元素）,在列表的尾部新增添加元素
# l.append('python')
# print(f"添加元素之后的l列表{l}")

#列表支持拼接，将多个列表的元素放到一个列表内
# l1=[1,2,3]
# l2=["a","b","c"]
# l3=l1+l2
# print(l3)   #[1,2,3,'a','b','c']

#支持重复输出，将重复输出的元素放到一个列表内
# print(l2*2)
#列表反转
# print(l1[::-1])

#count(需要统计的元素） 统计列表中某个元素出现的次数，返回的是数值,如果需要统计的元素不存在，返回数值0
# a=["a","a","a",1,2,3]
# c=a.count("a")
# print(f"a在列表中出现的次数{c}")

#extend（需要添加的元素） 向列表内添加元素，可以添加多个元素，默认添加到列表的尾部
# 需要添加的元素：可以是列表、元祖、集合、字典
# b=["123",456]
# c=["hello","python"]
# b.extend(c)  #向列表b添加多个元素的过程
# print(b)

#index(需要查找的元素）：如果找到该元素返回元素对应的索引值,找不到抛出异常
# b=["123",456]
# print(b.index(456)) #找到情景
# print(b.index("abc"))  #找不到情景

#insert(index,需要添加的元素）：向列表内的指定位置插入元素
# index：指索引值
# c=[1,2,4]
# c.insert(2,["123","456",12])
# print(c)

#pop(索引值) 删除列表中的元素，当索引值不写的时候，默认删除最后一个元素,返回被删除的元素
# k=[1,2,3,4,5,"hello"]
# print(k.pop(3))
# print(k)

#remove(指定需要删除的元素）： 删除列表中元素
# k=[1,2,3,4,5,"hello"]
# k.remove(2)
# print(k)

#reverse()：  反转列表中的元素
# a=[1,2,3,4,5,6]
# a.reverse()#反转过程
# print(a)

#sort（reverse=False）： 对列表内的元素进行排序，按照asscii,默认升序
#reverse=True  降序,不能使用多种类型
#使用多种类型报错：TypeError: '<' not supported between instances of 'str' and 'int'
# a=[2,5,1]
# a.sort(reverse=True)
# print(a)

#clear(): 清空列表
# a=[1,2,3,4,5]
# a.clear()
# print(a)

#copy(): 复制列表,浅copy
# a=[1,2,3,4]
# b=a.copy()
# print(a)
# print(b)

#len():   求列表长度
# d=[1,2,3,4]
# print(len(d))

#max() 求列表中的元素的最大值,不能使用多种类型
# a=[1,2,3,4]
# print(max(a))

#min() 求列表中的元素的最小值,不能使用多种类型
# a=[1,2,3,4]
# print(min(a))

#list():  将非列表类型转换为列表类型
# str="12345"
# print(list(str))

#enumerate()   形成有序的序列
#k=["a","b","c","d"]
# print(enumerate(a))
# for i,j in enumerate(k):
#     print(i,j)


# a1.sort()
# print(f"身高范围是{a[0]}--{a[-1]}")
