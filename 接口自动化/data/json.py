#!/usr/bin/python
#-*- coding:utf-8 -*-
#import json
import requests
import re
"""
json  是一种轻量级的数据交互格式
  JavaScript语言中的一种表现形式
python中没有json    格式和字典一样

import json ：是一个模块
"""
# a={'name':123,'age':456}
# print(a)
# #将字典转换成json字符串
# b=json.dumps(a)
# print(type(b))
# #将json字符串转换成字典
# c=json.loads(b)
# print(type(c))

url=''
bb=requests.get(url)
#以字节的方式接受结果 content
#以字符串的方式接受结果  text
#以json的方式接受结果 json
cc=bb.json()  #json.loads(cc)
#print(cc['rgv587_flag'])
