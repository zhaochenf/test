#-*- coding: utf-8 -*-

# python 异常处理 https://juejin.im/entry/5a713192518825732a6dce43

#错误

# 1 python语法错误：书写格式、缩进
# 2 代码逻辑：python解释器无法编译解释，导致python报错

#异常:
#处理错误的过程被称为异常处理

# try …… except   最简单的异常处理

"""
try:
    d=1/0
    print(d)
#OverflowError  最大值异常  ZeroDivisionError 除数不能为0
except OverflowError:
    print("异常已经被处理了")
except ZeroDivisionError:
    print("ZeroDivisionError异常已经被处理了")

 """

#try …… except……finally

"""
try:
    d = 1 / 0
    print(d)
# OverflowError  最大值异常  ZeroDivisionError 除数不能为0
except OverflowError:
    print("异常已经被处理了")
except ZeroDivisionError:
    print("ZeroDivisionError异常已经被处理了")

finally:
    print("无论异常是否被处理，都会输出finally下面的代码")
"""

# try ……except……else

"""
try:
    d = 1 / 10
    print(d)
# OverflowError  最大值异常  ZeroDivisionError 除数不能为0
except OverflowError:
    print("异常已经被处理了")
except ZeroDivisionError:
    print("ZeroDivisionError异常已经被处理了")

else:
    print("不存在异常处理,else下面的代码")
"""

#python  --with语句

#1、with 应用场合：主要是操作系统资源、建立连接、python线程、进程的关闭释放
#2、with 一种概念：上下文管理
#3、with 格式：
#   with 语句块 as 变量名
#         语句块

#读取文件内容

# with open('b.txt','r',encoding='utf-8') as fb:
#     a=fb.read()
#     #a=fb.write('abcd')   #写入
#     print(a)


# python --正则   https://docs.python.org/zh-cn/3/library/re.html
# 正则模块 re
# 正则只能匹配字符串

import re

#s="abccabc"
# 1 . 代表除了\n以外的所有字符，一个.代表一个字符
# 2 * 匹配*前面的字符0次货多次
# 3 + 匹配+前面的字符1次或多次
# 4 ？ 匹配？前面的字符0次或一次
# 5 ^  匹配字符串以某个字符开头
# 6 $ 匹配字符串以某个字符结尾
s='python'
x=re.compile('^p.*')
res=re.match(x,s)
print(res)
# 7 {m} 匹配花括号前面字符出现的指定次数
# s="abccabc"
# x=re.compile('ab{1}')
# res=re.match(x,s)
# print(res)
#9 {m,n}  匹配花括号前面的字符出现的指定次数，最少m次，最多n次
# s="abccabc"
# x=re.compile('ab{1}')
# res=re.match(x,s)
# print(res)
# 10  [] 匹配中括号内的任意一个字符,每个字符匹配一次 [a-z] [A-Z] 26个大小写字母 [0-9] 数字
# s="abbccabc"
# x=re.compile('a[bc]')
# res=re.match(x,s)
# print(res)
# 11 | 匹配左右的表达式
# s="abbccabc"
# x=re.compile('ab|c')
# res=re.match(x,s)
# print(res)
# 12  \D 匹配任何非十进制数字的字符  0-9
#     \d  匹配任何十进制数字的字符 0-9
# s="123123"
# x=re.compile('\D')
# res=re.match(x,s)
# print(res)
# 13 \s  匹配空白字符 空格   \t \n \f \v
#     \S   匹配除空白字符的任意字符
# s="\t123123"
# x=re.compile('\s')
# res=re.match(x,s)
# print(res)
# 14 () 匹配括号内的字符
# s="http://www.baidu.com"
# x=re.compile('http://www.(.*?).com')
# res=re.match(x,s)
# print(res.group())

#编译正则表达式
#x=re.compile('.')
#x=re.compile('ab{1}')
# res=re.match(x,s)
# print(res)

# a=re.match("...",s)
# print(a)
#匹配正则
# re.match(编译好的正则，字符串)   从左往右开始匹配，第一个字符匹配不到的话，就停止，返回None
#re.search(编译好的正则，字符串） 从左往右对整个字符串进行搜索匹配、匹配不到返回None、匹配到第一个停止
#匹配不成功返回None
#group() 获取匹配到的内容
# re.findall(编译好的正则，字符串)  从左往右对整个字符串进行搜索匹配，匹配到的内容保存到列表
#使用（） 时仅仅匹配括号里的内容
# s="http://www.baidu.com"
# x=re.compile('www..*.c')
#s="http://www.baidu.comhttps://www.360.com"
# x=re.compile('www..*.c')
# x=re.compile('www.(.*?).com')
# res=re.findall(x,s)
# print(res)
#贪婪模式 .*  尽可能多的匹配字符
#非贪婪 .*?   匹配到字符就停止


#re.sub(正则表达式，要替换的字符，要匹配的字符串)
# g="hello world"
# k=re.sub('l','kk',g)
# print(k)

#把f替换成 1,234,567,890
# f='1234567890'
# k=re.sub('1234567890','1,234,567,890',f)
# #k=re.sub('')
# print(k)

a="dfe123\nqwe"
#print(a)
cc=re.compile("df(.*)w",re.S)  #re.I不区分大小写
#. 匹配任意字符
# re.S 给.加功能，让点匹配到包括换行符在内的任意字符
bb=re.findall(cc,a) #写法一
#bb=cc.findall(a)   #写法二
print(bb)


