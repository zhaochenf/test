#!/usr/bin/python
#-*- coding:utf-8 -*-
with open(file=r"D:\QQ\data\1.txt",mode="r",encoding="utf-8") as fb:
    date=fb.read().split(';')
s=[]
for i in date:
    k=i.replace('\n','').split(',')
    s.append(tuple(k))
print(s)